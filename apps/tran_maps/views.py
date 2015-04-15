from django.shortcuts import render
from django.views import generic

# Create your views here.


class MainView(generic.TemplateView):
    """Loads the main page."""
    template_name = 'tran_maps/main.html'


class OneNorth(generic.TemplateView):
    """Loads the Route 1 North Page"""
    template_name = 'tran_maps/onenorth.html'


class OneSouth(generic.TemplateView):
    """Loads the Route 1 South Page"""
    template_name = 'tran_maps/onesouth.html'


class Two(generic.TemplateView):
    """Loads the Route 2 Page"""
    template_name = 'tran_maps/two.html'


class Three(generic.TemplateView):
    """Loads the Route 3 Page"""
    template_name = 'tran_maps/three.html'


class Four(generic.TemplateView):
    """Loads the Route 4 Page"""
    template_name = 'tran_maps/four.html'


class FiveA(generic.TemplateView):
    """Loads the Route 5 A Page"""
    template_name = 'tran_maps/fivea.html'


class FiveB(generic.TemplateView):
    """Loads the Route 5 B Page"""
    template_name = 'tran_maps/fiveb.html'


class Six(generic.TemplateView):
    """Loads the Route 6 Page"""
    template_name = 'tran_maps/six.html'


class AllRoutes(generic.TemplateView):
    """Loads All the Routes on one Page"""
    template_name = 'tran_maps/all_routes.html'