from django import template
from house.models import Category

register = template.Library()

@register.inclusion_tag('core/category.html')
def category():
    categories = Category.objects.all()
    return {'categories':categories}