"""Here you can define the common settings for the project. These are imported by the development and production settings files. Use this file to do things like adding extra apps, geoluminate plugins, middleware, etc. to your project."""

from pathlib import Path

import geoluminate

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    "earth_science",
    "example",
]

GEOLUMINATE = {
    "application": {
        "domain": "www.heatflow.world",
        "developers": [
            {
                "email": "jennings@gfz-potsdam.de",
                "name": "Sam Jennings",
            },
        ],
    },
    "database": {
        "name": "Geoluminate - Earth Science",
        "short_name": "GeoES",
        "keywords": ["heat flow", "geothermal", "geoenergy"],
    },
    "governance": {
        "name": "International Heat Flow Commission",
        "short_name": "IHFC",
        "url": "https://www.ihfc-iugg.org",
    },
}


SHOW_DEBUG_TOOLBAR = False
DEBUG = True
geoluminate.setup(development=True)


# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# removing validators for local development
AUTH_PASSWORD_VALIDATORS = []

# Verifying emails in development is annoying
# For testing, uncomment the following line
ACCOUNT_EMAIL_VERIFICATION = "optional"


AWS_USE_SSL = False

ALLOWED_HOSTS = ["*"]


EARTH_SAMPLES = [
    # "DepthInterval",
    "DrillCore",
    "RockSample",
    "ThinSection",
]
