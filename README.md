# Platzigram
A little Instagram made in Django Framework for Platzi courses.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:matiasrolon/Platzigram.git
$ cd Platzigram
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv your_venv
$ source name_virtual_env/bin/activate
```

Then install the dependencies:

```sh
(your_venv)$ pip install -r requirements.txt
```
Note the `(your_venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
