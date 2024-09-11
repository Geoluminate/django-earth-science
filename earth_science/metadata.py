from django.utils.translation import gettext as _
from geoluminate.metadata import Authority

default_metadata = {
    "authority": Authority(
        name=_("Geoluminate Earth Science"),
        website="https://ihfc-iugg.org",
    ),
    "keywords": [],
    "repo_url": "https://github.com/Geoluminate/geoluminate-earth-science",
}
