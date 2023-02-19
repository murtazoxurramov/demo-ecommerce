from .base import *
from decouple import config
env_type = config('ENV_TYPE')

if env_type == 'production':
    from .production import *
elif env_type == 'development':
    from .local import *
