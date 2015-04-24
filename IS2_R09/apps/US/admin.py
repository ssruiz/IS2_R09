# -*- encoding: utf-8 -*-

"""
    Modulo que registra los L{modelos<IS2_R09.apps.US.models>} creados para los B{User Stories} en el Admin de Django  
"""
from django.contrib import admin
from IS2_R09.apps.US.models import us
admin.site.register(us)