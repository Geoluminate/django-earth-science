# Django Geologic Time

Django Geologic Time integrates the [Geologic Timescale (2020)](https://vocabs.ardc.edu.au/viewById/196) into your Django app. The primary goal of this app is to help standardise input of geological information into Earth Science databases. 

[![Visualise](https://geoluminate.github.io/django-earth-materials/images/visualise.png)](https://geoluminate.github.io/django-earth-materials/visualise.html)

**click the image above to view an interactive version of this resource.*

## Licensing

This application and it's code base are licensed under the permissive [MIT License](license).

The included data was published by the International Commission on Stratigraphy and the CGI Geoscience Terminology Working Group under the [CC BY 3.0 AU](https://creativecommons.org/licenses/by/3.0/au/). It was obtained in July of 2022 from [Research Vocabularies Australia](https://vocabs.ardc.edu.au/viewById/196).

## Installation

First install the application with pip using

    pip install django_earth_science

then add `earth_science` to your installed apps like so

    INSTALLED_APPS = [
        ...
        earth_science,
        ...
    ]

Finally, add the earth_science urls to your project urls

    urlpatterns = [
        ...
        path('earth_science', include('earth_science.urls')),
        ...
    ]

> **_NOTE:_**  Don't forget to run `python manage.py migrate earth_science` to migrate the schema and load the included data fixtures!


## Usage

Django Earth Materials provides an `GeologicTimeFK`, `GeologicTimeM2M` and `GeologicTimeOneToOne` field to help you integrate the app into your project as follows:

    from earth_science.fields import GeologicTimeFK, GeologicTimeM2M, GeologicTimeOneToOne

    class SomeModel(models.Model):
        lithology = GeologicTimeOneToOne()

Each field automatically points to the GeologicTime model and also sub-classes fields provided by `django-treewidget` in order to utilize the `jstree` javascript widget in forms. When viewing this model in the Django Admin site, you will now be presented with a field like this,

![Visualise](https://geoluminate.github.io/django-earth-materials/images/admin_widget.PNG)

where admin can select one or more items depending on the type of field used. 

> **_NOTE:_**  The above image is taken from an admin site that utilizes the [Djang Grappelli](https://grappelliproject.com) admin interface. If you don't use Grappelli then your field may look slightly different.


## Settings

Django Geologic Time includes two settings, `GEOLOGIC_TIME_INCLUDE` and `GEOLOGIC_TIME_EXCLUDE`, that can be declared in your `settings.py` file to control what tree nodes are available in the form widget. These are useful if your project is dedicated to a specific rock group. For example, 

    GEOLOGIC_TIME_INCLUDE = [
        'Igneous rock and sediment',
        'Metamorphic rock',
        ]

will restrict the widget to only igneous and metamorphic rock types. Alternatively,

    GEOLOGIC_TIME_EXCLUDE = [
        'Superficial deposit (natural and/or artificial)'
        ]
        
will exclude artificial materials from the widget.

> **_NOTE:_** If both `GEOLOGIC_TIME_INCLUDE` and `GEOLOGIC_TIME_EXCLUDE` are found in `settings.py`, only `GEOLOGIC_TIME_INCLUDE` will be used.

## Customisation

The widget can be customised either by supplying the `settings` and `treeoptions` arguments to the model field or by providing customisation options project wide in `settings.py` as `TREEWIDGET_SETTINGS` and `TREEWIDGET_TREEOPTIONS`. See the readme at [`django-treewidget`](https://github.com/netzkolchose/django-treewidget) for further instructions on customisation.

The following settings are recommended here but not required:

> **_NOTE:_**  To use, place these in your `settings.py` file.

    TREEWIDGET_SETTINGS = {
                'search':True, # adds a search bar to the widget that filters tree nodes
                }
                
    TREEWIDGET_TREEOPTIONS = {
        "core" : {
            "themes" : {
                "icons": False, # removes the folder icon next to each item
            },
        },
        "plugins" : [ "checkbox" ] # adds checkboxes next to each item
    }

### Unofficial names

Unofficial age names are were sourced from this [wikipedia list](https://en.wikipedia.org/wiki/List_of_geochronologic_names) on the 18th of August 2022. Many items were excluded that don't fit the purpose of this app. They include the following ranks ("status"):

* ALMA, ELMMZ and NALMA
* chron
* chronozone
* Martian epoch
* ice age

An additional 73 unofficial names were excluded for having no reported age bounds.

Lunar categories are also excluded. 

## Acknowledgments

This software is provided open-source thanks to:

[![GeoForschungsZentrum logo](https://geoluminate.github.io/images/gfz_logo.png)](https://www.gfz-potsdam.de)

[![GeoLuminate logo](https://geoluminate.github.io/images/standard_w1000.png)](https://www.geoluminate.com.au)