from django.shortcuts import render

from db.models import Route


# Create your views here.

def get_current_routs(request):
    route_list = []
    context = {
        'routs': Route.objects.filter(active=True),
    }
    return render(request, 'app/current_route.html', context)

class UserView(APIView):

    def update_profile(self, request):
        pass