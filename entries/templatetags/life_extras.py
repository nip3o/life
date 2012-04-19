from django import template

register = template.Library()

def pointify(value):
    """Replaces commas with points"""
    return value.replace(',', '.')

register.filter('pointify', pointify)