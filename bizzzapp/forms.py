from django import forms
from bizzzapp.models import Book, ImageModel, details


class bookingForm(forms.ModelForm):
    class Meta:
        model = Book
        fields='__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','title','price']

class detailsForm(forms.ModelForm):
    class Meta:
        model = details
        fields = '__all__'

