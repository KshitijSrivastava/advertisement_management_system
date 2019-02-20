from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from django.views.generic.edit import FormView
from blog.forms import PostForm,CommentForm,UserCreateForm
from . import forms
from django.utils import timezone
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView
from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

class SignUp(CreateView):
    """
    Signup of People
    """
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'


def index(request):
    return render(request,'blog/index.html')


class CreateView(CreateView):
    """
    Create Form
    Should be available to only the editor
    """
    template_name = 'blog/form_detail.html'
    form_class = PostForm




class PostUpdateView(UpdateView):
    """
    Update the Form:
    Should be available to only the Editor
    """
    template_name = 'blog/form_update.html'
    model = Post
    form_class = PostForm
    exclude = ['rev1_status','rev2_status','rev3_status']
    success_url = reverse_lazy('blog:rejected_post')

    def get_object(self):
        """
        To update the review for 1,2,3 to default 0 value
        """
        obj = Post.objects.get(pk=self.kwargs['pk'])
        obj.rev1_status = 0
        obj.rev2_status = 0
        obj.rev3_status = 0
        return obj


class AboutView(TemplateView):
    """
    About Page
    """
    template_name = 'blog/about.html'


class PostListView(ListView):
    """
    Return the list passed by all the Reviewers
    """
    template_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        """
        Returns a query which is is passed by Reviewer 3
        """
        if self.request.user.is_authenticated:
            return Post.objects.filter(rev3_status__exact=1).order_by('start_date')


class PostDetailView(DetailView):
    """
    Returns the Detailed view of the Posts
    """

    template_name = 'blog/post_detail.html'
    queryset = Post.objects.all()

    def post(self, request, *args, **kwargs):
        print(self.kwargs)
        print(request.POST)
        pk=self.kwargs['pk']
        print('Start of fxns')
        add_comment_to_post(request, pk)
        # print(reverse('blog:dashboard'))
        # print(redirect('blog:dashboard'))
        return redirect('blog:dashboard')


class PostRejectedListView(ListView):
    """
    Returns a list rejected by the reviewers
    """
    template_name = 'blog/post_rejected_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(rev1_status__exact=-1) | Post.objects.filter(rev2_status__exact=-1) | Post.objects.filter(rev3_status__exact=-1)


class PostReviewerListView(ListView):
    """
        Returns the Pending Post for each reviewer
    """
    template_name = 'blog/reviewer_list.html'
    model  = Post

    def get_queryset(self):
        "elif self.request.user.email == 'reviewer2@gmail.com':"
        # Gets the id of the reviewer and returns the pending ads

        if  self.request.user.email == 'reviewer1@gmail.com' :
            return Post.objects.filter(rev1_status__exact=0, rev2_status__exact=0, rev3_status__exact=0).order_by('start_date')
        elif self.request.user.email == 'reviewer2@gmail.com':
            return Post.objects.filter(rev1_status__exact=1,rev2_status__exact=0, rev3_status__exact=0).order_by('start_date')
        elif self.request.user.email == 'reviewer3@gmail.com':
            return Post.objects.filter(rev1_status__exact=1, rev2_status__exact=1, rev3_status__exact=0).order_by('start_date')
        else:
            print("User Not found")


def add_comment_to_post(request, pk):
    """
    Adds Comments to the Post
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # print(comment.author)
            # return redirect('blog:post_detail', pk=post.pk)

        user_email = request.user.email
        status = request.POST['btn_status']
        post_found = get_object_or_404(Post, id=pk)
        if user_email == 'reviewer1@gmail.com':
            post_found.rev1_status = status
            post_found.save()
        elif user_email == 'reviewer2@gmail.com':
            post_found.rev2_status = status
            post_found.save()
        elif user_email == 'reviewer3@gmail.com':
            post_found.rev3_status = status
            post_found.save()
        return redirect('blog:dashboard')


# class RejectView(View):
#
#     def post(self, request, *args, **kwargs):
#         user_email = kwargs['email']
#         post_id = kwargs['pk']
#         post_found = get_object_or_404(Post, id=post_id )
#         if user_email == 'reviewer1@gmail.com' :
#             post_found.rev1_status = -1
#             post_found.save()
#         elif user_email == 'reviewer2@gmail.com' :
#             post_found.rev2_status = -1
#             post_found.save()
#         elif user_email == 'reviewer3@gmail.com' :
#             post_found.rev3_status = -1
#             post_found.save()
#         return redirect('blog:post_list')
#         return None
#
#
# class AcceptView(View):
#
#     def post(self, request, *args, **kwargs):
#         user_email = kwargs['email']
#         post_id = kwargs['pk']
#         post_found = get_object_or_404(Post, id=post_id )
#         if user_email == 'reviewer1@gmail.com' :
#             post_found.rev1_status = 1
#             post_found.save()
#         elif user_email == 'reviewer2@gmail.com' :
#             post_found.rev2_status = 1
#             post_found.save()
#         elif user_email == 'reviewer3@gmail.com' :
#             post_found.rev3_status = 1
#             post_found.save()
#         else:
#             print('No user')
#         return redirect('blog:post_list')
