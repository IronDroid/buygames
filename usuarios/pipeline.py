from django.core.files import File
from .models import Usuario

def get_user_avatar(backend, details, response, social_user, uid, user, *args, **kwargs):
    url = None

    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
 
    elif backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal', '')

    if url:
    	if backend.name == 'twitter':
    		Usuario.objects.get_or_create(uid=user.username, username=details['fullname'], avatar=url, backend=backend.name)
    	else:
    		Usuario.objects.get_or_create(uid=user.username, username=details['fullname'], email=details['email'], avatar=url, backend=backend.name)
