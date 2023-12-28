from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
                    "placeholder": "Search by date",
                    "type": "datetime-local",
            }
        )
    )
    # deadline = forms.CharField(
    #     # input_formats=["%d.%B.%Y %I:%M%p"],
    #     widget=forms.DateTimeInput(attrs={
    #         "placeholder": "Search by date",
    #         "type": "datetime-local",
    #         "required": False,
    #     }
    #     ),
    # )

    class Meta:
        model = Task
        fields = ("content", "tags", "deadline")

