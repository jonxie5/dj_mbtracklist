from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def duration_format(value):
    sec = value / 1000
    sec = sec % (24 * 3600)
    sec %= 3600
    min = sec // 60
    sec %= 60
    return "%02d:%02d" % (min, sec)