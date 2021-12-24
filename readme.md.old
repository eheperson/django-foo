# djangorestframework-foo
test learned skills on django rest framework


# to test our api :

We can test our API using curl or httpie. Httpie is a user friendly http client that's written in Python. Let's install that.

```
# To install httpie
$ pip install httpie
```

```
# to test our api
$ http http://127.0.0.1:8000/snippets/
# or
$ curl http://127.0.0.18000/ehe -H 'Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR9eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6MDIyfQ.SflKxwRJSMeKKF2QT
```

```
curl http://127.0.0.1:8000/hello/ -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQzODI4NDMxLCJqdGkiOiI3ZjU5OTdiNzE1MGQ0NjU3OWRjMmI0OTE2NzA5N2U3YiIsInVzZXJfaWQiOjF9.Ju70kdcaHKn1Qaz8H42zrOYk0Jx9kIckTn9Xx7vhikY'

xxxxx.yyyyy.zzzzz = header.payload.signature

or 

header=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
payload=eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQzODI4NDMxLCJqdGkiOiI3ZjU5OTdiNzE1MGQ0NjU3OWRjMmI0OTE2NzA5N2U3YiIsInVzZXJfaWQiOjF9
signature=Ju70kdcaHKn1Qaz8H42zrOYk0Jx9kIckTn9Xx7vhikY

This information is encoded using Base64. If we decode, we will see something like this:

{
  "typ": "JWT",
  "alg": "HS256"
}

{
  "token_type": "access",
  "exp": 1543828431,
  "jti": "7f5997b7150d46579dc2b49167097e7b",
  "user_id": 1
}
reference : https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html#refresh-token

# To encryprt a token : https://jwt.io/

# to test access token via curl : 
$ curl -H "Authorization : Baearer <access_token>" <target_url_adress>

# to test refresh token via curl : 
$ curl -X POST <refresh_token_url_adress> -d "refresh=<refresh_token>"
# it will return new access token
```