from django.urls import include, path

from .plugins import plugins
from .views import PointCRUDView

urlpatterns = [
    # *PointEditView.get_urls()
    *PointCRUDView.get_urls(),
    path("loc/<str:pk>/", include(plugins.get_urls("location"))),
]
