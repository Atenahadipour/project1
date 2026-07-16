from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pickle
import os
from django.conf import settings

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>پیش‌بینی هوشمند قیمت مسکن</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght=300;400;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Vazirmatn', sans-serif; }
        </style>
    </head>
    <body class="bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen flex items-center justify-center p-6">
        <div class="bg-white rounded-2xl shadow-xl p-8 max-w-md w-full border border-indigo-50">
            <div class="text-center mb-8">
                <h1 class="text-2xl font-bold text-indigo-900 mb-2">هوش مصنوعی پیش‌بینی قیمت خانه</h1>
                <p class="text-sm text-gray-500">مشخصات خانه را وارد کنید تا قیمت تقریبی محاسبه شود</p>
            </div>

            <div class="space-y-5">
                <div>
                    <label class="block text-sm font-semibold text-gray-700 mb-2">متراژ خانه (متر مربع)</label>
                    <input type="number" id="area" placeholder="مثلاً 100" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition text-left">
                </div>
                
                <div>
                    <label class="block text-sm font-semibold text-gray-700 mb-2">تعداد اتاق خواب</label>
                    <input type="number" id="room" placeholder="مثلاً 2" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition text-left">
                </div>

                <button onclick="getPrediction()" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-indigo-200 flex items-center justify-center space-x-2">
                    <span>پیش‌بینی قیمت</span>
                </button>
            </div>

            <div id="resultContainer" class="mt-8 p-4 rounded-xl hidden transition-all duration-300">
                <p class="text-xs text-gray-500 text-center mb-1" id="resultLabel">قیمت پیش‌بینی شده:</p>
                <p class="text-xl font-bold text-center" id="resultPrice"></p>
            </div>
        </div>

        <script>
            async function getPrediction() {
                const area = document.getElementById('area').value;
                const room = document.getElementById('room').value;
                const resultContainer = document.getElementById('resultContainer');
                const resultPrice = document.getElementById('resultPrice');
                const resultLabel = document.getElementById('resultLabel');

                if (!area || !room) {
                    alert('لطفاً هم متراژ و هم تعداد اتاق را وارد کنید.');
                    return;
                }

                try {
                    const response = await fetch('/api/predict/', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ Area: area, Room: room })
                    });
                    
                    const data = await response.json();
                    
                    resultContainer.classList.remove('hidden', 'bg-red-50', 'bg-emerald-50');
if (data.status === 'success') {
                        resultContainer.classList.add('bg-emerald-50');
                        resultLabel.innerText = "قیمت پیش‌بینی شده:";
                        resultPrice.className = "text-xl font-bold text-center text-emerald-700";
                        const formattedPrice = Number(data.predicted_price_toman).toLocaleString('fa-IR');
                        resultPrice.innerText = formattedPrice + " تومان";
                    } else {
                        resultContainer.classList.add('bg-red-50');
                        resultLabel.innerText = "خطا:";
                        resultPrice.className = "text-sm font-semibold text-center text-red-600";
                        resultPrice.innerText = data.message;
                    }
                } catch (error) {
                    resultContainer.classList.remove('hidden');
                    resultContainer.classList.add('bg-red-50');
                    resultPrice.innerText = 'ارتباط با سرور برقرار نشد.';
                }
            }
        </script>
    </body>
    </html>
    """
    return HttpResponse(html_content)

@api_view(['POST'])
def predict_price(request):
    try:
        area = request.data.get('Area')
        room = request.data.get('Room')
        
        if area is None or room is None:
            return Response({
                'status': 'error', 
                'message': 'لطفاً مقادیر Area (متراژ) و Room (تعداد اتاق) را ارسال کنید.'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        model_path = os.path.join(settings.BASE_DIR, 'house_model.pkl')
        
        if not os.path.exists(model_path):
            return Response({
                'status': 'error', 
                'message': 'فایل مدل پیدا نشد. ابتدا فایل پایتون مدل (train_model.py) را اجرا کنید.'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        
        prediction = model.predict([[float(area), int(room)]])
        predicted_price = round(prediction[0], 2)
        
        return Response({
            'status': 'success',
            'predicted_price_toman': predicted_price
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'status': 'error', 
            'message': f'خطایی رخ داده است: {str(e)}'
        }, status=status.HTTP_400_BAD_REQUEST)