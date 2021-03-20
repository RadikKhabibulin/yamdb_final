from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ('username',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
