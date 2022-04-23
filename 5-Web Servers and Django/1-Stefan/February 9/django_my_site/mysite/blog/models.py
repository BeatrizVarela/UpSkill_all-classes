from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

# todas as classes (models.Model) são uma extenção - uma tabela na base de dados
class Post(models.Model):
    # isto é o que faz aparecer o drop down nas escolhas
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    tags = TaggableManager()
    # estes managers são essencialmente as views da Base de Dados
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    # esta só a dizer que é para ordenar os resultados por ondem inversa de publicação
    class Meta:
        #ordering = ('-publish',)
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day, self.slug])

# para criar comentarios no post
class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    # para texto mais extenso
    body = models.TextField()
    # este impoe um limite de caracteres
    name = models.CharField(max_length=80)
    email = models.EmailField()
    # auto_now_add - gera auto uma data, mas nao podemos defenir a data (nao permite ser alterado)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # permite desativar comments e assim
    active = models.BooleanField(default=True)


    class Meta:
        # tem uma virgula porque é um tuplo
        # ordem de mostra dos comments
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'