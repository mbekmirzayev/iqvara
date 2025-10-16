from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group

from apps.users.models import Course, User, Category, Settings, Order, Blog, Comment, Step


@admin.register(Settings)
class SettingsModelAdmin(admin.ModelAdmin):
    list_display = ('phone', 'contact_email', 'support_email', 'address')
    readonly_fields = ('latitude', 'longitude')

    def has_add_permission(self, request):
        return not Settings.objects.exists()


@admin.register(Order)
class OrderModelAdmin(ModelAdmin):
    list_display = ('amount',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'lesson_count', 'student_count',)
    search_fields = ('title',)
    list_filter = ('title',)

    def lesson_count(self, obj):
        return obj.lessons.count()

    lesson_count.short_description = 'Darslar soni'

    def student_count(self, obj):
        return obj.students.count()

    student_count.short_description = 'darsni sotib olgan studentlar soni'

    def review_count(self, value):
        return value.review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    # prepopulated_fields = {"slug": ("name",)}
    list_filter = ('name',)
    ordering = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title' , 'image' , 'is_published' , 'content')
    list_filter = ('category', 'tags', 'is_published')


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at')
    list_filter = ('user', 'created_at')


@admin.register(Step)
class StepModelAdmin(admin.ModelAdmin):
    list_display = 'title',


admin.site.unregister(Group)
