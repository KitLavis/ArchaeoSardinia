from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseServerError
from .models import Post, Comment
from .forms import CommentForm


def Home(request):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of blog.Post
    ``latest_news``
        The latest instance of blog.Post
    ``post_list``
        queryset excluding latest_news
    ``paginator``
        Number of posts per page excluding
        latest_news
    """
    queryset = Post.objects.filter(status=1)
    if not queryset.exists():
        return HttpResponseServerError()
    latest_news = queryset.latest()
    post_list = queryset.exclude(id=latest_news.id)

    p = Paginator(post_list, 4)
    page = request.GET.get("page")
    p_posts = p.get_page(page)

    return render(
        request,
        template_name="index.html",
        context={
            "latest_news": latest_news,
            "post_list": post_list,
            "p_posts": p_posts,
        }
    )


class PostDetail(View):
    """
    Displays an individul instance of blog.Post
    in detail
    """
    def get(self, request, slug):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("created_on")
        comment_count = post.comments.count()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_count": comment_count,
                "commented": False,
                "liked": liked,
                "comment_form": comment_form
            },
        )

    def post(self, request, slug):
        """
        Function post within PostDetail allows for
        a comment to be added
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("created_on")

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = self.request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Success! Thanks for contributing!'
                )

            comment_form = CommentForm()

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_edit(request, slug, comment_id):
    """
    Function allows for an individual comment to be edited
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
    if comment_form.is_valid() and comment.name == request.user:
        comment = comment_form.save(commit=False)
        comment.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Comment updated successfully'
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'Error updating comment! Please try again.'
            )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Function allows for an individual comment to be deleted
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.name == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class Like(View):
    """
    Class based view allows for a post to be liked by
    a user
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
