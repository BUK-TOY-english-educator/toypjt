from .models import Essay
from django.forms import ModelForm

class EssayForm(ModelForm):

    class Meta:
        model = Essay
        fields = ('content',) 