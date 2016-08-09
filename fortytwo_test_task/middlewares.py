from apps.hello.models import RequestKeeperModel


class RequestKeeperMiddleware():
    def process_request(self, request):
        is_utility_request = '/requests/fetching' in request.get_full_path()
        if not is_utility_request:
            if request.user.is_authenticated():
                # set current username into author's field if user is authenticated
                RequestKeeperModel.objects.create(
                    path=request.get_full_path(),
                    method=request.method,
                    author=request.user.username
                )
            else:
                # set default author value if user isn't authenticated
                RequestKeeperModel.objects.create(
                    path=request.get_full_path(),
                    method=request.method
                )
