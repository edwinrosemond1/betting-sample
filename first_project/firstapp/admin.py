from django.contrib import admin
from firstapp.models import AccessRecord, Topic, Webpage, UserProfileInfo

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
# admin.site.register(User)
admin.site.register(UserProfileInfo)

# user: edwin123
# pass: test1234
