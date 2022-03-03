from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader

from basics.models import Dummy

# Create your views here.
def funcView_ello(request):
    return HttpResponse("ello from simple function based view !")

def funcView_query(request):
    """
        Writing a view that actually do something
    """
    latest_dummies_list = Dummy.objects.order_by('-published_date')
    output = ' - '.join([q.bullshit for q in latest_dummies_list])
    return HttpResponse(output)

def dummy_index(request):
    """
        index page with template example
    """
    latest_dummies_list = Dummy.objects.order_by('-published_date')
    template = loader.get_template('basics/index.html')
    context = {
        'latest_dummies_list': latest_dummies_list,
    }
    return HttpResponse(template.render(context, request))
    #
    # A shortcut : render()
    #
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    #
    # we no longer need to import 'loader' and 'HttpResponse' 

def simple_detail(request, dummy_id):
    return HttpResponse("You're looking at question %s." % dummy_id)

def detail(request, dummy_id):
    """
        Example to raising 404 error
    """
    try:
        dummy = Dummy.objects.get(pk=dummy_id)
    except Dummy.DoesNotExist:
        raise Http404("Bullshit does not exist")
        #  raise the Http404 exception if a question with the requested ID doesn’t exist.
    return render(request, 'basics/detail.html', {'dummy': dummy})
    #
    # A shortcut: get_object_or_404()
    # question = get_object_or_404(Dummy, pk=dummy_id)
    # return render(request, 'basics/detail.html', {'dummy': dummy})