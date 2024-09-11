"""Here you can define the common settings for the project. These are imported by the development and production settings files. Use this file to do things like adding extra apps, geoluminate plugins, middleware, etc. to your project."""

import geoluminate

geoluminate.setup(
    apps=[
        "earth_science",
        "earth_science.location",
        "earth_science.geology.geologic_time",
        "earth_science.geology.lithology",
        "example",
    ],
)
