from openai import OpenAI
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST

client = OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com",
)

def index(request):
    return render(request, "index.html")

@require_POST
def generate(request):
    name     = request.POST.get("name", "").strip()
    category = request.POST.get("category", "").strip()
    features = request.POST.get("features", "").strip()
    tone     = request.POST.get("tone", "нейтральный")

    if not name or not features:
        return JsonResponse({"error": "Заполни название и характеристики"}, status=400)

    from .promts import build_prompt
    prompt = build_prompt(name, category, features, tone)

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  # DeepSeek-V3
            max_tokens=700,
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
        return JsonResponse({"result": result})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)