from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from together import Together
from ui_app.models import Book

client = Together(api_key="0cc12ec3ffb314230e652f3811891f3b94f9695c69e95dd14c6ffb5d0d6b0c07")

# Список ключевых слов, указывающих на запросы по книгам
BOOK_KEYWORDS = ['книга', 'автор', 'название', 'описание', 'книги']


@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").strip()

        if not user_message:
            return JsonResponse({"error": "Пустое сообщение"}, status=400)

        # Поиск книг по ключевым словам
        books = Book.objects.filter(
            title__icontains=user_message
        ) | Book.objects.filter(
            author__icontains=user_message
        ) | Book.objects.filter(
            description__icontains=user_message
        )

        if books.exists():
            recommendations = "\n".join([f"📖 {book.title} — {book.author}" for book in books[:5]])
            reply = f"Вот что я нашёл по запросу:\n{recommendations}"
        else:
            # AI-ответ, если книг не найдено
            response = client.chat.completions.create(
                model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
                messages=[{"role": "user", "content": user_message}]
            )
            reply = response.choices[0].message.content

        return JsonResponse({"response": reply})

    return JsonResponse({"error": "Только POST запросы"}, status=405)


def chatbot_page(request):
    return render(request, "chatbot/chat.html")
