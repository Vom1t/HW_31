from rest_framework.permissions import BasePermission


class AdOwnerPermission(BasePermission):
    message = 'Вы не Модератор'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in ('admin', 'moderator'):
            return True
        return False