from django.http import HttpResponseForbidden
from .models import UserPagePermission

def require_page_permission(page_name):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            # Allow superusers to access all pages
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            
            try:
                permission = UserPagePermission.objects.get(user=request.user)
                if permission.can_access(page_name):
                    return view_func(request, *args, **kwargs)
            except UserPagePermission.DoesNotExist:
                pass
            
            return HttpResponseForbidden(f"You don't have permission to access {page_name}. Please contact an administrator.")
        return wrapper
    return decorator