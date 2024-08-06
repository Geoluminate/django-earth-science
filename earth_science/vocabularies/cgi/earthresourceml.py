"""Collection of vocabularies from the CGI EarthResourceML vocabulary. <https://cgi.vocabs.ga.gov.au/vocab/>"""

from research_vocabs import Vocabulary


class CommodityCode(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/commodity-code"


class EarthResourceExpression(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/earth-resource-expression"


class EarthResourceForm(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/earth-resource-form"


class EarthResourceMaterialRole(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/earth-resource-material-role"


class EarthResourceShape(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/earth-resource-shape"


class EndUsePotential(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/end-use-potential"


class EnvironmentalImpact(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/environmental-impact"


class ExplorationActivityType(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/exploration-activity-type"


class ExplorationResult(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/exploration-result"


class MineStatus(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/mine-status"


class MineralOccurrenceType(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/mineral-occurrence-type"


class MineralResourceReportingClassificationMethod(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/mineral-resource-reporting-classification-method"


class MiningActivity(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/mining-activity"


class ProcessingActivity(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/processing-activity"


class RawMaterialRole(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/raw-material-role"


class ReserveAssessmentCategory(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/reserve-assessment-category"


class ResourceAssessmentCategory(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/resource-assessment-category"


class UNFCCode(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/unfc-code"


class WasteStorage(Vocabulary):
    class Meta:
        source = "http://resource.geosciml.org/classifier/cgi/waste-storage"
