from django.contrib import admin

from bizzzapp.models import Book,seats,details,ImageModel

# Register your models here.
admin.site.register(Book)
admin.site.register(seats)
admin.site.register(details)
admin.site.register(ImageModel)


