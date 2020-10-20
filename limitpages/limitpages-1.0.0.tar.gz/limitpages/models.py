from django.core.exceptions import ValidationError
from django.conf import settings

from papermerge.core.models import AbstractDocument


class Document(AbstractDocument):
    """
    Limit number of pages to settings.LIMITPAGES_MAX_PAGES.
    If settings is omitted - use 15 as default.
    """

    def clean(self):

        max_pages = 15

        if hasattr(settings, 'LIMITPAGES_MAX_PAGES'):
            max_pages = settings.LIMITPAGES_MAX_PAGES

        if self.get_page_count() > max_pages:
            error_msg = f"In Demo mode max {max_pages} pages allowed"
            raise ValidationError({
                'page_count': error_msg
            })
