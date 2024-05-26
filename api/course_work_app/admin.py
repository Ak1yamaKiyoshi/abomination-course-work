from django.contrib import admin
from .models import Ankete, Keywords, PasswordRestoration, ClosedInfo, OpenInfo, Invitation, Ankete

admin.site.register(Ankete)
admin.site.register(Keywords)
admin.site.register(PasswordRestoration)
admin.site.register(ClosedInfo)
admin.site.register(OpenInfo)
admin.site.register(Invitation)
