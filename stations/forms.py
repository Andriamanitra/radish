from django import forms
from .models import Station, StationUrl


class StationForm(forms.Form):
    name = forms.CharField(label="Name", max_length=63)
    description = forms.CharField(label="Description", max_length=255)
    url = forms.URLField(label="Link to stream", max_length=255)

    def url_is_good(self):
        for extension in [".m3u", ".mp3", ".pls", ".m3u8", ".xspf", ".asx"]:
            if self.cleaned_data["url"].endswith(extension):
                print(extension)
                return True
        return False

    def store(self):
        s = Station(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"]
        )
        s.save()
        s_url = StationUrl(
            url=self.cleaned_data["url"],
            station=s
        )
        s_url.save()


class StationUrlForm(forms.ModelForm):
    class Meta:
        model = StationUrl
        fields = ["url"]
