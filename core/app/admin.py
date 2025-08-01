from django.contrib import admin
from . import models

admin.site.register(models.Partners)
admin.site.register(models.News)
admin.site.register(models.Review)
admin.site.register(models.QuestionsAnswers)
admin.site.register(models.Application)