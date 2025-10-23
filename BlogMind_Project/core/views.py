# BlogMind_Project/core/views.py

from django.shortcuts import render
from .forms import ContentGeneratorForm # Make sure this import is correct

def interface_view(request):
    generated_content = "Your AI-generated content will appear here..." # Default text

    if request.method == 'POST':
        form = ContentGeneratorForm(request.POST)
        
        if form.is_valid():
            # **Simulated Processing (The future home of Gemini)**
            topic = form.cleaned_data['core_topic']
            tone = form.cleaned_data['desired_tone']
            length = form.cleaned_data['estimated_length']
            
            # Simulated Content that confirms inputs were received:
            generated_content = (
                f"--- Inputs Received Successfully ---\n"
                f"Topic: {topic.upper()}\n"
                f"Tone: {tone.capitalize()}\n"
                f"Length: {length.capitalize()} (Ready for AI)\n\n"
                f"This data is ready to be sent to the Gemini API when you integrate it."
            )
            # The form remains bound to show the user their previous inputs
            context = {'form': form, 'generated_content': generated_content}
            return render(request, 'core/interface.html', context)
    
    # Handle GET request or invalid POST submission
    else:
        form = ContentGeneratorForm()
        
    context = {'form': form, 'generated_content': generated_content}
    return render(request, 'core/interface.html', context)