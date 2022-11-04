from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info in ['/login/', '/home/', '/regist/', '/image_code/', '/favicon.ico/', '/']:
            return

        if request.session.get("info"):
            return
        print(request.path_info)
        return redirect('/login/')