# Eventex

App created for handling events.

[![Build Status](https://travis-ci.org/arthurguerra/eventex.svg?branch=master)](https://travis-ci.org/arthurguerra/eventex)
[![Code Health](https://landscape.io/github/arthurguerra/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/arthurguerra/eventex/master)

## Developer

1. Clone github repository
2. Create a Python 3.5, virtualenv environment
3. Activate virtualenv
4. Install dependencies
5. Configure your dev instance with the *.env* file
6. Run tests (*python manage.py tests*)

```console
git clone git@github.com:arthuguerra/eventex.git wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/envsample .env
python manage.py test
```

## How to deploy?

1. Create a Heroku app instance
2. Send configuration to Heroku
3. Get a SECRET_KEY from the Heroku app instance
4. Set DEBUG=False
5. Configure email settings (smtp)
6. Push code to Heroku

```console
heroku create my-instance
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure email (smpt)
git push heroku master --force
```