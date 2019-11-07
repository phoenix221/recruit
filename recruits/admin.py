from django.contrib import admin
from .models import Sith, Planet, ShadowHands, Question, ChoiceQuestion, Recruit

class ChoiceQuestionsInline(admin.StackedInline):
    model = ChoiceQuestion
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceQuestionsInline]


# Register your models here.
admin.site.register(Sith)
admin.site.register(Planet)
admin.site.register(ShadowHands)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Recruit)