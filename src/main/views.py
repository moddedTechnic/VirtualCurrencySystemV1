from functools import wraps
from typing import Callable
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse

from django.shortcuts import render


class RenderData:
    def __init__(self, *, context=None) -> None:
        self.context = context or {}

    def dict(self):
        return {'context': self.context}

    def __add__(self, other):
        if isinstance(other, RenderData):
            context = self.context.copy()
            context.update(other.context)
            return RenderData(context=context)


class Context(RenderData):
    def __init__(self, **context) -> None:
        super().__init__(context=context)


class Title(Context):
    def __init__(self, title) -> None:
        super().__init__(title=title)


def renders(template_name: str) -> Callable[
        [Callable[[WSGIRequest], RenderData]],
        Callable[[WSGIRequest], HttpResponse]
    ]:
    def wrapper(
            func: Callable[[WSGIRequest], RenderData]
        ) -> Callable[[WSGIRequest], HttpResponse]:
        @wraps(func)
        def wrapped(request: WSGIRequest) -> HttpResponse:
            render_data = func(request)
            render_data += Context(request=request, user=request.user)
            return render(
                request,
                template_name=template_name,
                **render_data.dict()
            )
        return wrapped
    return wrapper

# Create your views here.


@renders('index.html')
def index(request: WSGIRequest) -> Title:
    del request  # unused
    return Title('Hello world')


@renders('about.html')
def about(request: WSGIRequest) -> Title:
    del request  # unused
    return Title('About')
