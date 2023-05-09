from django.http import HttpResponse, JsonResponse, HttpRequest

def api_response(request, param_id):
    return JsonResponse({'some': 'data', 'param_id': param_id})

def from_response(request):
    return JsonResponse({'success': 'here_should_be_some_status', 'data': 'here_should_be_some_data'})