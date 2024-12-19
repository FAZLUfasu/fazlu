from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Retrieve the value from the dictionary by key."""
    return dictionary.get(key)
