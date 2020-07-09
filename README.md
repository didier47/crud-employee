# crud-employee

Backend example made with Django Rest Framework and Cassandra including filters and ordering fields.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

If you want to try, you will need these prerequisites

```
Python > 3.6
```

### Installing

First, clone the project on your computer

```
git clone https://github.com/didier47/crud-employee.git
```

then, create a virtual environment for the project, you can use virtualenvwrapper-win if your os is windows

```
pip install virtualenvwrapper-win
mkvirtualenv <name_you_desire>
```

after that, install the packages in requirements.txt to make sure you have everything needed (you will need .env)

```
pip install -r requirements.txt
```

finally, set up aassandra, you can easily do this using laragon if your os is windows, then, synchronize db with

```
py manage.py syncdb
```

now you can run it

```
py manage.py runserver
```

Navigate to localhost:8000/swagger/ and explore this basic crud

## Authors

* **Didier Gaona**

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details
