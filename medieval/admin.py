from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class IndexPageAdmin(SummernoteModelAdmin):
    summernote_fields = ('about_me',  'work_experiens', 'projects')

admin.site.register(King)
admin.site.register(Person)
admin.site.register(Servant)
admin.site.register(IndexPage, IndexPageAdmin)
