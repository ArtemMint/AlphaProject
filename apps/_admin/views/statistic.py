from django.shortcuts import render
from django.views import generic


class AdminStatisticView(generic.View):
    template_name = 'admin/statistic.html'

    def get(self, request):
        return render(
            self.request,
            self.template_name,
            {},
        )
