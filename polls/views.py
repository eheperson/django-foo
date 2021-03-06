from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic # using generic views of django


from .models import Question, Choice

# Create your views here.

# old 'index' view, uncommet to test and comment actual 'index' view
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# old 'index' view, uncommet to test and comment actual 'index' view
def index(request):
    """
        Write a view that actually do something
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index(request):
    """
        index with template example
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    # A shortcut : render()
    #
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    #
    # we no longer need to import 'loader' and 'HttpResponse' 

# --------------------------------------------------------------------------------------

# old 'detail' view, uncommet to test and comment actual 'detail' view
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
    """
        Example to raising 404 error
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
        #  raise the Http404 exception if a question with the requested ID doesn’t exist.
    return render(request, 'polls/detail.html', {'question': question})
    #
    # A shortcut: get_object_or_404()
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})

# --------------------------------------------------------------------------------------

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# This is almost exactly the same as the detail() view above. 
# The only difference is the template name
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# --------------------------------------------------------------------------------------

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# -----------------------------------------------------------------------------
        # USING GENERIC VIEWS
# -----------------------------------------------------------------------------
# By default, the DetailView generic view uses a template called "<app name>/<model name>_detail.html". 
# In our case, it would use the template "polls/question_detail.html".
# Similarly, the ListView generic view uses a default template called "<app name>/<model name>_list.html"; 
# we use template_name to tell ListView to use our existing "polls/index.html" template.
    # The template_name attribute is used to tell Django to use a specific template name instead of 
    # the autogenerated default template name.


# generic ListView : “display a list of objects” 
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


# generic DetailView : “display a detail page for a particular type of object.”
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))