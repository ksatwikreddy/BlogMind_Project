# BlogMind_Project/core/forms.py

from django import forms

# Define choices based on your interface
TONE_CHOICES = [
    ('professional', 'Professional'),
    ('casual', 'Casual'),
    ('technical', 'Technical'),
    # Add other tones as needed
]

LENGTH_CHOICES = [
    ('short', 'Short (500 words)'),
    ('medium', 'Medium (1000 words)'),
    ('long', 'Long (2000 words)'),
]

class ContentGeneratorForm(forms.Form):
    # 1. Core Topic Idea (Text Input)
    core_topic = forms.CharField(
        label='1. Core Topic Idea', 
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'e.g., Future of AI in Content Marketing'})
    )
    
    # 2. Desired Tone (Dropdown/Select)
    desired_tone = forms.ChoiceField(
        label='2. Desired Tone', 
        choices=TONE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    # 3. Estimated Length (Dropdown/Select)
    estimated_length = forms.ChoiceField(
        label='3. Estimated Length', 
        choices=LENGTH_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )