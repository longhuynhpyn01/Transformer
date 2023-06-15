from django.shortcuts import render
import json
from django.http import JsonResponse
import requests

def get_data(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        # print("data:", data)
        text = data.get('input', '')
        
        print("text:", text)

        API_URL = "https://api-inference.huggingface.co/models/ntclai/en_vi_translation_1"
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs": text,
        })

        print("translate:", output[0]['translation_text'])
        
        return JsonResponse({'message': output[0]['translation_text']})


    return JsonResponse({'error': 'Invalid request method'})
