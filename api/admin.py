from django.contrib import admin
from . import models

admin.site.register(models.InboxItem)
admin.site.register(models.TaskItem)
admin.site.register(models.ProjectItem)
admin.site.register(models.FilterItem)
admin.site.register(models.TagItem)