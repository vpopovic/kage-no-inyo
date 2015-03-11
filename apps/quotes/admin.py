from django.contrib import admin

from .models import Quote, Author


class QuoteAdmin(admin.ModelAdmin):
    list_filter = ['author']


admin.site.register(Author)
admin.site.register(Quote, QuoteAdmin)
