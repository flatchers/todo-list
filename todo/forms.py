from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Task


# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ["date"]


# class TaskForm(forms.ModelForm):
#     tasks = forms.ModelMultipleChoiceField(
#         queryset=Tag.objects.all(),
#         widget=forms.CheckboSelectMultiple,
#         required=Falsex
#     )
#
#     class Meta:
#         model = Task
#         fields = "__all__"


class TaskForm(forms.Form):
    class Meta:
        model = Task
        fields = ("content", "tags", "deadline")
        deadline = forms.DateTimeField(
            # input_formats=["%d.%B.%Y %I:%M%p"],
            # widget=forms.TextInput(attrs={"placeholder": "DD.MM.YYYY"}),
        )

    # def deadline_cleaned_data(self):
    #     deadline = self.cleaned_data["deadline"]
    #     return deadline

