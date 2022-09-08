from treewidget.fields import TreeOneToOneField, TreeForeignKey, TreeManyToManyField
from earth_science.models import EarthMaterial
from django.conf import settings
from earth_science.utils import filter_tree

def material_type_limiter():
    """Controls what objects are passed to the jstree widget.
    
    The app will look for node names specified in either EARTH_MATERIALS_INCLUDE or EARTH_MATERIALS_EXCLUDE in the settings.py file and exclude or filter result based on which ever has been declared. If both variables contain items, only EARTH_MATERIALS_INCLUDE is used and the queryset is filtered.    
    """
    include = getattr(settings,'EARTH_MATERIALS_INCLUDE', [])
    exclude = getattr(settings,'EARTH_MATERIALS_EXCLUDE', [])

    values = include if include else exclude

    if values:
        return filter_tree(EarthMaterial.objects.filter(name__in=values), exclude = not include)
    return {}

class EarthMaterialMixin():

    def __init__(self, *args, **kwargs):
        kwargs['to'] = "earth_science.EarthMaterial"
        kwargs['limit_choices_to'] = material_type_limiter
        super().__init__(*args, **kwargs)

class EarthMaterialFK(EarthMaterialMixin,TreeForeignKey):
    pass

class EarthMaterialOneToOne(EarthMaterialMixin,TreeOneToOneField):
    pass

class EarthMaterialM2M(EarthMaterialMixin,TreeManyToManyField):
    pass

class GeologicTimeMixin():

    def __init__(self, *args, **kwargs):
        kwargs['to'] = "geologic_time.GeologicTime"
        # kwargs['limit_choices_to'] = limit_choices_to
        super().__init__(*args, **kwargs)


class GeologicTimeFK(GeologicTimeMixin,TreeForeignKey):
    pass

class GeologicTimeOneToOne(GeologicTimeMixin,TreeOneToOneField):
    pass

class GeologicTimeM2M(GeologicTimeMixin,TreeManyToManyField):
    pass