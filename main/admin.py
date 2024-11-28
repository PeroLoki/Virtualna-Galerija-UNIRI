from django.contrib import admin
from .models import *

model_list = [Category, Image]

admin.site.register(model_list)
