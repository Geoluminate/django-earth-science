import os

from django.db.models import F, Q
from django.db.models.functions import Substr

from geoscience.models import EarthMaterial

ParentPath = Substr("path", 1, (F("depth") - 1) * EarthMaterial.steplen)
RootPath = Substr("path", 1, EarthMaterial.steplen)


def filter_tree(queryset=None, exclude=False):
    """builds a query to either filter or exclude nodes in the tree"""

    # start by getting the descendants
    query = Q(id__in=include_descendants(queryset))

    if exclude:
        # if we are excluding, return the negated Q object
        return ~query
    else:
        # if we are filtering, we need to first add the ancestors otherwise the
        # tree won't build correctly
        return query | Q(id__in=include_ancestors(queryset))


def include_descendants(queryset=None):
    for node in queryset:
        queryset |= node.get_descendants()
    return queryset


def include_ancestors(queryset=None):
    for node in queryset:
        queryset |= node.get_ancestors()
    return queryset.values_list("id")


dir_path = os.path.dirname(os.path.realpath(__file__))

database = os.path.join(dir_path, "data/data.csv")
