from django import template
from django.template.defaultfilters import date
from datetime import datetime

register = template.Library()

@register.simple_tag
def display_schedule_time(day, start, end):
    if day and start and end:
        date_str = date(day, "n/j")
        start_time_str = date(start, "G:i")
        end_time_str = date(end, "G:i")
        return f"{date_str} {start_time_str} ~ {end_time_str}"
    else:
        return ""

@register.simple_tag
def url_schedule_time(day, start, end):
    if day and start and end:
        formatted_str = f"{day.strftime('%Y%m%d')}T{start.strftime('%H%M%S')}00/{day.strftime('%Y%m%d')}T{end.strftime('%H%M%S')}00"
        return formatted_str
    else:
        return ""
    
    
@register.filter
def tags_to_comma_separated_string(tags):
    return ', '.join(tag.name for tag in tags)