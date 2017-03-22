#-*- coding: utf-8 -*-

def clip(text, max_len=80):
    """
    return the text after removing 공백
    :param text:
    :param max_len:
    :return:
    """

    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


"""
▶ python -i clip.py
>>> clip.__defaults__
(80,)
>>> clip.__code__
<code object clip at 0x105f2d780, file "clip.py", line 3>
>>> clip.__code__.co_varnames
('text', 'max_len', 'end', 'space_before', 'space_after')
>>> clip.__code__.co_argcount
2
"""


from inspect import signature
"""
>>> from inspect import signature
>>> sig = signature(clip)
>>> sig
<Signature (text, max_len=80)>
>>> str(sig)
'(text, max_len=80)'
>>> sig.parameters
mappingproxy(OrderedDict([('text', <Parameter "text">), ('max_len', <Parameter "max_len=80">)]))
>>> for name, param in sig.parameters.items():
...     print(param.kind, ':', name, '=', param.default)
...
POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
POSITIONAL_OR_KEYWORD : max_len = 80
"""



"""
>>> from tag import tag
>>> from clip import clip
>>> import inspect
>>> sig = inspect.signature(tag)
>>> my_tag = {"name": 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
>>> bound_args = sig.bind(**my_tag)
>>> bound_args
<BoundArguments (name='img', cls='framed', attrs={'src': 'sunset.jpg', 'title': 'Sunset Boulevard'})>
>>> for name, value in bound_args.arguments.items():
...     print(name, '=', value)
...
name = img
cls = framed
attrs = {'src': 'sunset.jpg', 'title': 'Sunset Boulevard'}
>>> del my_tag['name']
>>> bound_args = sig.bind(**my_tag)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/selo/.pyenv/versions/3.5.0/lib/python3.5/inspect.py", line 2920, in bind
    return args[0]._bind(args[1:], kwargs)
  File "/Users/selo/.pyenv/versions/3.5.0/lib/python3.5/inspect.py", line 2835, in _bind
    raise TypeError(msg) from None
TypeError: missing a required argument: 'name'
"""