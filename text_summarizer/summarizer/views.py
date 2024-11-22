from django.shortcuts import render
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(request):
    summary = None
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            # Adjust max_length and min_length for better summaries
            summary = summarizer(text, max_length=200, min_length=50, do_sample=False)[0]['summary_text']
    return render(request, 'summarizer/summarize.html', {'summary': summary})
