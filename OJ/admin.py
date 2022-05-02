from django.contrib import admin

# Register your models here.

from OJ.models import Problem, Submission, TestCase

admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(TestCase)