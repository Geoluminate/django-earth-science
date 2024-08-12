from research_vocabs.vocabularies import RemoteVocabulary


class ISC2020(RemoteVocabulary):
    class Meta:
        source = "https://vocabs.ardc.edu.au/registry/api/resource/downloads/1211/isc2020.ttl"
        prefix = "isc"
        namespace = "http://resource.geosciml.org/classifier/ics/ischart/"
