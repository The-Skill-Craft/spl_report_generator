from django.contrib import admin
from .models import user,gd,interviewer,apt,pi,resume,essay,pt
# Register your models here.
admin.site.register(user)
admin.site.register(interviewer)
admin.site.register(apt)
admin.site.register(pi)
admin.site.register(resume)
admin.site.register(essay)
admin.site.register(pt)
admin.site.register(gd)