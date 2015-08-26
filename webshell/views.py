import commands

from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import permission_required


@require_POST
@permission_required('is_superuser')
def execute_script_view(request):
    source = request.POST.get('source', '').replace('"', r'\"')
    result = commands.getoutput('python -c "%s"' % source)

    return HttpResponse(result)