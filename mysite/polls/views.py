from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll

def index(request):
  latest_polls = Poll.objects.all().order_by('-pub_date')[:5]
  return render_to_response('polls/index.html', {'latest_poll_list':latest_polls})

def detail(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  return render_to_response('polls/detail.html', {'poll': p},
      context_instance=RequestContext(request))

def results(request, poll_id):
  return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  try:
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Re-display the poll voting form.
    return render_to_response('polls/detail.html', {
        'poll': p,
        'error_message': "You didn't select a valid choice."
        }, context_instance=RequestContext(request))
  else:
    selected_choice.votes +=1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
