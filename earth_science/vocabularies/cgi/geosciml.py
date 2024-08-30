"""Collection of vocabularies from the CGI GeoSciML RemoteVocabulary.

<https://cgi.vocabs.ga.gov.au/vocab/>

note::

It's currently not possible to download full vocabularies direct from the CGI website or from Research Vocabs Australia.
Therefore, the vocabularies are linked direct to the .ttl representations stored in the official CGI-IUGS GitHub repository.

https://github.com/CGI-IUGS/cgi-vocabs

"""

from research_vocabs.vocabularies import RemoteVocabulary


class AlterationType(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/alterationtype.ttl"


class BoreholeDrillingMethod(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/boreholedrillingmethod.ttl"


class CompositionCategory(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/compositioncategory.ttl"


class CompoundMaterialConstituentPart(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/compoundmaterialconstituentpartrole.ttl"


class ConsolidationDegree(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/consolidationdegree.ttl"


class ContactType(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/contacttype.ttl"


class ConventionCodeForStrikeAndDipMeasurements(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/conventioncode.ttl"


class DeformationStyle(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/deformationstyle.ttl"


class DescriptionPurpose(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/descriptionpurpose.ttl"


class DeterminationMethodOrientation(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/determinationmethodorientation.ttl"


class EventEnvironment(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/eventenvironment.ttl"


class EventProcess(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/eventprocess.ttl"


class FaultMovementSense(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/faultmovementsense.ttl"


class FaultMovementType(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/faultmovementtype.ttl"


class FaultType(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/faulttype.ttl"


class FoliationType(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/foliationtype.ttl"


class GeneticCategory(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/geneticcategory.ttl"


class GeologicUnitMorphology(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/geologicunitmorphology.ttl"


class GeologicUnitPartRole(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/geologicunitpartrole.ttl"


class GeologicUnitType(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/geologicunittype.ttl"


class LineationType(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/lineationtype.ttl"


class MappingFrame(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/mappedfeatureobservationmethod.ttl"


class MetamorphicFacies(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/metamorphicfacies.ttl"


class MetamorphicGrade(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/metamorphicgrade.ttl"


class ObservationMethodGeologicFeature(RemoteVocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifierscheme/cgi/2016.01/featureobservationmethod"


class ObservationMethodMappedFeature(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/mappedfeatureobservationmethod.ttl"


class OrientationDeterminationMethod(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/determinationmethodorientation.ttl"


class ParticleAspectRatio(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/particleaspectratio.ttl"


class ParticleShape(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/particleshape.ttl"


class ParticleType(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/particletype.ttl"


class PlanarPolarityCode(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/planarpolaritycode.ttl"


class ProportionTerm(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/proportionterm.ttl"


class SimpleLithology(RemoteVocabulary):
    # This vocabulary is available from the Aus Research Vocabs website, however, we are using the CGI-IUGS GitHub repository
    # for consistency with the other vocabs. (and assuming the repository is the most up-to-date source for the vocabularies?)

    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/simplelithology.ttl"
        # source = "https://vocabs.ardc.edu.au/registry/api/resource/downloads/214/ga_simple-lithology_v0-1.ttl"


class StratigraphicRank(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/stratigraphicrank.ttl"


class ValueQualifier(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/valuequalifier.ttl"


class RemoteVocabularyRelation(RemoteVocabulary):
    class Meta:
        source = "https://github.com/CGI-IUGS/cgi-vocabs/blob/master/vocabularies/geosciml/vocabularyrelation.ttl"
