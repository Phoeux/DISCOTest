import logging
from datetime import datetime
import time


logger = logging.getLogger(__name__)


class LogErrorsMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self._get_response(request)
        duration = time.time() - start_time
        if duration >= 1:
            logger.warning(f'request takes too much time {duration}')
        return response
