from django import forms

class StationForm(forms.Form):
    name = forms.CharField(label="Name", max_length=63)
    description = forms.CharField(label="Description", max_length=255)
    url = forms.URLField(label="Link to stream (for example .m3u or .pls)", max_length=255)