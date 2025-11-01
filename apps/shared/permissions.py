from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import User

class IsAdminUser(BasePermission):
    """
    Faqat admin foydalanuvchilarga ruxsat beradi.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == User.Status.ADMIN


class IsInstructorOrAdmin(BasePermission):
    """
    Faqat o‘qituvchi (instructor) yoki admin foydalanuvchilarga ruxsat beradi.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            (request.user.role in User.Status.INSTRUCTOR or request.user.role in User.Status.ADMIN)
        )


class IsStudentOrAdmin(BasePermission):
    """
    Faqat student yoki admin foydalanuvchilarga ruxsat beradi.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            (request.user.role in User.Status.STUDENT or request.user.role in User.Status.ADMIN)
        )


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Kirgan foydalanuvchi POST/PUT/DELETE qila oladi,
    boshqalar faqat GET (ko‘rish) qilishi mumkin.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.role in User.Status.STUDENT )

class IsOwnerOrAdmin(BasePermission):
    """
    Obyekt egasiga (masalan, o‘zi yaratgan comment, payment) yoki admin userga ruxsat beradi.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated and (
                obj.user == request.user or
                request.user.role == User.Status.ADMIN
            )
        )


class IsEnrolledOrReadOnly(BasePermission):
    """
    Kursni ko‘rish uchun user enroll bo‘lgan bo‘lishi kerak,
    lekin umumiy ma’lumotni (list/retrieve) hamma ko‘rishi mumkin.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # obj bu Lesson yoki Course bo‘lishi mumkin
        return (
            request.user.is_authenticated and
            obj.enrollments.filter(student=request.user).exists()
        )


class AllowAny(BasePermission):
    """
    Hamma foydalanuvchiga ruxsat (hatto login qilmaganlarga ham).
    """
    def has_permission(self, request, view):
        return True
