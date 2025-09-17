def user_permissions(request):
    if request.user.is_authenticated:
        # Superusers have access to all pages
        if request.user.is_superuser:
            return {
                'user_perms': {
                    'can_access_page1': True,
                    'can_access_page2': True,
                    'can_access_page3': True,
                    'can_access_page4': True,
                    'can_access_page5': True,
                    'can_access_page6': True,
                    'can_access_page7': True,
                    'can_access_page8': True,
                    'can_access_page9': True,
                    'can_access_page10': True,
                    'can_access_page11': True,
                    'can_access_page12': True,
                    'can_access_page13': True,
                    'can_access_page14': True,
                    'can_access_page15': True,
                    'is_superuser': True
                }
            }
        
        try:
            from .models import UserPagePermission
            permissions = UserPagePermission.objects.get(user=request.user)
            return {
                'user_perms': {
                    'can_access_page1': permissions.can_access_page1,
                    'can_access_page2': permissions.can_access_page2,
                    'can_access_page3': permissions.can_access_page3,
                    'can_access_page4': permissions.can_access_page4,
                    'can_access_page5': permissions.can_access_page5,
                    'can_access_page6': permissions.can_access_page6,
                    'can_access_page7': permissions.can_access_page7,
                    'can_access_page8': permissions.can_access_page8,
                    'can_access_page9': permissions.can_access_page9,
                    'can_access_page10': permissions.can_access_page10,
                    'can_access_page11': permissions.can_access_page11,
                    'can_access_page12': permissions.can_access_page12,
                    'can_access_page13': permissions.can_access_page13,
                    'can_access_page14': permissions.can_access_page14,
                    'can_access_page15': permissions.can_access_page15,
                    'is_superuser': False
                }
            }
        except UserPagePermission.DoesNotExist:
            return {'user_perms': None}
    return {'user_perms': None}