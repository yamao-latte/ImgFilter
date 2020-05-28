from django import forms
#from .models import Document


class PhotoForm(forms.Form):
    image = forms.ImageField()


class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50, empty_value='output')
    file = forms.FileField()


# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('description', 'document', )


