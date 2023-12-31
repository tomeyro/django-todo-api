def cors_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
        return response

    return middleware
