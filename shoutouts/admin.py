from django.contrib import admin
from .models import ShoutOut, Mention
# Register your models here.

class MentionInLine(admin.StackedInline):
    model = Mention

class ShoutOutAdmin(admin.ModelAdmin):
    list_display = (
        'submitter',
        'created',
        'approved',
        'approved_by',
        'mention_count',
    )
    list_filter = ('approved', )
    readonly_fields = ('created','modified')
    fields = (
        'submitter',
        'body',
        'approved',
        'approved_by',
        'created',
        'modified',
    )
    ordering = ('-created',)
    date_hierarchy = 'created' #for this 'pip install pytz' for timezones
    inlines = [MentionInLine]


admin.site.register(ShoutOut, ShoutOutAdmin)
