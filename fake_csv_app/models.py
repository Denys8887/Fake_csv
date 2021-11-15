from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Schema(models.Model):
    class ColumnSeparator(models.TextChoices):
        COMMA = ',', _('Comma(,)')
        SEMICOLON = ';', _('Semicolon(;)')
        PIPE = '|', _('Pipe(|)')

    class StringCharacter(models.TextChoices):
        DOUBLE_QUOTE = '"', _('Double-quote(")')
        SINGLE_QUOTE = '\'', _('Single-quote(\')')

    title = models.CharField(max_length=40)
    column_separator = models.CharField(max_length=30, choices=ColumnSeparator.choices,
                                        default=ColumnSeparator.COMMA)
    string_character = models.CharField(max_length=30, choices=StringCharacter.choices,
                                        default=StringCharacter.DOUBLE_QUOTE)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Column(models.Model):
    class ColumnType(models.TextChoices):
        FULL_NAME = 'Full name', _('Full name')
        EMAIL = 'Email', _('Email')
        PHONE_NUMBER = 'Phone number', _('Phone number')
        JOB = 'Job', _('Job')
        INTEGER = 'Integer', _('Integer')
        COMPANY = 'Company', _('Company')

    name = models.CharField(max_length=40)
    type = models.CharField(max_length=20, choices=ColumnType.choices, default=ColumnType.INTEGER)
    from_value = models.IntegerField(name='From', null=True, blank=True)
    to_value = models.IntegerField(name='To', null=True, blank=True)
    order = models.PositiveIntegerField()
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='columns')

    def __str__(self):
        return f'Column "{self.name}" in Schema "{self.schema}"'


class Dataset(models.Model):
    class Status(models.TextChoices):
        PROCESSING = 'Processing', _('Processing')
        READY = 'Ready', _('Ready')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    csv_file = models.FileField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PROCESSING)
