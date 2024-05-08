import re
from django.shortcuts import render
from .dfa_logic import build_dfa

def home(request):
    return render(request, 'DFA/index.html')

def process_file(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            content = uploaded_file.read().decode('utf-8')
        else:
            content = request.POST.get('text_input', '')
        
        start_state = build_dfa()
        tokens = re.split('[ ,.!?()\n]', content)
        tokens = [token for token in tokens if token]  # Filter out empty strings
        results = []
        for token in tokens:
            lowercase_token = token.lower()
            is_accepted, path = start_state.testInput(lowercase_token)
            # Split the token by underscores
            token_parts = lowercase_token.split('_')
            results.append({'token': token_parts, 'is_accepted': is_accepted, 'path': path})
        return render(request, 'DFA/results.html', {'results': results, 'original_text': content})
    return render(request, 'DFA/index.html')

