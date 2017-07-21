# django-dump-http
Dump all Django HTTP requests and responses into files

To use it, copy the dump_http/ directory into your project and add

`'dump_http.dump_http.DumpHTTPMiddleware'` to `MIDDLEWARE` in your `settings.py`.

It creates the directory `dump.out` or directory specified by `DUMP_HTTP_DIR` in your `settings.py` if available,
and outputs dump files to this dir.

Request dump files end with `.1` and response dump files end with `.2`.

The format of file names is:

`T1-T2-S-K` where `T1` is the server start time (in seconds since the epoch), `T2` is the moment of the dump. `S` is zero-based serial number of the HTTP connection and `K` is `1` for requests and `2` for corresponding responses.

This project is subject to some bugs, which are difficult to workaround in Django.
