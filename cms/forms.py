from django import forms
#from .models import Document


class PhotoForm(forms.Form):
    image = forms.ImageField()


class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50, empty_value='output')
    file = forms.FileField(widget=forms.FileInput(attrs={'onchange': 'previewImage(this)'}))


class KernelChoiceForm(forms.Form):
    choicel = forms.ChoiceField(
        choices=(
            ('3', '3*3'),
            ('5', '5*5')
        ),
        label='カーネルサイズ',
        initial=['0'],
        required=True,
        widget=forms.Select()
        #attrs={'id': 'two', 'name': 'two' }
    )


class SimpleChoiceForm(forms.Form):
    choicels = forms.ChoiceField(
        choices=(
            ('0', 'Vertical Scharr Filter'),
            ('1', 'Horizontal Scharr Filter'),
            ('2', 'Laplacian Filter'),
            ('3', 'Blur Filter'),
            ('4', 'Motion Filter'),
            ('5', '自分でカーネルを設定する')
        ),
        label='フィルタ選択',
        initial=['5'],
        required=True,
        widget=forms.Select()
        #attrs={'id': 'one', 'name': 'one'}
    )


