#
#
# Throttling is similar to permissions, 
# in that it determines if a request should be authorized. 
# Throttles indicate a temporary state, and are used to control 
# the rate of requests that clients can make to an API.
#
# As with permissions, multiple throttles may be used. 
# Your API might have a restrictive throttle for unauthenticated requests, 
# and a less restrictive throttle for authenticated requests.
#
# Another scenario where you might want to use multiple throttles would be 
# if you need to impose different constraints on different parts of the API, 
# due to some services being particularly resource-intensive.
#
# Multiple throttles can also be used if you want to impose both 
# burst throttling rates, and sustained throttling rates. For example, 
# you might want to limit a user to a maximum of 60 requests per minute, 
# and 1000 requests per day.
#
#

from rest_framework.throttling import (
    AnonRateThrottle, # restrict the user ip If there is an anonymous user
    SimpleRateThrottle,
    UserRateThrottle, # to restrict any user, logged in or anonymous, does not matters.
    ScopedRateThrottle,
)

class RegisterThrottle(SimpleRateThrottle):
    scope = 'registerthrottle' 
    # scope variable will be used in settings.py to set throttle restriction rate

    def get_cache_key(self, request, view):
        if request.user.is_authenticated or request.thod == 'GET':
            return None # restrict unauthorized access or POST request

        return self.cache_format % {
            'scope' : self.scope,
            'ident' : self.get_ident(request)
        }

class RegisterThrottleAnon(AnonRateThrottle):
    scope = 'registerthrottleAnon' 
    # scope variable will be used in settings.py to set throttle restriction rate

class RegisterThrottleAnon(UserRateThrottle):
    scope = 'registerthrottleUser' 
    # scope variable will be used in settings.py to set throttle restriction rate
