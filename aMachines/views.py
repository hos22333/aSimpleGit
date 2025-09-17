from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Page1Log, UserPagePermission
from .decorators import require_page_permission
import math
from django.contrib.auth.decorators import user_passes_test




# Page 1 - Calculator functionality
@login_required
@require_page_permission('page1')
def page1_view(request):
    if request.method == 'POST':
        inputs = [request.POST.get(f'input{i}', '') for i in range(1, 11)]
        
        result = 0
        for inp in inputs:
            try:
                result += float(inp)
            except ValueError:
                pass
        
        log_entry = Page1Log(
            user=request.user,
            input1=inputs[0],
            input2=inputs[1],
            input3=inputs[2],
            input4=inputs[3],
            input5=inputs[4],
            input6=inputs[5],
            input7=inputs[6],
            input8=inputs[7],
            input9=inputs[8],
            input10=inputs[9],
            result=result
        )
        log_entry.save()
        
        return render(request, 'aMachines/page1.html', {
            'inputs': inputs,
            'result': result,
            'submitted': True
        })
    
    return render(request, 'aMachines/page1.html')

# Page 2 - Special page
@login_required
@require_page_permission('page2')
def page2_view(request):
    return render(request, 'aMachines/page2.html')

# Page 3
@login_required
@require_page_permission('page3')
def page3_view(request):
    return render(request, 'aMachines/page3.html')

# Page 4
@login_required
@require_page_permission('page4')
def page4_view(request):
    return render(request, 'aMachines/page4.html')

# Page 5
@login_required
@require_page_permission('page5')
def page5_view(request):
    return render(request, 'aMachines/page5.html')

# Page 6
@login_required
@require_page_permission('page6')
def page6_view(request):
    return render(request, 'aMachines/page6.html')

# Page 7
@login_required
@require_page_permission('page7')
def page7_view(request):
    return render(request, 'aMachines/page7.html')

# Page 8
@login_required
@require_page_permission('page8')
def page8_view(request):
    return render(request, 'aMachines/page8.html')

# Page 9
@login_required
@require_page_permission('page9')
def page9_view(request):
    return render(request, 'aMachines/page9.html')

# Page 10
@login_required
@require_page_permission('page10')
def page10_view(request):
    return render(request, 'aMachines/page10.html')

# Page 11
@login_required
@require_page_permission('page11')
def page11_view(request):
    return render(request, 'aMachines/page11.html')

# Page 12
@login_required
@require_page_permission('page12')
def page12_view(request):
    return render(request, 'aMachines/page12.html')

# Page 13
@login_required
@require_page_permission('page13')
def page13_view(request):
    return render(request, 'aMachines/page13.html')

# Page 14
@login_required
@require_page_permission('page14')
def page14_view(request):
    return render(request, 'aMachines/page14.html')

# Page 15
@login_required
@require_page_permission('page15')
def page15_view(request):
    return render(request, 'aMachines/page15.html')

@login_required
def authorization_view(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only administrators can access this page.")
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        
        # Get all page permissions from POST data
        page_permissions = {
            'page1': 'page1' in request.POST,
            'page2': 'page2' in request.POST,
            'page3': 'page3' in request.POST,
            'page4': 'page4' in request.POST,
            'page5': 'page5' in request.POST,
            'page6': 'page6' in request.POST,
            'page7': 'page7' in request.POST,
            'page8': 'page8' in request.POST,
            'page9': 'page9' in request.POST,
            'page10': 'page10' in request.POST,
            'page11': 'page11' in request.POST,
            'page12': 'page12' in request.POST,
            'page13': 'page13' in request.POST,
            'page14': 'page14' in request.POST,
            'page15': 'page15' in request.POST,
        }
        
        try:
            permission = UserPagePermission.objects.get(id=user_id)
            # Don't modify permissions for superusers
            if not permission.user.is_superuser:
                permission.can_access_page1 = page_permissions['page1']
                permission.can_access_page2 = page_permissions['page2']
                permission.can_access_page3 = page_permissions['page3']
                permission.can_access_page4 = page_permissions['page4']
                permission.can_access_page5 = page_permissions['page5']
                permission.can_access_page6 = page_permissions['page6']
                permission.can_access_page7 = page_permissions['page7']
                permission.can_access_page8 = page_permissions['page8']
                permission.can_access_page9 = page_permissions['page9']
                permission.can_access_page10 = page_permissions['page10']
                permission.can_access_page11 = page_permissions['page11']
                permission.can_access_page12 = page_permissions['page12']
                permission.can_access_page13 = page_permissions['page13']
                permission.can_access_page14 = page_permissions['page14']
                permission.can_access_page15 = page_permissions['page15']
                permission.save()
                messages.success(request, f'Permissions updated successfully for {permission.user.username}!')
            else:
                messages.info(request, 'Superuser permissions cannot be modified.')
        except UserPagePermission.DoesNotExist:
            messages.error(request, 'User not found!')
    
    permissions = UserPagePermission.objects.select_related('user').all()
    return render(request, 'aMachines/authorization.html', {'permissions': permissions})




@login_required
@user_passes_test(lambda u: u.is_superuser)
def view_logs(request):
    logs = Page1Log.objects.select_related('user').all().order_by('-timestamp')
    return render(request, 'aMachines/view_logs.html', {'logs': logs})