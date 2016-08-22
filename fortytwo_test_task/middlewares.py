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
        if not request.user.is_authenticated():
            req.author = RequestKeeperModel.\
                            _meta.get_field('author').get_default()
        req.save()
        return response
