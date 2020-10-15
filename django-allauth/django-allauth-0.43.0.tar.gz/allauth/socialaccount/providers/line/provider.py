from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class LineAccount(ProviderAccount):
    def get_avatar_url(self):
        return self.account.extra_data.get("pictureUrl")

    def to_str(self):
        return self.account.extra_data.get("displayName", self.account.uid)


class LineProvider(OAuth2Provider):
    id = "line"
    name = "Line"
    account_class = LineAccount

    def get_default_scope(self):
        return []

    def extract_uid(self, data):
        return str(data["userId"])

    def extract_common_fields(self, data):
        return dict(
            email=data.get("email"),
            username=data.get("displayName"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            name=data.get("name"),
        )


provider_classes = [LineProvider]
