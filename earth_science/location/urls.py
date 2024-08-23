from django.urls import include, path

from .plugins import location

urlpatterns = [
    *PointEditView.get_urls(),
    path("l/<lon>/<lat>/", include(location.urls)),
]
