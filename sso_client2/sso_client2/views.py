from django.shortcuts import HttpResponse


def index(request):
    """
    the index page
    """

    if request.user.is_authenticated:
        return HttpResponse("Hello, %s from Pariksharth Exam platform" % request.user.username)
    else:
        return HttpResponse("Please login to access this page")
