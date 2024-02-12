from django.shortcuts import render
from blog.models import Post
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.views.decorators.http import require_POST


@require_POST
def post_comment(request,post_id):
    post = get_object_or_404(Post,
                            id=post_id,
                            status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        data = {
                 'post': post,
                 'form': form,
                 'comment': comment}
    return render(request, 'post/comment.html', context=data)  





def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page',1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)



    return render(request, 'post/list.html', {'posts' : posts })



def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                                  status=Post.Status.Published,
                                  slug = post,
                                  publish_year = year,
                                  publish_month = month,
                                  publish_day = day)

    commants = post.commants.filter(active=True)
    form = CommentForm()
    return render(request, 'post/detail.html', {'post': post,
                                                'commets': commets,
                                                'form': form})
