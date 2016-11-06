from django.shortcuts import get_object_or_404, render

from adviseher.models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the QA index.")
def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'QA/question_detail.html', {'question': question})
#TODO: include answers too


