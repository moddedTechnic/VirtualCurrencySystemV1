
class Result:
    'Stores a result, either ok or error'

    def __init__(self, *, ok=None, err=None):
        self.ok = ok
        self.err = err

    def __bool__(self):
        return self.err is None

    def __repr__(self):
        return f'{self.__class__.__qualname__}(ok={self.ok}, err={self.err})'
    
    def __str__(self):
        return f'{self.__class__.__name__}(' + (f'ok={self.ok}' if self else f'err={self.err}') + ')'

    def unwrap(self):
        if self:
            return self.ok
        raise self.err

    def wrap_ok(self, ok_class, *args, **kwargs):
        if self:
            self.ok = ok_class(self.ok, *args, **kwargs)
        return self

    def wrap_err(self, err_class, *args, **kwargs):
        if not self:
            self.err = err_class(self.err, *args, **kwargs)
        return self
