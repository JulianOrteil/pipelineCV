# -*- coding: utf-8 -*-

"""Configurations persistent for the entire application."""


from dataclasses import dataclass, field, is_dataclass


__all__ = ['LoggingConfig']


def nested_dataclass(
    *args,
    init=True,
    repr=True,  # pylint: disable=redefined-builtin
    eq=True,  # pylint: disable=invalid-name
    order=False,
    unsafe_hash=False,
    frozen=False
):
    """Decorator for dataclasses that have nested dataclasses.

    Reconfigures the `__init__` function of the decorated class to parse
    nested `dict`s to initialize any nested dataclasses it may have.

    Note:
        All kwargs are sent to `dataclass`. Refer to its documentation
        for further info.

    Returns:
        wrapped_class (`class`):
            A class with a reconfigured `__init__` function.
    """

    def wrapper(cls):
        cls = dataclass(
            cls,
            init=init,
            repr=repr,
            eq=eq,
            order=order,
            unsafe_hash=unsafe_hash,
            frozen=frozen
        )
        original_init = cls.__init__

        def __init__(self, *args, **kwargs):
            for name, value in kwargs.items():
                field_type = cls.__annotations__.get(name, None)
                if is_dataclass(field_type) and isinstance(value, dict):
                    # Create the nested dataclass
                    new_obj = field_type(**value)
                    kwargs[name] = new_obj
            original_init(self, *args, **kwargs)

        cls.__init__ = __init__
        return cls

    return wrapper(args[0]) if args else wrapper


@nested_dataclass(frozen=True)
class _LoggingConfig():

    @dataclass(frozen=True)
    class Handler:

        enabled: bool = True
        location: str = '{root}\\pipelinecv\\logs'
        level: str = 'INFO'

    root: str = 'TEMP'
    stderr = Handler()
    file = Handler()
    gui = Handler()

LoggingConfig = _LoggingConfig()
