import datetime
from django import template
from django.utils import timezone

register = template.Library()

@register.filter(name="parsedate")
def parsedate(value):
    diff = datetime.datetime.now() - value.replace(tzinfo=None) 
    day = diff.days
    
    if int(day) >= 1:
        return value.strftime('%Y/%m/%d')

    if value.replace(tzinfo=None).day + 1 == datetime.datetime.now().day:
        return f"Hier à {value.strftime('%H:%M')}"
    return value.strftime('%H:%M')

# print(parsedate(datetime.datetime(2022, 4, 21, 12, 30, 10)))