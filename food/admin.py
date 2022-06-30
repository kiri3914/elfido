from django.contrib import admin
from .models import Food, Table, BookTable, Category, Response, Event

admin.site.register(Food)
admin.site.register(Table)
admin.site.register(BookTable)
admin.site.register(Category)
admin.site.register(Response)
admin.site.register(Event)
