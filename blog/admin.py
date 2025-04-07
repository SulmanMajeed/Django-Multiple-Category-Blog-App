from django.contrib import admin
from .models import Writer, Category, Blog, Newsletter, Contact

# Register your models here.

admin.site.register(Writer)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Newsletter)
admin.site.register(Contact)