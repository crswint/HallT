from django.contrib import admin
from apps.tran_maps import models
# Register your models here.
# we want to see this model in the admin page, this accomplishes that

admin.site.register(models.Stop)
admin.site.register(models.Route)

