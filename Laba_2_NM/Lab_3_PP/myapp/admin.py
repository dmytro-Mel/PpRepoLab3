from django.contrib import admin
from .models import User, Asset , Wallet , Chain , Status , Invoice

admin.site.register(User)
admin.site.register(Asset)
admin.site.register(Wallet)
admin.site.register(Chain)
admin.site.register(Status)
admin.site.register(Invoice)


# views.py
