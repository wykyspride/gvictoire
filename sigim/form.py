from django import forms
from .models import bien,compbien, tests


class biensForm(forms.Form):
    #biens=forms.ModelChoiceField(queryset=bien.objects.filter(status="valide"),
    #NameChoiceField est la class definie dans le model <<bien> pour recuper le nom des biens enregistrés
    biens=bien.NameChoiceField(queryset=bien.objects.filter(status="valide"),
        widget=forms.Select(attrs={"hx-get": "load_piece/", "hx-target":"#id_pieces"}),
        to_field_name="id")
    pieces=forms.ModelChoiceField(queryset=compbien.objects.none())
    #loyer=forms.ModelChoiceField(queryset=compbien.objects.none(),
        #widget=forms.Select(attrs={"hx-get": "load_piece_details/", "hx-target":"#id_loyer"}))
    

class composantsForm(forms.ModelForm):
    npieces=compbien.NameChoiceFieldpiece(queryset=compbien.objects.all(),
        widget=forms.Select(attrs={"hx-get": "load_piece_details/", "hx-target":"#id_lapiece"}))
    lapiece=forms.ModelChoiceField(queryset=compbien.objects.none())
    class Meta:
        model=compbien
        fields=['nomcomposant','loyer']

   

# class formpieces(forms.ModelForm):
    
#     npieces=compbien.NameChoiceFieldpiece(queryset=compbien.objects.all(),
#         widget=forms.Select(attrs={"hx-get": "load_piece_details/", "hx-target":"#id_lapiece"}))
#     lapiece=forms.ModelChoiceField(queryset=compbien.objects.none())

    
#     class Meta:
#         model=compbien
#         fields=['nomcomposant','loyer']
#         widget={
#             'nomcomposant': forms.Textarea(attrs={'class': 'form-control'}),
#             'loyer': forms.Select(attrs={'class': 'form-control'}),
#         }


class formtest(forms.ModelForm):
    class Meta:
        model=tests
        #fields=('text', 'photo', 'doc')
        fields=('__all__')
