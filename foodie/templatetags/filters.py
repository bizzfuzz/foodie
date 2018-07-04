from django import template

register = template.Library()
@register.filter
def addClass(field, classname):
    return field.as_widget(attrs = {
        'class': ''.join((field.css_classes(), classname))
    })
