from django import template

register = template.Library()


@register.filter
def reading_time(words, wpm=250):
    """
    Returns a plain English estimated reading time
    """
    minutes = words / wpm
    if minutes <= 1.15:
        return "About a minute."
    else:
        return f"About {int(minutes)} minutes."



