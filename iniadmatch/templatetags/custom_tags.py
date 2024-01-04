from django import template
from django.template.defaultfilters import date

register = template.Library()

@register.simple_tag
def display_schedule_time(start, end):
    if start and end:
        start_time_str = date(start, "n/j G:i")
        end_time_str = date(end, "G:i")
        return f"{start_time_str} ~ {end_time_str}"
    else:
        return ""


@register.filter
def tags_to_comma_separated_string(tags):
    return ', '.join(tag.name for tag in tags)