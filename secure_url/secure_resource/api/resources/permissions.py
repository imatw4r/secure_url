from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed


QUERY_PARAM_KEY = "password"


class IsPasswordCorrect(BasePermission):
    def has_object_permission(self, request, view, obj):
        password = request.query_params.get(QUERY_PARAM_KEY, None)
        if password is None:
            raise AuthenticationFailed(
                f"Password not provided. Please, use {QUERY_PARAM_KEY!r} query to provide password."
            )
        if password != obj.get_password():
            raise AuthenticationFailed(
                f"Invalid password. Password {password!r} is invalid."
            )
        return True
