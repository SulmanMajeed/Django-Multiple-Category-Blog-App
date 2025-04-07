# In your custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Get an item from a dictionary safely.
    Usage: {{ mydict|get_item:key }}
    """
    # Convert key to lowercase to make case-insensitive matching
    if not isinstance(key, str):
        # If it's not a string, try converting it to string
        key = str(key)
    
    # Check for direct match
    if key in dictionary:
        return dictionary[key]
    
    # Try case-insensitive match
    key_lower = key.lower()
    for dict_key in dictionary:
        if dict_key.lower() == key_lower:
            return dictionary[dict_key]
    
    # Return the default if not found
    return dictionary.get('default', 'gray-500')