# django-dump-http
Dump all Django HTTP requests and responses into files

To use it, copy the dump_http/ directory into your project and add

`'dump_http.dump_http.DumpHTTPMiddleware'` to `MIDDLEWARE` in your `settings.py`.

It creates the directory `dump.out` or directory specified by `DUMP_HTTP_DIR` in your `settings.py` if available,
and outputs dump files to this dir.

Request dump files end with `.1` and response dump files end with `.2`.

This project is subject to some bugs, which are difficult to workaround in Django.
