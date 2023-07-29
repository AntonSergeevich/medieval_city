from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import IndexPage, Person, Servant, MedieVallPage
from .forms import AddForm, AddFormServant
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(ListView):
    model = IndexPage
    template_name = 'medieval/index.html'
    context_object_name = 'index'

    @staticmethod
    def resume():
        return IndexPage.objects.first()




class MediaValView(ListView):
    model = MedieVallPage
    template_name = 'medieval/medie.html'
    @staticmethod
    def persons():
        return Person.objects.all()

    @staticmethod
    def servants():
        return Servant.objects.all()

class AddPersonView(LoginRequiredMixin, CreateView):
    template_name = 'medieval/add.html'
    form_class = AddForm
    success_url = '/medie/'
    permission_required = ('medieval.add_person')


class PersonUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'medieval/add.html'
    form_class = AddForm
    success_url = '/medie/'
    permission_required = ('medieval.change_person')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Person.objects.get(pk=id)


class PersonDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'medieval/delete.html'
    queryset = Person.objects.all
    success_url = '/medie/'
    permission_required = ('medieval.delete_person')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Person.objects.get(pk=id)


class AddServantView(LoginRequiredMixin,CreateView):
    template_name = 'medieval/add_servant.html'
    form_class = AddFormServant
    success_url = '/medie/'
    permission_required = ('medieval.add_servant')

class ServantUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'medieval/add_servant.html'
    form_class = AddFormServant
    success_url = '/medie/'
    permission_required = ('medieval.change_servant')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Servant.objects.get(pk=id)

class ServantDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'medieval/delete_servant.html'
    queryset = Servant.objects.all
    success_url = '/medie/'
    permissiom_required = ('mediaval.delete_servant')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Servant.objects.get(pk=id)

