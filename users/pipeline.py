from django.core.exceptions import ObjectDoesNotExist
from .models import Socials
import urllib.request


def update_user_social_data(strategy, *args, **kwargs):
    """Set the name and avatar for a user only if is new.
    """
    print('update_user_social_data ::', strategy)
    # print(args)
    response = kwargs['response']
    full_name = ''
    backend = kwargs['backend']
    user = kwargs['user']
    # for k in response:
    #     print(k, ":", kwargs['response'][k])
    #

    if response and response['picture']:
        url = response['picture']
        try:
            social = user.socials
        except ObjectDoesNotExist:
            social = Socials(user=user)

        if social.avatar != url:
            social.avatar = url
            # ext = url.split('/')[-1].split('.')[-1]
            # filename = ('{}.{}'.format(user.id, ext))
            # urllib.request.urlretrieve(url, 'user_file/avatar/' + filename)
        social.save()
    else:
        print('not found')
