from inspect import isfunction

from django.utils.decorators import method_decorator


class _cbv_decorate(object):
    def __init__(self, dec):
        self.dec = method_decorator(dec)

    def __call__(self, obj):
        obj.dispatch = self.dec(obj.dispatch)
        return obj


def patch_view_decorator(dec):
    def _conditional(view):
        if isfunction(view):
            return dec(view)

        return _cbv_decorate(dec)(view)

    return _conditional
