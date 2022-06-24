from django import template
from afisha.models import Category, Movie


register = template.Library()

#вывод всех категорий
@register.simple_tag()
def get_categories():
    return Category.objects.all()


#вывод последдних добавленных
@register.inclusion_tag('afisha/tags/last_movies.html')
def get_last_movies(count=5):
    movies = Movie.objects.filter(draft=False).order_by('-id')[:count]
    return {'last_movies': movies}