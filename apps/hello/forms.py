from django import forms

from apps.hello.models import MyData, RequestKeeperModel
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


class ChangeReqsPrior(forms.ModelForm):
    class Meta:
        model = RequestKeeperModel
        fields = ['priority']
        widgets = {
            'priority': forms.TextInput(attrs={'class': 'form-control',
                                               'name': 'priority',
                                               'id': 'form_req',
                                               'label': ''
                                               })
        }

    def __init__(self, *args, **kwargs):
        super(ChangeReqsPrior, self).__init__(*args, **kwargs)
        self.fields['priority'].label = ''
