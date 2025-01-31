from django import forms

from todo_app.models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name",]


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        required=True
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
