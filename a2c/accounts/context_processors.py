from django.core.urlresolvers import reverse

from accounts.models import Contact


def contact_status(request):
    """
    Check if user has a valid contact object. If yes, show app upload form, otherwise, hide it.contact_status
    
    """

    if request.user.is_authenticated():
        try:
            return {
                'has_contact': Contact.objects.filter(user=request.user),
                
            }
        except DoesNotExist:
            pass
    return {
        
        }
