# flask-psycopg2-starter

A starter kit including Flask and Psycopg2 without SQLAlchemy

## Requirements

- `Python>=3.7.3` [General](https://www.python.org/downloads/release/python-373/)
- `PostgreSQL>=11.2` [General](https://www.postgresql.org/download/) [macOS](https://postgresapp.com/)

## Installation

```bash
# flask-psycopg2-starter/
$ make install
[...]
```

## Routes

```bash
# flask-psycopg2-starter/
$ flask routes
Endpoint       Methods    Rule
-------------  ---------  -----------------------
auth.login     GET, POST  /auth/login
auth.logout    GET        /auth/logout
auth.register  GET, POST  /auth/register
index          GET        /
static         GET        /static/<path:filename>
```

## Production

If you are starting with this boilerplate to build an application for prod deployment, there is a `serve.py` that wraps the Flask application with a basic logger.

## Issues

If you run into permission issues like below,

```bash
# flask-psycopg2-starter/
$ make install
virtualenv venv
make: ./make-venv: Permission denied
make: *** [install] Error 1
$ chmod +x make-venv # should fix the issue
```

If you run into issues installing `psycopg2` on macOS, refer to [this StackOverflow post](https://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa). Personally, I had to set following flags such that compiler can find `openssl`:

``` bash
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
```
