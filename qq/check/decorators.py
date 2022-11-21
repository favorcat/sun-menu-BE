
from django.http import Http404

def check_owner(function):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name="owner").exists():
          print(request.user.groups.all())
          return function(request, *args, **kwargs)
        raise Http404

    return wrapper