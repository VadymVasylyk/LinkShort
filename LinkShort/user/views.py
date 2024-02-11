from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import UserRegForm, UserEditForm, LinkAddForm
from .models import Links


def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserEditForm()
    return render(request, 'user/profile.html', {'form': form})


class LinksView(CreateView):
    model = Links
    template_name = 'user/links.html'
    form_class = LinkAddForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        if Links.objects.filter(short=form.cleaned_data['short']).exists():
            messages.error(self.request, 'Link with such short name already exist, try other name')
            print(messages)
            return redirect('links')

        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx=super(LinksView, self).get_context_data(**kwargs)
        user_links = Links.objects.filter(user = self.request.user)
        ctx['links'] = user_links
        ctx['messages'] = messages.get_messages(self.request)
        return ctx
