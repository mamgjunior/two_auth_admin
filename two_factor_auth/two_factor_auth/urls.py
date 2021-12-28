from django.contrib import admin
from django.urls import path

"""
Será preciso utilizar o model OTPAdminSite em nosso arquivo urls, isso nos permitirá registrar o dispositivo TOTP pela primeira vez.
Então adicione o seguinte código antes da lista urlpatterns.
"""
from django_otp.admin import OTPAdminSite
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin

class OTPAdmin(OTPAdminSite):
    pass

admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin_site.urls),
]
