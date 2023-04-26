from django.urls import include, path

urlpatterns = [
    path("treewidget/", include("treewidget.urls")),
]
