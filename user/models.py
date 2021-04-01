import re

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from rest_framework.validators import ValidationError

from helpers.models import TimeStamp


def validate_image(image):
    if image.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise ValidationError("Must be an image of type jpeg, jpg, or png")
    # 0.5 MB
    if image.size > 0.5 * 1024 * 1024:
        raise ValidationError("Maximum file size is 500kb")


def validate_pwd(password):
    if not re.findall(r"\d", password):
        raise ValidationError("The password must contain at least 1 digit, 0-9.")

    if len(password) < 6:
        raise ValidationError("The password must must be of at least 6 characters")


class UserManager(BaseUserManager):
    def create_user(
        self, email, password, lastname, firstname, date_of_birth, **extrafields
    ):
        if not email:
            ValueError("Email field is required")
        if not firstname:
            ValueError("Firstname field is required")
        if not lastname:
            ValueError("Lastname field is required")
        if not date_of_birth:
            ValueError("Date of birth field is required")

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            firstname=firstname,
            lastname=lastname,
            date_of_birth=date_of_birth,
            **extrafields
        )

        user.is_active = True
        user.set_password(password)
        user.save(using=self.db)
        return user

    # explicit over implicit
    def create_superuser(self, email, password, lastname, firstname, date_of_birth):
        user = self.create_user(email, password, lastname, firstname, date_of_birth)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, TimeStamp):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    # note that the default character numbers must be less than or 100
    # add https: // res.cloudinary.com / dnrh79klc + /image/path
    image = CloudinaryField(
        "image",
        default="https://res.cloudinary.com/health-id/image/upload/v1554552278/Profile_Picture_Placeholder.png",
        validators=[validate_image],
    )
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100, validators=[validate_pwd])
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # ensure this is objects and not object
    # else User.objects.all() won't work
    # it has to be Class.object.all()
    # and most 3rd party packages depend on objects
    objects = UserManager()

    REQUIRED_FIELDS = ["firstname", "lastname", "date_of_birth"]
    USERNAME_FIELD = "email"

    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_username(self):
        return self.email

    # allows assignment property to the image value
    # from the view
    def __setitem__(self, key, value):
        self.image = value

    @property
    def is_staff(self):
        return self.is_admin
