from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import views

from _db import models


class HomeView(generic.TemplateView):
    """Render home page"""
    template_name = 'website/home.html'


class ContactView(generic.TemplateView):
    """Render home page"""
    template_name = 'website/contact.html'


class AboutView(generic.TemplateView):
    """Render home page"""
    template_name = 'website/about.html'
