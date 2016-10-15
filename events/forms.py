from django import forms
from django.contrib.auth.models import User
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 
from events.models import Event

class EventForm(forms.Form):

    METHOD_OF_CONTACT = (
        ('EMAIL','Email'),
        ('CALL', 'Call'),
        ('TEXT', 'Text'),
    )
    eventtype = forms.CharField(required=False,label='Title', widget=forms.TextInput(attrs={'placeholder': 'Title of event'}))
    snap = forms.FileField(required=False,label='Event Look-up Picture ')    
      #date_event = forms.DateTimeField(label='Event Date',widget=DateTimeWidget(usel10n=True, bootstrap_version=3))    
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'cols': 22, 'rows': 2 ,'placeholder': 'Give some overview of your event'}))
    place = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=METHOD_OF_CONTACT,label='Preferred Method of Contact',
    )
    zip_Code = forms.CharField(label='Zipcode', widget=forms.TextInput(attrs={'placeholder': 'Zipcode of your area'})
    )
     #duration = forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))
     # dresscode = forms.BooleanField(label='Event Dress Code Allow'    )  

class HostForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('eventtype', 'snap', 'description','place', 'zip_Code', )
  
    
    
