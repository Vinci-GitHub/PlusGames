from django.contrib import admin

from .models import Game


class GameModalAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'id', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at')


admin.site.register(Game, GameModalAdmin)
