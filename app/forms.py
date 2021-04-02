from django import forms
from .models import Notification, Subject, Notes, QuestionPaper


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
            attrs={'accept':'application/pdf',
                   'class':'form-control'}
        ))

    class Meta:
        model = Notification
        fields = ('title', 'notification', )


class AddSubjectForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Subject name",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Subject
        fields = ('name',)


class AddSubjectNotesForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Note Title",
                "class": "form-control"
            }
        ))
    subject = forms.ModelChoiceField(

        widget=forms.Select(
            attrs={

                "class": "form-control"
            }
        ),
        queryset=Subject.objects.all(),
        empty_label="Choose subject"
    )

    note = forms.FileField(
        widget=forms.FileInput(
            attrs={
                   'class': 'form-control'}
        ))

    class Meta:
        model = Notes
        fields = ('title', 'subject', 'note')


class AddSubjectQpForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "QP title",
                "class": "form-control"
            }
        ))
    subject = forms.ModelChoiceField(

        widget=forms.Select(
            attrs={

                "class": "form-control"
            }
        ),
        queryset=Subject.objects.all(),
        empty_label="Choose subject"
    )

    year = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "year",
                "class": "form-control"
            }
        ))

    qp = forms.FileField(
        widget=forms.FileInput(
            attrs={'accept': 'application/pdf',
                   'class': 'form-control'}
        ))

    class Meta:
        model = QuestionPaper
        fields = ('title', 'year', 'subject', 'qp')
