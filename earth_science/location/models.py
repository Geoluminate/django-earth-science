from django.contrib import admin
from django.utils.translation import gettext as _
from geoluminate.db import models

from earth_science.conf import settings

X_OPTS = settings.EARTH_SCIENCE_X_COORD
Y_OPTS = settings.EARTH_SCIENCE_Y_COORD


# 6 decimal places is accurate to within ~0.11 meters
X_MAX_DIGITS = X_OPTS.get("max_digits") or X_OPTS["decimal_places"] + 3

Y_MAX_DIGITS = Y_OPTS.get("max_digits") or Y_OPTS["decimal_places"] + 2


class Point(models.Model):
    x = models.DecimalField(
        verbose_name=_("x"),
        help_text=_("The x-coordinate of the location."),
        max_digits=X_MAX_DIGITS,
        decimal_places=X_OPTS["decimal_places"],
    )
    y = models.DecimalField(
        verbose_name=_("y"),
        help_text=_("The y-coordinate of the location."),
        max_digits=Y_MAX_DIGITS,
        decimal_places=Y_OPTS["decimal_places"],
    )
    crs = models.CharField(
        verbose_name=_("CRS"),
        help_text=_("The coordinate reference system."),
        max_length=255,
        default=settings.EARTH_SCIENCE_CRS,
        editable=False,
    )

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        """Returns the string representation of this site"""
        return f"{self.latitude}, {self.longitude}"

    def point2d(self):
        return {"type": "Point", "coordinates": [self.x, self.y]}

    @property
    @admin.display(description=_("latitude"))
    def latitude(self):
        """Convenience method for retrieving the site's latitude ordinate."""
        return self.y

    @latitude.setter
    def latitude(self, val):
        self.y = val

    @property
    @admin.display(description=_("longitude"))
    def longitude(self):
        """Convenience method for retrieving the site's longitude ordinate."""
        return self.x

    @longitude.setter
    def longitude(self, val):
        self.x = val

    def get_absolute_url(self):
        """Returns the absolute URL for this site"""
        return "/"
        # return reverse(
        #     "location-detail", kwargs={"lon": self.longitude, "lat": self.latitude}
        # )
