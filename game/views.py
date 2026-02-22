from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
import random
from .models import GameProblems
from .get_data import get_text

# Create your views here.
def game_menu(request):
    
    return render(request, 'menu.html')

def play_mode(request):
    problems = GameProblems.objects.all()


    # якщо перший вхід — створюємо score
    max_tasks_number = problems.count()

    if request.method == "GET":
        request.session['score'] = 0
        request.session['task'] = 1

        all_ids = list(GameProblems.objects.values_list('id', flat=True))
        random.shuffle(all_ids)
        request.session['remaining_ids'] = all_ids

        problem = None

        if all_ids:
            problem_id = all_ids.pop()
            request.session['remaining_ids'] = all_ids
            problem = GameProblems.objects.get(id=problem_id)

        return render(request, "check.html", {
            "score": 0,
            "problem": problem,
            "task": 1,
            "max_tasks_number": max_tasks_number,
        })
        
    # якщо користувач відповів
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "check":
            problem_id = request.POST.get("problem_id")
            problem = get_object_or_404(GameProblems, id=problem_id)
            expl = get_text.checking(card_title=problem.name, answear=request.POST.get("explaining"))

            grade = expl["grade"]
            explaining = expl["content"]

            request.session['score'] += int(grade)
            request.session['is_checked'] = True

            context = {
                'problem': problem,
                'score': request.session['score'],
                'explaining': explaining,
                'grade': grade,
                'task': request.session['task'],
                'max_tasks_number': max_tasks_number,
                'is_last': request.session['task'] == max_tasks_number,
            }

            return render(request, "next.html", context)
        elif action == "next":

            remaining_ids = request.session.get('remaining_ids', [])


            if not remaining_ids:   
                max_score = max_tasks_number * 10

                percentage = float(request.session['score'] / max_score)
                print(percentage)
                message = ""
                if percentage == 1:
                    message = "Perfect! You've got full marks!"
                elif percentage >= 0.8:
                    message = "Excellent work!"
                elif percentage >= 0.6:
                    message = "Good job!"
                else:
                    message = "Keep practicing to improve your score."
                print(message)
                context = {
                    'score': request.session['score'],
                    'is_last': True,
                    'max_score': max_score,
                    'message': message,
                }

                return render(request, "result.html", context)

            problem_id = remaining_ids.pop()
            request.session['remaining_ids'] = remaining_ids
            problem = GameProblems.objects.get(id=problem_id)

            request.session['task'] += 1
            request.session['is_checked'] = False

            context = {
                "score": request.session['score'],
                "problem": problem,
                'task': request.session['task'],
                'max_tasks_number': max_tasks_number,
            }

            return render(request, "check.html", context)


# def get_question(request):
#     problems = GameProblems.objects.all()

#     if not problems.exists():
#         return JsonResponse({"error": "No problems"}, status=404)

#     problem = random.choice(problems)

#     return JsonResponse({
#         "id": problem.id,
#         "name": problem.name,
#         "description": problem.description,
#     })
