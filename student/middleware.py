import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None
        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('process_view: {:.2f}s'.format(costed))
        return response

    def process_template_response(self, request, response):
        return resposne

    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print('request_to response cost: {:.2f}s'.format(costed))
        return response