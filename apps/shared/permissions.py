from rest_framework.permissions import BasePermission, SAFE_METHODS


# class IsAuthenticatedOrReadOnly(BasePermission):
#
#     def has_permission(self, request, view):
#         return bool(
#             request.method in SAFE_METHODS or
#             request.user and
#             request.user.is_authenticated
#         )


class IsInstructorOrAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (request.user and request.user.is_authenticated and

                (request.user.is_instructor() or request.user.is_admin())

                )

class InstructorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        elif request.user.is_admin():
            return True

        return obj.instuctor == request.user