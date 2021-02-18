from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView


from trains.models import Train
from trains.forms import TrainsForm

__all__ = ('home', 'TrainView', 'TrainDetailView', 'TrainCreateView', 'TrainUpdateView', 'TrainDeleteView')


def home(request, pk=None):
    qs = Train.objects.all()
    paginator = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, }
    return render(request, 'trains/home.html', context)


class TrainView(ListView):
    paginate_by = 4
    model = Train
    template_name = 'trains/home.html'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainsForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Город успешно создан"


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainsForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Поезд успешно отредактирован"


class TrainDeleteView(SuccessMessageMixin, DeleteView):
    model = Train
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('trains:home')

    # success_message = "Город успешно удален"

    def get(self, request, *args, **kwargs):
        messages.warning(request, 'Поезд удален')
        return self.post(request, *args, **kwargs)





