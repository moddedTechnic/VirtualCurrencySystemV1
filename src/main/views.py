from functools import wraps

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


def renders(template_name):
    def wrapper(func):
        @wraps(func)
        def wrapped(request):
            render_data = func(request)
            render_data += Context(request=request, user=request.user)
            return render(request, template_name=template_name, **render_data.dict())
        return wrapped
    return wrapper

# Create your views here.


@renders('index.html')
def index(request):
    del request  # unused
    return Title('Hello world')


@renders('about.html')
def about(request):
    del request  # unused
    return Title('About')
