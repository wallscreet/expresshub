from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Upcoming
from .forms import PostForm, PostEditForm, CommentForm, AddUpcomingForm

'''
def home(request):
    return render(request, 'home.html', {})
'''


class UpcomingView(ListView):
    queryset = Upcoming.objects.filter(status=0).order_by('-startdate')
    template_name = 'upcoming.html'
    paginate_by = 5


class AddUpcomingView(CreateView):
    model = Upcoming
    form_class = AddUpcomingForm
    template_name = 'add_upcoming.html'


class HomeView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-createdate')
    # model = Post
    template_name = 'home.html'
    paginate_by = 10


class DraftView(ListView):
    queryset = Post.objects.filter(status=0).order_by('-createdate')
    template_name = 'drafts.html'
    paginate_by = 5


'''
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
'''


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'author', 'body')


class EditPostView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'edit_post.html'
    # fields = ['title', 'body', 'status']


def authorview(request, author):
    author_posts = Post.objects.filter(author=author)
    return render(request, 'author.html', {'author': author, 'author_posts': author_posts})


def post_detail(request, pk):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(status=1).order_by('-createdate')
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
