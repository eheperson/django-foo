from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """ 
    has_object_permission : 
    has_permission :  request timi ne olursa olsun(post,get,delete vs) ilk olarak has permission çalışır

    fakat, delete metodu yazdığımızda, api ucu genellikle sadece delete requeste izin verir.
        temelde sayfaya yapılan her istek get dir.

    yukarıda ki saçma sapan açıklamaya özet olarak : 
        has_object_permission sadece izin verilen görev yapıldığı zaman çalışır.
        has_permission her koşulda çalışacak olan ilk fonksiyondur. 

    has_permission : kullanıcının giriş yapmadığı durumlarda kullanılır 
    has_permission_object : kullanıcının giriş yaptığı durumlarda kullanılır 
    """ 
    message = "you must be the owner of the object"
 
    def has_permission(self, request, view):
        """" 
        just an example
        """
        print("has_permission is running.")
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        #   to check if user is the owner of the post or if user is admin
        return obj.user == request.user
