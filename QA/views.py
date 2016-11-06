from django.shortcuts import get_objects_or_404, render
from django.http import Http404

from adviseher.models import Question
# TODO: how to import models from main level?

def index(request):
    return HttpResponse("Hello, world. You're at the QA index.")
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'QA/detail.html', {'question': question})
#TODO: include answers too


