from django.contrib import admin
from .models import Question, Choice
# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question'        , {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})    
    ]
    inlines = [ChoiceInLine]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_field = ['question_text']

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)