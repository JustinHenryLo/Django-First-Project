from django.contrib import admin
from .models import Question,Choice
# Register your models here.
#will appear in localhost/admin/polls
admin.site.register(Question)
admin.site.register(Choice)