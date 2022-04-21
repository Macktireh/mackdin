import datetime
from django import template
from django.utils import timezone

register = template.Library()

@register.filter(name="parsedate")
def parsedate(value):
    diff = datetime.datetime.now() - value.replace(tzinfo=None) 
    day = diff.days
    if(int(day) >= 1):
        return value.strftime('%Y/%m/%d')
    return value.strftime('%H:%M')