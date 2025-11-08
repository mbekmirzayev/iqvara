from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminUser(BasePermission):
    """
    Faqat admin foydalanuvchilarga ruxsat beradi.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsInstructorOrAdmin(BasePermission):
    """
    Faqat o‘qituvchi (instructor) yoki admin foydalanuvchilarga ruxsat beradi.
    """

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_instructor or user.is_admin)


class IsStudentOrAdmin(BasePermission):
    """
    Faqat student yoki admin foydalanuvchilarga ruxsat beradi.
    """

    def has_permission(self, request, view):
        return (
                request.user.is_authenticated and
                (request.user.is_student or request.user.is_admin)
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
                request.user.is_authenticated and request.user.is_student
        )


class IsOwnerOrAdmin(BasePermission):
    """
    Obyekt egasiga (masalan, o‘zi yaratgan comment, payment) yoki admin userga ruxsat beradi.
    """

    def has_object_permission(self, request, view, obj):
        return (
                request.user.is_authenticated and
                (
                        obj.user == request.user or
                        request.user.is_admin
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
