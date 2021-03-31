from django import forms
from .models import Notification


class UploadNotificationForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Notification title",
                "class": "form-control"
            }
        ))
    notification = forms.FileField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "Choose file",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Notification
        fields = ('title', 'notification', )
