from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    return num % val


@register.filter
def add(num, val):
    return num + val
    

@register.filter
def sub(num, val):
    return num - val