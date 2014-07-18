from django.shortcuts import render, get_object_or_404
from .models import ShoutOut
from .forms import ShoutOutForm

from django.views.generic import ListView, DetailView, CreateView
from shoutouts.forms import ShoutOutForm
from braces.views import LoginRequiredMixin


class ShoutOutList(ListView):
    template_name = 'shoutouts/list.html'
    context_object_name = 'shoutouts'
    queryset = ShoutOut.objects.public()

class ShoutOutDetail(DetailView):
    template_name = 'shoutouts/detail.html'
    context_object_name = 'shoutout'
    model = ShoutOut

class ShoutOutCreate(LoginRequiredMixin,CreateView):
    template_name = 'shoutouts/create.html'
    model = ShoutOut
    form_class = ShoutOutForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.submitter = self.request.user
        self.object.save()
        return super(ShoutOutCreate, self).form_valid(form)

def shoutout_list(request):
    """List all public shootouts """
    return render(
        request,
        'shoutouts/list.html',
        {
            'shoutouts': ShoutOut.objects.public(),
        },
    )


def shoutout_detail(request, pk):
    """Display a shoutout"""
    shoutout = get_object_or_404(ShoutOut, pk=pk)
    return render(
          request,
        'shoutouts/detail.html',
        {
            'shoutout': shoutout,
        },
    )


# Create your views here.
