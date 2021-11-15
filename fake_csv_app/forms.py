from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Field
from django.forms import ModelForm

from .models import Schema, Column


class SchemaForm(ModelForm):

    class Meta:
        model = Schema
        fields = ('title', 'column_separator', 'string_character')

    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop('is_add', False)
        super(SchemaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'd-flex justify-content-left'
        self.helper.layout = Layout(
            'title',
            'column_separator',
            'string_character',
            Submit('submit', 'Add columns' if self.is_add else 'Edit columns', css_class='btn btn-primary')
        )


class ColumnForm(ModelForm):

    class Meta:
        model = Column
        fields = ('name', 'type', 'From', 'To', 'order')

    def __init__(self, *args, **kwargs):
        self.is_add = kwargs.pop('is_add', False)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = 'd-flex justify-content-left mx-1'
        self.helper.field_class = 'mx-1'
        self.fields['From'].disabled = False
        self.fields['To'].disabled = False
        self.helper.layout = Layout(
            Row(
                Field('name'),
                Field('type'),
                Field('From'),
                Field('To'),
                Field('order'),
            ),
            Submit('submit', 'Add column' if self.is_add else 'Edit column', css_class='btn btn-primary')
        )
