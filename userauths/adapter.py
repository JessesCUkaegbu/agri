from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.helpers import complete_social_login

class MyGoogleOAuth2Adapter(GoogleOAuth2Adapter):
    def complete_login(self, request, app, token, **kwargs):
        response = kwargs.get("response") or token.get("response")
        login = self.get_provider().sociallogin_from_response(request, response)
        return complete_social_login(request, login)

    def get_callback_url(self, request, app):
        callback_url = super(MyGoogleOAuth2Adapter, self).get_callback_url(request, app)
        callback_url += '&prompt=select_account'
        return callback_url
