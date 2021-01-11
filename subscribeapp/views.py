from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        # project.pk 를 get 방식으로 받아서 project.pk 가 있는 detail page로 되돌아 감
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        # 프로젝트가 없으면(404) 되돌아 가는 예외처
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        # 원래 구독되어있던 것인지 아닌지 확인
        subscription = Subscription.objects.filter(user=user, project=project)

        # 구독되어 있으면 삭제 후 다시 구독..? 없으면 구독 저장
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    # 가져올 게시글들 조
    # values_list : 받는 값들을 리스트화 시킨다
    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=projects)
        return article_list

