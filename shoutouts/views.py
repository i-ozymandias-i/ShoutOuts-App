from django.shortcuts import render, get_object_or_404
from .models import ShoutOut

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
