# from django.db import models
# from django.utils.translation import gettext as _

# from geoluminate.contrib.gis.base import AbstractSite


# class Site(models.Model):
#     """An abstract base class for geoscience databases that contains spatial fields relevant to the geosciences. E.g. Geological province, tectonic plate, etc.
#     """

#     plate = models.ForeignKey(
#         "plates.Plate",
#         verbose_name=_("Tectonic Plate"),
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#     )

#     province = models.ForeignKey(
#         "provinces.Province",
#         verbose_name=_("Geologic Province"),
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#     )

#     class Meta:
#         abstract = True
