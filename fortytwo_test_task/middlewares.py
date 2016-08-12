from apps.hello.models import RequestKeeperModel


class RequestKeeperMiddleware(object):
    def process_response(self, request, response):
        if not request.is_ajax():
            if request.user.is_authenticated():
                req = RequestKeeperModel(method=request.method,
                                        name=request.path,
                                        status=response.status_code,
                                        author=request.user.username)
            else:
                req = RequestKeeperModel(method=request.method,
                                        name=request.path,
                                        status=response.status_code)
            req.save()
        return response
