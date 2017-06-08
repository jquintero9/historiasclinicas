try:
    from .base import *
    from .local import *
    live = False
except ImportError:
    live = True

if live:
    from .production import *
    from .base import *
