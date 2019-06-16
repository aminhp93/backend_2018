from django.contrib import admin

# Register your models here.
from stocks.models import Stock

admin.site.register(Stock)
