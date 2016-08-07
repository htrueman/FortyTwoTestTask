from django import forms

from apps.hello.models import MyData
from apps.hello.widgets import DatePicker


class EditForm(forms.ModelForm):
    class Meta:
        model = MyData
        fields = '__all__'
        widgets = {
            'bio': forms.Textarea(attrs={
                'cols': 35,
                'rows': 7}),
            'other_conts': forms.Textarea(attrs={
                'cols': 35,
                'rows': 7}),
            'birthday': DatePicker(),
            'photo': forms.FileInput(attrs={'id': 'id_photo'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field not in 'birthday':
                self.fields[field].widget.attrs['class'] = 'form-control'
