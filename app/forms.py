from django import forms
from .models import Notification


class UploadNotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('title', 'notification', )
