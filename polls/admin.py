from django.contrib import admin

# Register your models here.

from .models import Question, Choice

# admin.site.register(Choice)

class ChoiceInline(admin.StackedInline):
# class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# https://docs.djangoproject.com/en/4.0/intro/tutorial07/
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']

    fieldsets = [
        #The first element of each tuple in fieldsets is the title of the fieldset
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)