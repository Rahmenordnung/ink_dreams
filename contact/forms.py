from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from django import forms

class ContactForm(forms.Form):
  name = forms.CharField()
  email = forms.EmailField(label='E-Mail')
  category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other'), ('feedback', 'Feedback'), ('information', 'Information'), ('returns & complains', 'Returns & Complains'), ('cashback', 'Cashback') ])
  subject = forms.CharField(required=False)
  body = forms.CharField(widget=forms.Textarea)
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.helper = FormHelper
    self.helper.form_method = 'post'
    
    self.helper.layout = Layout(
      'name',
      'email',
      'category',
      'body',
      Submit('submit', 'Submit', css_class='btn-succes')
    )