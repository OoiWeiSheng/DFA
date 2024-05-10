import re
from django.shortcuts import render
from .dfa_logic import build_dfa

def home(request):
    start_state, accepted_words = build_dfa()
    return render(request, 'DFA/index.html', {'accepted_words': accepted_words})

def process_file(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            content = uploaded_file.read().decode('utf-8')
        else:
            content = request.POST.get('text_input', '')
            
        content = content.replace('\r', '') #Remove line break
        
        start_state, accepted_words = build_dfa() #Build a starting state, accepted_words is not used here (used in home())
        tokens = re.split('[ ,.–!-?()\n]', content)   # Remove special characters
        tokens = [token for token in tokens if token]   # Tokenization
        results = [] # To store tokens, path, is_accepted
        
        for token in tokens:
            lowercase_token = token.lower() # lower case for each tokens
            is_accepted, path = start_state.testInput(lowercase_token) # Run DFA
            # Split the token by underscores
            token_parts = lowercase_token.split('_')
            results.append({'token': token_parts, 'is_accepted': is_accepted, 'path': path})
            
        # Extract accepted string counts from the start state
        accepted_counts = start_state.accepted_counts
        
        return render(request, 'DFA/results.html', {'results': results, 'original_text': content, 'accepted_counts': accepted_counts})
    return render(request, 'DFA/index.html')
