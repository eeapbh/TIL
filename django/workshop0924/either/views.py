from django.shortcuts import render, redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'either/index.html', context)

def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('either:detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'either/create_question.html', context)

def detail(request, question_pk):
    # 질문 title, pick_a, pick_b
    # 댓글이 보여야한다.
    # 현재 득표량 비교
    # 댓글로 투표(create_comment를 할수 잇어야한다)
    question = Question.objects.get(pk=question_pk)
    comments = question.comment_set.all()
    form = CommentForm()

    total_count = len(comments)
    pick_a_count = comments.filter(pick=True).count()


    context = {
        'question': question,
        'comments': comments,
        'form': form,
        'total_count':total_count,
        'pick_a_count':pick_a_count,
    }
    return render(request, 'either/detail.html', context)

def create_comment(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = question
            comment.save()
    return redirect('either:detail', question_pk)
