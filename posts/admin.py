from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#Models
from django.contrib.auth.models import User
from posts.models import Post
# Primer forma de agregarlo.
# admin.site.register(Profile)


#Segunda forma de agregarlo a nuestro dashboard de admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Profile admin."""
    # Podemos personalizar lo que se vea en el listado
    list_display = ('pk','user', 'title', 'photo')

    # Los valores que queremos que al clikcearlos nos lleven al Post
    list_display_links = (['title'])

    # Indicamos por que campos podemos hacer busqueda de Post.
    # User en si, es un objeto, por eso lo ideal seria indicarle con que campo de ese objeto hacemos la busqueda
    search_fields = ('user__email',
                     'title'
    )

    """Trabajando con fieldsets"""
    """fieldsets = (
        ('Profile', {
            'fields': (
                ('user','picture'),     # Esto estara en una fila, en dos columnas
            ),
        }),
        ('Extra info', {                # Esto es otra seccion
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {                  # Esto es otra seccion
            'fields': (
                ('created', 'modified')
            )
        })
    )"""

    # Especifico los campos que no podremos editar.
    readonly_fields = ('created','modified','user')
