
import logging
from django.http import HttpResponse

from shop import settings

logger = logging.getLogger(__name__)


# def index(request):
#     if request.GET.get("param"):
#         logger.info(f'My custom var = {settings.MY_CUSTOM_VARIABLE}')
#         logger.info(f"My param = {request.GET.get('param')}")
#         logger.info(f'Debug type = {type(settings.DEBUG)}')
#         logger.info(f'Debug = {settings.DEBUG}')
#     if settings.FIRST_SETTINGS == 'second':
#         logger.info(f'Settings number = {settings.SECOND_SETTINGS}')
#     if settings.FIRST_SETTINGS == 'third':
#         logger.info(f'Ssttings number = {settings.THIRD_SETTINGS}')
#     return HttpResponse("Shop index view")

def index(request):
    if request.GET.get('products'):
        logger.info(f'')