from django.template import Library
import re
from html import unescape

register = Library()

@register.filter
def fix_text(string):
    string = re.sub('&nbsp;', ' ', string)
    string = re.sub('\n', ' ', string)
    string = re.sub('\r', ' ', string)
    return string

@register.filter
def in_category_terms(category, letter):
    return category.filter(name__istartswith=letter).order_by('name')


@register.filter
def in_category_authors(category, letter):
    return category.filter(last_name__istartswith=letter).order_by('last_name')


@register.filter
def in_category_books(category, letter):
    return category.filter(title__istartswith=letter).order_by('title')


@register.filter
def split_chapters(chapters):
    return chapters.split('$ ')


@register.filter
def chapter_length(chapter):
    return len(chapter)


@register.filter
def check_author(pub, author):
    if author in str(pub):
        return True
    else:
        return False