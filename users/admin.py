from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#Models
from django.contrib.auth.models import User
from users.models import Profile

# Primer forma de agregarlo.
# admin.site.register(Profile)


#Segunda forma de agregarlo a nuestro dashboard de admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    # Podemos personalizar lo que se vea en el listado
    list_display = ('pk','user', 'phone_number', 'website', 'picture')

    # Los valores que queremos que al clikcearlos nos lleven al Profile
    list_display_links = (['user'])

    #Los campos que queremos que se puedan editar desde el listado directamente
    list_editable = ('phone_number','website','picture')

    # Indicamos por que campos podemos hacer busqueda de Profiles.
    # User en si, es un objeto, por eso lo ideal seria indicarle con que campo de ese objeto hacemos la busqueda
    search_fields = ('user__email',
                     'user__first_name',
                     'user__last_name',
                     'phone_number'
    )

    #Tipos de filtros
    list_filter = ('user__is_staff',
                   'user__is_active',
                   'created',
                   'modified'
    )

    """Trabajando con fieldsets"""
    fieldsets = (
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
    )

    # Especifico los campos que no podremos editar.
    readonly_fields = ('created','modified','user')

# Ahora vamos a agregar la info de Profile dentro de la info de User.
# Para eso tengo que desregistrar el User comun y registrar el User que tiene dentro un inline de Profile

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users"""
    model  = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin"""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)