from django.utils.translation import gettext as _
from geoluminate.metadata import Authority, Citation

default_metadata = {
    "authority": Authority(
        name=_("Geoluminate Earth Science"),
        website="https://github.com/Geoluminate/geoluminate-earth-science",
    ),
    "citation": Citation(text="Geoluminate Earth Science", doi=""),
    "keywords": [
        "earth_science",
    ],
    "repo_url": "https://github.com/Geoluminate/geoluminate-earth-science",
}
