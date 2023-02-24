
import logging
from django.http import HttpResponse

from shop import settings

logger = logging.getLogger(__name__)


def index(request):
    if request.GET.get("param"):
        logger.info(f'My custom var = {settings.MY_CUSTOM_VARIABLE}')
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Shop index view")