from django.contrib import admin
from bookstore.models import Books, Authors, Comments

admin.site.register(Authors)


class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Books._meta.fields]
    search_fields = ['title', 'id', 'author__first_name']
    list_filter = ['title', 'id', 'author']
    list_editable = ('title',)

    class Meta:
        model = Books


class CoomentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comments._meta.fields]
    search_fields = ['body', 'id', 'book__id']
    list_filter = ['body', 'id', 'author', 'book']
    list_editable = ('body',)

    class Meta:
        model = Comments

admin.site.register(Books, BookAdmin)
admin.site.register(Comments, CoomentAdmin)
