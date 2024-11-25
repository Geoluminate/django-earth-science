from django.utils.translation import gettext as _
from geoluminate.metadata import Metadata
from research_vocabs.fields import ConceptField

from earth_science.geology.generic_models import GenericRock
from earth_science.metadata import default_metadata
from earth_science.models.samples.generic import GenericEarthSample
from earth_science.vocabularies.cgi import geosciml


class CompoundMaterial(GenericEarthSample):
    _defaults = {}

    # I guess this probably needs to be a relationship to a new model
    constituent_parts = ConceptField(
        concept_class=geosciml.CompoundMaterialConstituentPart,
        blank=True,
        null=True,
    )

    consolidation_degree = ConceptField(
        concept_class=geosciml.ConsolidationDegree,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Compound Material")
        verbose_name_plural = _("Compound Materials")


class GenericRock(GenericRock):
    _defaults = {}

    alteration_type = ConceptField(
        concept_class=geosciml.AlterationType,
        blank=True,
        null=True,
    )

    composition_category = ConceptField(
        concept_class=geosciml.CompositionCategory,
        blank=True,
        null=True,
    )

    lineation = ConceptField(
        concept_class=geosciml.Lineation,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Generic Rock")
        verbose_name_plural = _("Generic Rocks")

    def save(self, *args, **kwargs):
        # assign any default values that are not already set
        for field, value in self._defaults.items():
            if not getattr(self, field):
                setattr(self, field, value)
        super().save(*args, **kwargs)


class IgneousRock(GenericRock):
    _defaults = {
        "alteration_type": "not altered",
        "consolidation_degree": "unconsolidated",
    }

    class Meta:
        verbose_name = _("Igneous Rock")
        verbose_name_plural = _("Igneous Rocks")
        proxy = True

    class Config:
        metadata = Metadata(
            **default_metadata,
            description=_(
                "Igenous rock is a type of rock formed through the crystallization and solidification of molten silicate material, known as magma or lava, originating from the partial melting of the Earth's mantle or crust. These rocks are classified into intrusive (plutonic) or extrusive (volcanic) types, depending on whether the molten material cools and solidifies beneath the Earth's surface or after erupting onto the surface, respectively. Igneous rocks are primarily composed of silicate minerals, such as feldspar, quartz, olivine, and pyroxene, and are characterized by their texture, mineralogy, and chemical composition, which reflect the conditions under which they formed."
            ),
            keywords=["igneous", "rock", "magma", "solidification"],
        )
        form_class = "earth_science.geology.rock_samples.forms.IgneousRockForm"
        filter_class = "earth_science.geology.rock_samples.filters.IgneousRockFilter"
        importer_class = "earth_science.geology.rock_samples.importers.IgneousRockImporter"


class MetamorphicRock(GenericRock):
    _defaults = {
        "consolidation_degree": "consolidated",
    }

    class Meta:
        verbose_name = _("Metamorphic Rock")
        verbose_name_plural = _("Metamorphic Rocks")
        proxy = True

    class Config:
        metadata = Metadata(
            **default_metadata,
            description=_(
                "Metamorphic rock is a type of rock that forms from the alteration of pre-existing rocks (igneous, sedimentary, or other metamorphic rocks) through exposure to high temperatures, pressures, and chemically active fluids, without the rock melting into liquid magma. This process, known as metamorphism, leads to changes in the mineral composition, texture, and structure of the rock, producing new minerals and foliated or non-foliated textures depending on the conditions of temperature, pressure, and deformation. Metamorphic rocks, such as schist, gneiss, and marble, provide insight into the geological processes that occur deep within the Earth and the history of tectonic movements."
            ),
            keywords=["metamorphic", "rock", "transformation", "mineralogy"],
        )
        form_class = "earth_science.geology.rock_samples.forms.IgneousRockForm"
        filter_class = "earth_science.geology.rock_samples.filters.IgneousRockFilter"
        importer_class = "earth_science.geology.rock_samples.importers.IgneousRockImporter"


class SedimentaryRock(GenericRock):
    _defaults = {
        "consolidation_degree": "consolidated",
    }

    class Meta:
        verbose_name = _("Sedimentary Rock")
        verbose_name_plural = _("Sedimentary Rocks")
        proxy = True

    class Config:
        metadata = Metadata(
            **default_metadata,
            description=_(
                "Sedimentary rock is a type of rock formed by the accumulation, compaction, and cementation of mineral and organic particles, or by the precipitation of minerals from solution at or near the Earth's surface. These rocks originate from the weathering and erosion of pre-existing rocks, whose fragments are transported by water, wind, ice, or gravity, and deposited in layers in various environments, such as rivers, lakes, deserts, and oceans. Over time, these layers are compacted and cemented together by minerals precipitated from groundwater, forming sedimentary rocks like sandstone, shale, and limestone. Sedimentary rocks are characterized by their stratified layers and often contain fossils, making them key records of the Earth's surface conditions and life forms over geological time."
            ),
            keywords=["sedimentry", "rock", "transformation", "mineralogy"],
        )
        form_class = "earth_science.geology.rock_samples.forms.IgneousRockForm"
        filter_class = "earth_science.geology.rock_samples.filters.IgneousRockFilter"
        importer_class = "earth_science.geology.rock_samples.importers.IgneousRockImporter"
