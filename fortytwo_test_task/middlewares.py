from apps.hello.models import RequestKeeperModel


class RequestKeeperMiddleware(object):
    def process_response(self, request, response):
        if request.is_ajax() or request.path.startswith("/static/"):
            return response

        req = RequestKeeperModel(
            method=request.method,
            name=request.path,
            status=response.status_code,
            author=request.user.username
        )
        if request.user.is_authenticated():
            req.author = request.user.username

        req.save()
        return response
