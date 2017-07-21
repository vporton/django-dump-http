import time

# WARNING: The order of headers, quoting, and probably lettercase is broken
def reconstruct_request_or_response(reqest_or_response):
    pass

start_time = int(time.time())

class DumpHTTPMiddleware(object):
    # One-time configuration and initialization.
    def __init__(self, get_response):
        self.get_response = get_response
        self.serial = 0

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        cur_time = int(time.time())
        base_name = "%d-%d-%d" % (start_time, cur_time, self.serial)

        self.serial += 1

        # Code to be executed for each request/response after
        # the view is called.

        return response