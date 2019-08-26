
[![Build Status](https://travis-ci.org/klevamane/Airtech.svg?branch=develop)](https://travis-ci.org/klevamane/Airtech)  [![Maintainability](https://api.codeclimate.com/v1/badges/b2e9924c1204f0bb5c52/maintainability)](https://codeclimate.com/github/klevamane/Airtech/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/b2e9924c1204f0bb5c52/test_coverage)](https://codeclimate.com/github/klevamane/Airtech/test_coverage)
[![Coverage Status](https://coveralls.io/repos/github/klevamane/Airtech/badge.svg?branch=feature-flight-operations)](https://coveralls.io/github/klevamane/Airtech?branch=feature-flight-operations)
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d168ecfa3b922b36265e)
# Airtech
This project automates the flight booking system

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
To install this project you need the following framework and tools
```
- Python3
- Postgres
- Memcached
```

### Installing
These Steps would help you install the project dependent packages and run the application. 
The project has two sections FrontEnd and BackEnd, the instructions here is structure to setup both section interdependently.

#### Primary steps
* Clone the repository and CD into the repository directory
* Ensure that you have created a database for this project
* Create a .env file
* Update the new .env file with required data

#### How to Start the backend
* create and activate a virtual environment. Here is an example using Pipenv: run `pipenv install`
* Start shell `pipenv shell`
* Run migration `python manage.py migrate`
* Start the app via Django `python manage.py runserver`
* create a database in postgres and make the connection via the environment variable

#### To run locally
* Start the app via Django `python manage.py runserver`
* Open a HTTP client (e.g. Postman)...:
    * Make a `POST` request to the endpoint `v1/api/login` with Headers:
    ```json
    Authorization: {jwt-token}
    ```
* Get and use the token value in the response object for all subsequent requests. Under the Authorization menu,
    * TYPE is `Bearer Token`
    * Token is {token value}


#### To run tests locally
* `pytest`


### Built with
1. Django
2. Djangorestframework
3. Postgres

### Contributors
* Onengiye Richard (klevamane)

### Author
* Onengiye Richard (klevamane)
