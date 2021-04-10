'Some utility functions for the Main module'

from functools import wraps
from typing import Any, Callable, Optional
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse

from django.template.response import TemplateResponse


class RenderData:
    '''
    A class to store data about a template to be rendered
    Stores:
    - context
    '''

    def __init__(self, *args, context=None) -> None:
        self.context = context or {}
        for arg in args:
            self += arg

    def dict(self):
        return {'context': self.context}

    def __add__(self, other):
        if isinstance(other, RenderData):
            context = self.context.copy()
            context.update(other.context)
            return RenderData(context=context)

    def __iadd__(self, other):
        result = self + other
        if isinstance(result, RenderData):
            self.context = result.context
        return self


class Context(RenderData):
    def __init__(self, **context) -> None:
        super().__init__(context=context)


class Title(Context):
    def __init__(self, title) -> None:
        super().__init__(title=title)
        self.__title = title

    def __str__(self) -> str:
        return f'{self.__class__.__qualname__}(\'{self.__title}\')'


class Renders:
    '''A decorator to that makes the generic case of a view which renders a
    template simpler to implement
    '''

    def __init__(self, template_name: Optional[str] = None, **kwargs: Any):
        self.template_name = template_name or 'base.html'
        self.kwargs = kwargs

    def __call__(self, func: Callable[[WSGIRequest], RenderData]) -> \
            Callable[[WSGIRequest], HttpResponse]:
        @wraps(func)
        def wrapper(request: WSGIRequest) -> HttpResponse:
            render_data = func(request)
            return TemplateResponse(
                request,
                self.template_name,
                **render_data.dict(),
                **self.kwargs
            )
        return wrapper


class View:
    'A class to make creating static views easy'

    #pylint: disable=keyword-arg-before-vararg
    def __init__(self,
        template_name: Optional[str] = None,
        *render_data_args, **render_data_kwargs
    ):
        self.template_name = template_name
        self.render_data = RenderData(*render_data_args, **render_data_kwargs)

    def __call__(self, request: WSGIRequest) -> HttpResponse:
        return TemplateResponse(
            request,
            self.template_name,
            **self.render_data.dict()
        )
