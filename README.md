# flask-psycopg2-starter

## Issues

If you run into permission issues like below,

```bash
$ make install
virtualenv venv
make: ./make-venv: Permission denied
make: *** [install] Error 1
$ chmod +x make-venv # should fix the issue
```

If you run into install `psycopg2` on macOS, refer to [this StackOverflow post](https://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa). Personally, I had to set following flags such that compiler can find `openssl`:

``` bash
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
```
