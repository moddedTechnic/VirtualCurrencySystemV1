from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def controls(*directions: str):
    directions = set(directions)

    up = '' if 'up' in directions else 'disabled'
    down = '' if 'down' in directions else 'disabled'
    left = '' if 'left' in directions else 'disabled'
    right = '' if 'right' in directions else 'disabled'

    vert = 'up' in directions or 'down' in directions
    horiz = 'left' in directions or 'right' in directions

    result = '<section class="controls">'
    if vert:
        result += f'<button class="up" {up}></button>'
        result += f'<button class="down" {down}></button>'
    if horiz:
        result += f'<button class="left" {left}></button>'
        result += f'<button class="right" {right}></button>'
    result += '</section>'

    return mark_safe(result) if vert or horiz else ''
