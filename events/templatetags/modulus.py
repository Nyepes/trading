import math
from django import template

register = template.Library()


@register.filter(name='modulus')
def modulus(a,b):
    return a%b