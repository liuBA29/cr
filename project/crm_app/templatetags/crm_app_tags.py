from crm_app.models import  *
from django import  template



register= template.Library()

@register.simple_tag()
def get_sdelki(filter=None):
    if not filter:
        return Sdelka.objects.all()
    else:
        return Sdelka.objects.filter(pk=filter)



