from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import BugReportForm, FeatureRequestForm
from .models import BugReport, FeatureRequest


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


class BugListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'
    context_object_name = "bug_list"


class FeatureRequestListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'
    context_object_name = "feature_list"


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'


class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_id_detail.html'
    context_object_name = 'feature'


class BugCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control/bug_list')

    def from_valid(self, form):
        form.instance.project = get_object_or_404(BugReport, pk=self.kwargs['bug_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('quality_control:bug_list')


class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'

    def from_valid(self, form):
        form.instance.project = get_object_or_404(FeatureRequest, pk=self.kwargs['feature_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('quality_control:feature_list')


class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_list')


class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:feature_list')


class BugDeleteView(DeleteView):
    model = BugReport
    template_name = 'quality_control/bug_confirm_delete.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_list')
    context_object_name = 'bug'


class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:feature_list')
    template_name = 'quality_control/feature_confirm_delete.html'
    context_object_name = 'feature'

# def index(request):
#     bug_list_url = reverse('quality_control:bug_list')
#     feature_list_url = reverse('quality_control:feature_list')
#     html = f"<h1> Система контроля качества </h1> " \
#            f"<a href='{bug_list_url}'> Список всех багов"   \
#            f"<br> <a href='{feature_list_url}'> Запросы на улучшение"
#     return HttpResponse(html)

# def bug_list(request):
#     return HttpResponse('<h1>Список отчетов об ошибках</h1>')
#
# def feature_list(request):
#     return HttpResponse('<h1>Список запросов на улучшение</h1>')
#
# def feature_id_detail(request, feature_id):
#     return HttpResponse(f'Детали улучшения {feature_id}')
#
# def bug_detail(request, bug_id):
#     return HttpResponse(f'Детали бага {bug_id}')
#
# def bug_list(request):
#     bugs = BugReport.objects.all()
#     bugs_html = '<h1> Список ошибок </h1><ul>'
#     for bug in bugs:
#         bugs_html += f'<li><a href="{bug.id}/">{bug.title} | Status:{bug.status}</a></li>'
#     bugs_html += "</ul>"
#     return HttpResponse(bugs_html)

# def bug_list(request):
#     bug = BugReport.objects.all()
#     return render(request, 'quality_control/bug_list.html', {'bug_list': bug})
#
#
# def feature_list(request):
#     features = FeatureRequest.objects.all()
#     features_html = '<h1> Список запросов на улучшение </h1><ul>'
#     for feature in features:
#         features_html += f'<li><a href="{feature.id}/">{feature.title} | Status:{feature.status}</a></li>'
#     features_html += "</ul>"
#     return HttpResponse(features_html)
#
# def bug_detail(request, bug_id):
#    bug = get_object_or_404(BugReport, id=bug_id)
#    response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>'
#    return HttpResponse(response_html)

# def feature_id_detail(request, feature_id):
#    feature = get_object_or_404(FeatureRequest, id=feature_id)
#    response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p>'
#    return HttpResponse(response_html)

# def feature_list(request):
#     features = FeatureRequest.objects.all()
#     return render(request, 'quality_control/feature_list.html', {'feature_list': features})
#
# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#          bug_list_url = reverse('quality_control:bug_list')
#          feature_list_url = reverse('quality_control:feature_list')
#          html = f"<h1>Система контроля качества</h1> " \
#                   f"<a href='{bug_list_url}'> Список всех багов"  \
#                   f"<br> <a href='{feature_list_url}'> Запросы на улучшение"
#         return render(request, 'quality_control/index.html')

# class BugListView(ListView):
#     model = BugReport
#
#     def get(self, request,  *args, **kwargs):
#         bugs = self.get_queryset()
#         bugs_html = '<h1>Список ошибок</h1><ul>'
#         for bug in bugs:
#             bugs_html += f'<li><a href="{bug.id}/">{bug.title} | Status:{bug.status}</a></li>'
#         bugs_html += "</ul>"
#         return HttpResponse(bugs_html)
#
# class FeatureRequestListView(ListView):
#     model = FeatureRequest
#
#     def get(self, request, *args, **kwargs):
#         features = self.get_queryset()
#         features_html = '<h1>Список запросов на улучшение</h1><ul>'
#         for feature in features:
#             features_html += f'<li><a href="{feature.id}/">{feature.title} | Status:{feature.status}</a></li>'
#         features_html += "</ul>"
#         return HttpResponse(features_html)
#
# class BugDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         bug = self.object
#         response_html = f'<h1>{bug.title}</h1>'\
#                         f'<p>Related project: {bug.project.name}</p>' \
#                         f'<p>Related task: {bug.task.name} | Related task status: {bug.task.status}</p>' \
#                         f'<p>Status: {bug.status}</p>' \
#                         f'<p>Priority: {bug.priority}</p>' \
#                         f'<p>Description: {bug.description}</p>'
#         return HttpResponse(response_html)
#
# class FeatureRequestDetailView(DetailView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_id'
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         feature = self.object
#         response_html = f'<h1>{feature.title}</h1>' \
#                         f'<p>Related project: {feature.project.name}</p>' \
#                         f'<p>Related task: {feature.task.name} Related task status: {feature.task.status}</p>' \
#                         f'<p>Status: {feature.status}</p>' \
#                         f'<p>Priority: {feature.priority}</p>'  \
#                         f'<p>Description: {feature.description}</p>'
#         return HttpResponse(response_html)

# def create_bug(request):
#     if request.method == 'POST':
#         form = BugReportForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('quality_control:bug_list')
#     else:
#         form = BugReportForm()
#     return render(request, 'quality_control/create_bug.html', {'form': form})

# def create_request(request):
#     if request.method == 'POST':
#         form = FeatureRequestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('quality_control:feature_list')
#     else:
#         form = FeatureRequestForm()
#     return render(request, 'quality_control/create_request.html', {'form': form})

# def update_bug(request, bug_id):
#     bug = get_object_or_404(BugReport, pk=bug_id)
#     if request.method == 'POST':
#         form = BugReportForm(request.POST, instance=bug)
#         if form.is_valid():
#             form.save()
#             return redirect('quality_control:bug_detail', bug_id=bug.id)
#     else:
#         form = BugReportForm(instance=bug)
#     return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})
#
# def update_feature(request, feature_id):
#     feature = get_object_or_404(FeatureRequest, pk=feature_id)
#     if request.method == 'POST':
#         form = FeatureRequestForm(request.POST, instance=feature)
#         if form.is_valid():
#             form.save()
#             return redirect('quality_control:feature_id_detail', feature_id=feature.id)
#     else:
#         form = FeatureRequestForm(instance=feature)
#     return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})
#
# def delete_bug(request, bug_id):
#     bug = get_object_or_404(BugReport, pk=bug_id)
#     bug.delete()
#     return redirect('quality_control:bug_list')
#
# def delete_feature(request, feature_id):
#     feature = get_object_or_404(FeatureRequest, pk=feature_id)
#     feature.delete()
#     return redirect('quality_control:feature_list')

