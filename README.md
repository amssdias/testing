[python-download]: https://www.python.org/downloads/
[django-link]: https://www.djangoproject.com/

![Python Badge](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Python Badge](https://img.shields.io/badge/Django-3.2.12-092E20?logo=django)
![Workflow branch master](https://github.com/amssdias/calorie_counter/actions/workflows/testing.yml/badge.svg?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


<h1 align=center>Calorie Counter</h1>


The calorie counter app is a great way to keep track of all the calories you are burning every day. The user can add all the food they are eating and the app will count the calories. We can further add a function for users to add their daily workout sessions, running and jogging to calculate how much calories they have burned.

This project was made before by me, but I decided to do a better version of it, with clean code and better functionality. You can check it here: [HealthGain](https://github.com/amssdias/healthgain).


### Built with

![Django Badge](https://img.shields.io/badge/-Django-092E20?style=for-the-badge&labelColor=black&logo=django&logoColor=white)


## :hammer: Getting started

### Pre requisites

- [Python][python-download] - 3.9 or up
- [Django][django-link] - 3.2.12


### Installation

#### Clone the project

```
git clone https://github.com/amssdias/calorie_counter
cd calorie_counter
```

#### Configure settings (email)

Fill up the "_**.env.example**_" file, so users can receive activation links and to reset passwords. Rename it as well to ".env".


#### Install dependencies & activate virtualenv

1. Pipenv ***(make sure you have [Python][python-download] installed)***:

	```python
     pip install pipenv  # For Windows
     brew install pipenv # For MacOs
     sudo apt install pipenv # For Debian Buster+
     sudo dnf install pipenv # For Fedora

    ```
    
2. Install packages:

	```python
    pipenv install # will create a virtual environment with all the modules needed
    ```

3. Activate virtualenv and apply migrations:

	```python
    pipenv shell # To activate the virtual environment

    python manage.py makemigrations
    python manage.py migrate
    ```

If any doubts here's a link to some more explanations: [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)



## :mag_right: Usage

### On one terminal window:
```python
pipenv shell
python manage.py runserver
```

Paste this link on your browser:
**http://127.0.0.1:8000/accounts/login**

### If we want to use celery to run tasks asynchronously:

On a new terminal window run:
```python
pipenv shell
celery -A calourie_counter.celery worker -l info
celery -A calorie_counter.celery worker --pool=solo -l info # For windows
```


## Features

- Create an account
  - Send email to activate account
- Log in
	- Via email and password
	- Resend activation link
	- Reset password
