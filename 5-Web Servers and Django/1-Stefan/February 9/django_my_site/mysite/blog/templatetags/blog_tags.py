import markdown
from django import template
from django.utils.safestring import mark_safe

from ..forms import SearchForm
from ..models import Post
# existem dois tipos de tags (simples, e de inclusão)


register = template.Library()
# tag simples
@register.simple_tag()
def total_posts():
    return Post.published.count()
# aplicar a tag na base.html


# tag de inclusao
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    # a tag de inclusao tem de retornar um contexto
    return {"latest_posts": latest_posts}


# criacção de filtro (pip install markdown)
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


# invocar o formulario e depois mandamos para o serach_bar
@register.inclusion_tag('blog/post/search_bar.html')
def search_bar():
    search_form = SearchForm() # o formulario é vazio pq é para pesquisa
    return {"search_form": search_form} # retorna o fomulario ao contexto