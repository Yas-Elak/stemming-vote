from django import template
register = template.Library()

@register.filter
def pourcent( value, arg ):
    '''
    Divides the value; argument is the divisor and make it a pourcentage
    Returns empty string on any error.
    '''
    try:
        value = int( value )
        arg = int( arg )

        if arg: return str(round((value / arg) * 100, 2))
    except: pass
    return ''