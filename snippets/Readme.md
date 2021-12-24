#
# Prepare 

First we need to install our package requirements.

```
pip install django
pip install djangorestframework
pip install pygments  # We'll be using this for the code highlighting
```

Once that's done we can create an app that we'll use to create a simple Web API.

```
python manage.py startapp snippets
```

We'll need to add our new snippets app and the `rest_framework` app to `INSTALLED_APPS`.\
Let's edit the `core/settings.py` file:

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'snippets.apps.SnippetsConfig',
]
```

---

## Request Objects 

* REST framework introduces a `Request` object that extends the regular `HttpRequest`, and provides more flexible request parsing.
* The core functionality of the `Request` object is the `request.data` attribute, which is similar to `request.POST`, but more useful for working with Web APIs.

```
request.POST  # Only handles form data.  Only works for 'POST' method.
request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods
```

## Response Objects

* REST framework also introduces a Response object, which is a type of `TemplateResponse` that takes unrendered content and uses content negotiation to determine the correct content type to return to the client.

```
return Response(data)  # Renders to content type as requested by the client.
```

## Status Codes

* Using numeric `HTTP status codes` in your views doesn't always make for obvious reading, and it's easy to not notice if you get an error code wrong. 
* REST framework provides more explicit identifiers for each status code, such as `HTTP_400_BAD_REQUEST` in the status module. 
* It's a good idea to use these throughout rather than using numeric identifiers.

## Wrapping API Views

* REST framework provides two wrappers you can use to write API views.
  * The `@api_view` decorator for working with function based views.
  * The `APIView` class for working with class-based views.
  
> These wrappers provide a few bits of functionality such as making sure you receive `Request` instances in your view, and adding context to `Response` objects so that content negotiation can be performed.

> The wrappers also provide behaviour such as returning `405 Method Not Allowed` responses when appropriate, and handling any `ParseError` exceptions that occur when accessing `request.data` with malformed input.


---

# Important Points

* The `create()` and `update()` methods define how fully fledged instances are created or modified when calling `serializer.save()`.