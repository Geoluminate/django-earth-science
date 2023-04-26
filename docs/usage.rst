=====
Usage
=====

To use Geoluminate Earth Science in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'geoscience.apps.GeoscienceConfig',
        ...
    )

Add Geoluminate Earth Science's URL patterns:

.. code-block:: python

    from geoscience import urls as geoscience_urls


    urlpatterns = [
        ...
        url(r'^', include(geoscience_urls)),
        ...
    ]
