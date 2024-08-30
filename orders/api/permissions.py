from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.order.user == request.user


class IsOrderOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
