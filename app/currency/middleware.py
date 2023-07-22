from time import time
import currency.models as models


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start = time()
        response = self.get_response(request)
        end = time()

        print(f'View took to execute: {end - start}')

        models.RequestResponseLog.create(
            path=request.path,
            request_method=request.method,
            time=end - start
        )
        return response
