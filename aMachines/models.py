from django.db import models
from django.contrib.auth.models import User

class Page1Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    input1 = models.CharField(max_length=100)
    input2 = models.CharField(max_length=100)
    input3 = models.CharField(max_length=100)
    input4 = models.CharField(max_length=100)
    input5 = models.CharField(max_length=100)
    input6 = models.CharField(max_length=100)
    input7 = models.CharField(max_length=100)
    input8 = models.CharField(max_length=100)
    input9 = models.CharField(max_length=100)
    input10 = models.CharField(max_length=100)
    result = models.FloatField()
    
    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"


class UserPagePermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 15 distinct page permission fields
    can_access_page1 = models.BooleanField(default=False)
    can_access_page2 = models.BooleanField(default=False)
    can_access_page3 = models.BooleanField(default=False)
    can_access_page4 = models.BooleanField(default=False)
    can_access_page5 = models.BooleanField(default=False)
    can_access_page6 = models.BooleanField(default=False)
    can_access_page7 = models.BooleanField(default=False)
    can_access_page8 = models.BooleanField(default=False)
    can_access_page9 = models.BooleanField(default=False)
    can_access_page10 = models.BooleanField(default=False)
    can_access_page11 = models.BooleanField(default=False)
    can_access_page12 = models.BooleanField(default=False)
    can_access_page13 = models.BooleanField(default=False)
    can_access_page14 = models.BooleanField(default=False)
    can_access_page15 = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('user',)
    
    def __str__(self):
        return f"Permissions for {self.user.username}"
    
    def can_access(self, page_name):
        """Check if user can access specific page"""
        if page_name == 'page1': return self.can_access_page1
        elif page_name == 'page2': return self.can_access_page2
        elif page_name == 'page3': return self.can_access_page3
        elif page_name == 'page4': return self.can_access_page4
        elif page_name == 'page5': return self.can_access_page5
        elif page_name == 'page6': return self.can_access_page6
        elif page_name == 'page7': return self.can_access_page7
        elif page_name == 'page8': return self.can_access_page8
        elif page_name == 'page9': return self.can_access_page9
        elif page_name == 'page10': return self.can_access_page10
        elif page_name == 'page11': return self.can_access_page11
        elif page_name == 'page12': return self.can_access_page12
        elif page_name == 'page13': return self.can_access_page13
        elif page_name == 'page14': return self.can_access_page14
        elif page_name == 'page15': return self.can_access_page15
        return False