from django.contrib import admin
from .models import Post, Comment

# o arroba é uma anotação
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # define os campos que vemos na nossa pagina de admin para o post
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # parametros de filtragem de conteudos
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # preenche automaticamente o campo slug
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


# regista os nosso modelos
# permite que a pagina admin aceda ao modelos do nosso blo@g (app)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('post', 'active', 'name', 'email', 'body') # ordem dos campos na edição
    list_display = ('post', 'active', 'name', 'email', 'body') # ordem das colunas na vista de lista da entidade
    list_filter = ('active', 'created', 'updated') # filtros na pagina do admin
    search_fields = ('name', 'email', 'body', 'post__tile') # campos pelos quais se pode pesquisar no admin, o __ é a convencao para a referencia