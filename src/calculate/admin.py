# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Temperature
from models import Average

# Register your models here.
admin.site.register(Temperature)
admin.site.register(Average)
