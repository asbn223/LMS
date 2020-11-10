from django import forms
from core.models import Books


# class BookForm(forms.Form):
#     name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'field',
#                 'placeholder': 'Book Name'
#             }
#         )
#     )
#
#     author = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'field',
#                 'placeholder': 'Author'
#             }
#         )
#     )
#
#     publish_date = forms.DateField(
#         widget=forms.DateInput(
#             attrs={
#                 'class': 'field',
#                 'placeholder': 'Publish Date'
#             }
#         )
#     )
#
#     desc = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'field',
#                 'placeholder': 'Enter Book Description'
#             }
#         )
#     )
#
#     image = forms.ImageField(
#     )


class BookForm(forms.ModelForm):

    def __init__(self, *args,**kwargs):
        super(BookForm, self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'field'

    class Meta:
        model = Books
        fields = '__all__'
        widgets = {
            'book_name': forms.TextInput(attrs={'placeholder': 'Book Name'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author'}),
            'publish_date': forms.TextInput(attrs={'placeholder': 'Publish Date'}),
            'desc': forms.Textarea(attrs={'placeholder': 'Enter Book Description'}),
        }


