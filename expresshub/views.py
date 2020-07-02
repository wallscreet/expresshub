from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from .forms import PostForm, PostEditForm, CommentForm, AddUpcomingForm, PostMForm, PostHForm, PostMEditForm, \
    PostHEditForm, HCommentForm, MCommentForm, PostM, PostH, LostFoundForm, LostFound, LostFoundEditForm, LFCommentForm
from .models import Post, Upcoming

'''
def home(request):
    return render(request, 'home.html', {})
'''


class UpcomingView(ListView):
    queryset = Upcoming.objects.filter(status=0)
    template_name = 'upcoming.html'
    paginate_by = 10


class AddUpcomingView(CreateView):
    model = Upcoming
    form_class = AddUpcomingForm
    template_name = 'add_upcoming.html'


class HomeView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-createdate')
    # model = Post
    template_name = 'home.html'
    paginate_by = 10


class MaintenanceView(ListView):
    queryset = PostM.objects.exclude(statusm=2).order_by('-createdatem')
    # model = Post
    template_name = 'maintenance.html'
    paginate_by = 10


class MaintenanceCompleteView(ListView):
    queryset = PostM.objects.filter(statusm=2).order_by('-createdatem')
    # model = Post
    template_name = 'maintenancecomp.html'
    paginate_by = 10


class HousekeepingView(ListView):
    queryset = PostH.objects.exclude(statush=2).order_by('-createdateh')
    # model = Post
    template_name = 'housekeeping.html'
    paginate_by = 10


class HousekeepingCompleteView(ListView):
    queryset = PostH.objects.filter(statush=2).order_by('-createdateh')
    # model = Post
    template_name = 'housekeepingcomp.html'
    paginate_by = 10


class LostFoundView(ListView):
    queryset = LostFound.objects.filter(status=0).order_by('-createdate')
    # model = LostFound
    template_name = 'lostfound.html'
    paginate_by = 10


class FoundView(ListView):
    queryset = LostFound.objects.filter(status=1).order_by('-createdate')
    # model = LostFound
    template_name = 'found.html'
    paginate_by = 10


class ClaimedView(ListView):
    queryset = LostFound.objects.filter(status=2).order_by('-createdate')
    # model = LostFound
    template_name = 'claimed.html'
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


class AddPostMView(CreateView):
    model = PostM
    form_class = PostMForm
    template_name = 'add_postm.html'
    # fields = '__all__'
    # fields = ('titlem', 'authorm', 'bodym')


class EditPostMView(UpdateView):
    model = PostM
    form_class = PostMEditForm
    template_name = 'edit_postm.html'
    # fields = ['titlem', 'bodym', 'statusm']


class AddLostFoundView(CreateView):
    model = LostFound
    form_class = LostFoundForm
    template_name = 'add_lostfound.html'
    # fields = '__all__'
    # fields = ('item', 'creator', 'description')


class EditLostFoundView(UpdateView):
    model = LostFound
    form_class = LostFoundEditForm
    template_name = 'edit_lostfound.html'
    # fields = ['item', 'description', 'status']


class AddPostHView(CreateView):
    model = PostH
    form_class = PostHForm
    template_name = 'add_posth.html'
    # fields = '__all__'
    # fields = ('titleh', 'authorh', 'bodyh')


class EditPostHView(UpdateView):
    model = PostH
    form_class = PostHEditForm
    template_name = 'edit_posth.html'
    # fields = ['titleh', 'bodyh', 'statush']


def authorview(request, author):
    author_posts = Post.objects.filter(author=author)
    return render(request, 'author.html', {'author': author, 'author_posts': author_posts})


def authormview(request, authorm):
    authorm_posts = PostM.objects.filter(authorm=authorm)
    return render(request, 'authorm.html', {'authorm': authorm, 'authorm_posts': authorm_posts})


def creatorview(request, creator):
    creator_posts = LostFound.objects.filter(creator=creator)
    return render(request, 'creator.html', {'creator': creator, 'creator_posts': creator_posts})


def authorhview(request, authorh):
    authorh_posts = PostH.objects.filter(authorh=authorh)
    return render(request, 'authorh.html', {'authorh': authorh, 'authorh_posts': authorh_posts})


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


def postm_detail(request, pk):
    template_name = 'postm_detail.html'
    postm = get_object_or_404(PostM, pk=pk)
    mcomments = postm.mcomments.order_by('-mcreatedate')
    new_mcomment = None
    # Comment posted
    if request.method == 'POST':
        mcomment_form = MCommentForm(data=request.POST)
        if mcomment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_mcomment = mcomment_form.save(commit=False)
            # Assign the current post to the comment
            new_mcomment.postm = postm
            # Save the comment to the database
            new_mcomment.save()
    else:
        mcomment_form = MCommentForm()

    return render(
        request,
        template_name,
        {
            "postm": postm,
            "mcomments": mcomments,
            "new_mcomment": new_mcomment,
            "mcomment_form": mcomment_form,
        },
    )


def posth_detail(request, pk):
    template_name = 'posth_detail.html'
    posth = get_object_or_404(PostH, pk=pk)
    hcomments = posth.hcomments.order_by('-hcreatedate')
    new_hcomment = None
    # Comment posted
    if request.method == 'POST':
        hcomment_form = HCommentForm(data=request.POST)
        if hcomment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_hcomment = hcomment_form.save(commit=False)
            # Assign the current post to the comment
            new_hcomment.posth = posth
            # Save the comment to the database
            new_hcomment.save()
    else:
        hcomment_form = HCommentForm()

    return render(
        request,
        template_name,
        {
            "posth": posth,
            "hcomments": hcomments,
            "new_hcomment": new_hcomment,
            "hcomment_form": hcomment_form,
        },
    )


def lostfound_detail(request, pk):
    template_name = 'lostfound_detail.html'
    lostfound = get_object_or_404(LostFound, pk=pk)
    lfcomments = lostfound.lfcomments.order_by('-createdate')
    new_lfcomment = None
    # Comment posted
    if request.method == 'POST':
        lfcomment_form = LFCommentForm(data=request.POST)
        if lfcomment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_lfcomment = lfcomment_form.save(commit=False)
            # Assign the current post to the comment
            new_lfcomment.lostfound = lostfound
            # Save the comment to the database
            new_lfcomment.save()
    else:
        lfcomment_form = LFCommentForm()

    return render(
        request,
        template_name,
        {
            "lostfound": lostfound,
            "lfcomments": lfcomments,
            "new_lfcomment": new_lfcomment,
            "lfcomment_form": lfcomment_form,
        },
    )