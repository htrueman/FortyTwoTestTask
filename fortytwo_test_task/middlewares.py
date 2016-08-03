from apps.hello.models import RequestKeeperModel


class RequestKeeperMiddleware():
    def process_request(self, request):
        is_utility_request = '/requests/fetching' in request.get_full_path()
        if not is_utility_request:
            RequestKeeperModel.objects.create(
                path=request.get_full_path(),
                method=request.method
            )
