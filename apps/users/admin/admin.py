from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group

from apps.users.models import Blog, Category, Comment, Course, Payment, Setting, Step, User
from users.models import FAQ, Enrollment, Lesson, Promocode, Review, Section, Tag
from users.models.setting import Device


# users.py
@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


# tags.py
@admin.register(Tag)
class TagModelAdmin(ModelAdmin):
    list_display = ('title',)


# setting.py
@admin.register(Setting)
class SettingsModelAdmin(ModelAdmin):
    list_display = ('phone', 'contact_email', 'support_email', 'address')

    # readonly_fields = ('latitude', 'longitude')

    def has_add_permission(self, request):
        return not Setting.objects.exists()


@admin.register(FAQ)
class FAQModelAdmin(ModelAdmin):
    list_display = ('question', 'answer')


@admin.register(Device)
class DeviceModelAdmin(ModelAdmin):
    list_display = ("device_id", 'created_at', 'updated_at')


# payment.py
@admin.register(Payment)
class PaymentModelAdmin(ModelAdmin):
    list_display = ('discount', 'course_name', 'course_price', 'payment_type', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(Promocode)
class PromocodeModelAdmin(ModelAdmin):
    list_display = ('title', 'amount', 'created_at', 'expiry_date')


# course.py
@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ('title', 'short_description', 'lesson_count', 'student_count', 'get_instructors')
    search_fields = ('title',)
    list_filter = ('title',)

    @admin.display(description="Instructors")
    def get_instructors(self, obj):
        return ", ".join([i.full_name for i in obj.instructor.all()])

    def student_count(self, obj):
        return obj.students.count()


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    # prepopulated_fields = {"slug": ("name",)}
    list_filter = ('name',)
    ordering = ('name',)


@admin.register(Lesson)
class LessonModelAdmin(ModelAdmin):
    list_display = ('section', 'title', 'video_url', 'lesson_content', 'duration', 'lesson_status')

    @admin.display(description="Instructors")
    def get_instructors(self, obj):
        return ", ".join([i.full_name for i in obj.instructor.all()])

    def student_count(self, obj):
        return obj.students.count()


@admin.register(Section)
class Section(ModelAdmin):
    list_display = ('course', 'order_num', 'title')


@admin.register(Enrollment)
class EnrollmentModelAdmin(ModelAdmin):
    list_display = ('course', 'student', 'status')


@admin.register(Review)
class ReviewModelAdmin(ModelAdmin):
    list_display = ('course', 'student', 'comment', 'video_comment')


# blogs.py
@admin.register(Blog)
class BlogModelAdmin(ModelAdmin):
    list_display = ('title', 'image', 'is_published', 'content')
    list_filter = ('category', 'tags', 'is_published')


@admin.register(Comment)
class CommentModelAdmin(ModelAdmin):
    list_display = ('user', 'message', 'created_at')
    list_filter = ('user', 'created_at')


@admin.register(Step)
class StepModelAdmin(ModelAdmin):
    list_display = 'title',


admin.site.unregister(Group)
