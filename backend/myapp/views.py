from django.shortcuts import render
import json
from django.http import JsonResponse
from transformers import T5ForConditionalGeneration, T5Tokenizer
from .handle import *


def get_data(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode) # type là dict
        input_data = data.get('input', '') # hoặc data['input']
        
        finding = Transformer("123")
        results = finding.get_results()
        query = finding.get_query()
        print("query:", query)
        print("results:", results)
    
        # Xử lý dữ liệu ở đây và trả về kết quả
        response_data = {'message': f'Received input: {input_data}'}
    elif request.method == 'PUT':
        # Xử lý yêu cầu PUT
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        input_data = data.get('input', '')
        # Xử lý dữ liệu ở đây và trả về kết quả
        response_data = {'message': f'Received input from PUT: {input_data}'}
    else:
        response_data = {'message': 'Hello from the backend!'}
        
    return JsonResponse(response_data, status=200)


def summarize_text(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        # print("data:", data)
        text = data.get('input', '')
        
        print("text:", text)

        # Khởi tạo mô hình Transformer và tokenizer
        model = T5ForConditionalGeneration.from_pretrained('t5-base')
        # tokenizer = T5Tokenizer.from_pretrained('t5-base')
        
        print("model:", model)
        # print("tokenizer:", tokenizer)

        # # Tiền xử lý văn bản
        # inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
        
        # print("inputs:", inputs)


        # # Tóm tắt văn bản
        # summary_ids = model.generate(inputs, num_beams=4, max_length=150, length_penalty=2.0, early_stopping=True)
        # summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # print("summary_ids:", summary_ids)
        # print("summary:", summary)

        # return JsonResponse({'summary': summary})
        return JsonResponse({'summary': '1232cgd'})


    return JsonResponse({'error': 'Invalid request method'})
