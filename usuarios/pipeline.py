from django.core.files import File
from .models import Usuario
import urllib2

def get_user_avatar(backend, details, response, social_user, uid, user, *args, **kwargs):
    url = None

    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
 
    elif backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal', '')

    if url:
        usuario = Usuario()
        usuario.uid = user.username
        usuario.username = details['first_name'] +" "+ details['last_name']
        usuario.email = details['email']
        usuario.avatar = url
        usuario.backend = backend.name

        try:
            if not Usuario.objects.get(username = usuario.username) != None:
                usuario.save()
        except Exception, e:
            usuario.save()