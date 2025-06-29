from rest_framework import permissions
from .models import User


class RolePermission(permissions.BasePermission):
    required_role = None

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == self.required_role)


class IsAdminWolky(RolePermission):
    required_role = User.ADMIN_WOLKY


class IsAdminEmpresa(RolePermission):
    required_role = User.ADMIN_EMPRESA


class IsChofer(RolePermission):
    required_role = User.CHOFER


class IsOperador(RolePermission):
    required_role = User.OPERADOR
