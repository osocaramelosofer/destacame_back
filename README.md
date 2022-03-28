## Installation

Clone the project.

```sh
$ git clone https://github.com/osocaramelosofer/destacame_back.git
```

Create a python virtual enviroment.
To achieve this there are many ways to create a virtual enviroment, if you have a favorite one feel free to use it.
In this case we are gonna use [pyenv](https://docs.python.org/es/3/tutorial/venv.html).

Install pyenv Linux.

```sh
$ sudo apt install python3.8-venv
```

Crate a virtual enviroment & activate it. (I suggest you create a new directory named virtual_envs).
```sh
$ python3 -m venv destacame_back
$ source destacame_back/bin/activate
```

Now in the same terminal where we activate our virtual env, we are gonna install the project's dependencies.
```sh
$ python -m pip install django~=3.1.0
$ python -m pip install djangorestframework
$ python -m pip install django-cors-headers
```

Once've installed everything we need to navigate where we cloned the repository (in the same terminal) and run the server.
```sh
$ cd destacame_back
$ python manage.py runserver
```
(We need to be in the same level directory than ou manage.py)
