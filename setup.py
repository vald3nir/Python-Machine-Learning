# coding=utf-8
# !/usr/bin/python3

from subprocess import call

libraries = [
    "setuptools", "wheel",
    "gunicorn",
    "Flask", "Flask-Cors", "jwt",
    "pymongo[srv]",
]

call("pip install " + ' '.join(libraries), shell=True)
call("pip freeze > requirements.txt", shell=True)
