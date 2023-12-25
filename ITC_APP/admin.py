from django.contrib import admin
from .models import Anggota,Sertifikat, Bidang, Pengurus,Program,Event,Notification

# # Register your models here.
admin.site.register(Anggota)
admin.site.register(Sertifikat)
admin.site.register(Bidang)
admin.site.register(Pengurus)
admin.site.register(Program)
admin.site.register(Event)
admin.site.register(Notification)