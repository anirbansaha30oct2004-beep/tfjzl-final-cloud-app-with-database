from django.contrib import admin
from .models import Course, Lesson, Instructor, Question, Choice

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Instructor)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)