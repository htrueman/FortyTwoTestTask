from django import forms


class DatePicker(forms.DateInput):
    class Media:
        js = ('js/datepicker.js',
              'http://cdnjs.cloudflare.com/ajax/libs/'
              'bootstrap-datetimepicker/'
              '4.0.0/js/bootstrap-datetimepicker.min.js')
        css = {
            'all': (
                'http://cdnjs.cloudflare.com/ajax/libs/'
                'bootstrap-datetimepicker/'
                '4.0.0/js/bootstrap-datetimepicker.min.js',
            )
        }

    def __init__(self):
        self.attrs = {'class': 'datepicker form-control'}
        super(DatePicker, self).__init__(attrs=self.attrs)
