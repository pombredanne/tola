from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from models import ProjectProposal
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ProjectProposalForm
from django.utils import timezone


class ProjectProposalList(ListView):

    model = ProjectProposal

    def get_context_data(self, **kwargs):
        context = super(ProjectProposalList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProjectProposalCreate(CreateView):
    """
    Project Proposal Form
    """

    model = ProjectProposal

    def form_invalid(self, form):

        messages.error(self.request, 'Invalid Form', fail_silently=False)

        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):

        form.save()

        return HttpResponseRedirect('/programdb/success')

    form_class = ProjectProposalForm


class ProjectProposalUpdate(UpdateView):
    """
    Project Proposal Form
    """

    model = ProjectProposal

    def form_invalid(self, form):

        messages.error(self.request, 'Invalid Form', fail_silently=False)

        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):

        form.save()

        return HttpResponseRedirect('/programdb/success')

    form_class = ProjectProposalForm


class ProjectProposalDelete(DeleteView):
    """
    Project Proposal Form
    """

    model = ProjectProposal

    def form_invalid(self, form):

        messages.error(self.request, 'Invalid Form', fail_silently=False)

        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):

        form.save()

        return HttpResponseRedirect('/programdb/success')

    form_class = ProjectProposalForm
