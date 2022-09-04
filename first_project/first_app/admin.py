from re import U
from django.contrib import admin
from first_app.models import Topic, AccessRecord, Webpage, User

admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(User)
