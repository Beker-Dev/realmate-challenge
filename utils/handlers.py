from django.shortcuts import redirect

def redirect_404(request, exception):
    return redirect('messaging:conversation-list-view')

