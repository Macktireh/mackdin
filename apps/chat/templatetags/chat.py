import datetime
from django import template
from django.utils import timezone
from django.utils.translation import gettext as _

register = template.Library()

def add_2_hour(arg):
    if arg.hour == 22:
        arg = arg.replace(day=arg.day + 1)
        arg = arg.replace(hour=00)
        return arg
    elif arg.hour == 23:
        arg = arg.replace(day=arg.day + 1)
        arg = arg.replace(hour=1)
        return arg
    else:
        arg = arg.replace(hour=arg.hour + 2)
        return arg
    

@register.filter(name="parsedate")
def parsedate(value):
    date_last_msg = add_2_hour(value)
    diff = datetime.datetime.now() - date_last_msg.replace(tzinfo=None)
    day = diff.days
    
    if int(day) >= 1:
        return date_last_msg.strftime('%Y/%m/%d')

    if date_last_msg.day + 1 == datetime.datetime.now().day:
        return f"{_('Hier à')} {date_last_msg.strftime('%H:%M')}"
    return date_last_msg.strftime('%H:%M')

# print(parsedate(datetime.datetime(2022, 4, 21, 12, 30, 10)))

@register.filter(name="timestr")
def timestr(value):
    string_date = str(value)
    string_date = string_date.split(',')[0]
    return string_date

@register.filter(name="is_connected_user")
def is_connected_user(value):
    date_last_logout = add_2_hour(value)
    diff = datetime.datetime.now() - date_last_logout.replace(tzinfo=None)
    h = diff.total_seconds() / 3600
    if h < 1:
        return True
    return False