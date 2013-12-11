from django.core.urlresolvers import reverse

from social_auth.exceptions import AuthAlreadyAssociated
from social_auth.middleware import SocialAuthExceptionMiddleware


class ExampleSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def raise_exception(self, request, exception):
        return False

    def get_message(self, request, exception):
        if isinstance(exception, AuthAlreadyAssociated):
            return 'Somebody is already using that account!'
        return 'Ni modo'

    def get_redirect_uri(self, request, exception):
        if request.user.is_authenticated():
            return reverse('main')
        else:
            return reverse('main')