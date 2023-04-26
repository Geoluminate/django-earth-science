from django.db import models
from django.utils.translation import gettext as _
from treebeard.mp_tree import MP_Node


class EarthMaterial(MP_Node):
    label = models.CharField(_("Label"), help_text=_("Short label of the earth material"), max_length=255)
    name = models.CharField(_("Name"), help_text=_("Name of the earth material"), max_length=255)
    description = models.TextField(
        _("Description"),
        help_text=_("Description of the material"),
        max_length=255,
        blank=True,
        null=True,
    )
    code = models.CharField(_("Code"), help_text=_("Identifier code"), max_length=16, blank=True, null=True)
    url = models.URLField(
        _("About"),
        help_text=_("URL to the page describing the field on the BGS website"),
    )

    node_order_by = ["name"]

    class Meta:
        verbose_name = _("BGS Earth Material")
        verbose_name_plural = _("BGS Earth Materials")

    def __str__(self):
        # return self.verbose_path()
        # return f'{self.name} ({self.get_parent().name})'
        return f"{self.name}"

    def verbose_path(self):
        parent = self.get_parent()
        if parent:
            return f"{self.get_parent()} > {self.name}"
        else:
            return f"{self.name}"

    @staticmethod
    def autocomplete_search_fields():
        # For Django Grappelli related lookups
        return (
            "name__icontains",
            "code__icontains",
        )


class GeologicTime(MP_Node):
    rank = models.CharField(_("Rank"), max_length=16)

    label = models.CharField(_("Label"), help_text=_("Label"), max_length=255)

    notation = models.CharField(
        _("Notation"),
        help_text=_("Identifier code"),
        max_length=16,
        blank=True,
        null=True,
    )
    status = models.CharField(_("Status"), max_length=16, blank=True, null=True)
    about = models.URLField(
        _("About"),
        help_text=_("URL to the page describing the field on the BGS website"),
        null=True,
        blank=True,
    )

    older_bound = models.FloatField(_("Older bound"))
    younger_bound = models.FloatField(_("Younger bound"))

    node_order_by = ["younger_bound"]

    class Meta:
        verbose_name = _("Geologic Time")
        verbose_name_plural = _("Geologic Times")
        # db_table = 'geologic_time'

    def __str__(self):
        return f"{self.label} {self.rank}"

    def verbose_path(self):
        parent = self.get_parent()
        if parent:
            return f"{self.get_parent()} > {self.name}"
        else:
            return f"{self.name}"

    @staticmethod
    def autocomplete_search_fields():
        # For Django Grappelli related lookups
        return ("label__icontains",)

    @property
    def _rank(self):
        ranks = {
            1: "Super-Eon",
            2: "Eon",
            3: "Era",
            4: "Period",
            5: "Epoch",
            6: "Age",
        }
        return ranks[self.depth]
