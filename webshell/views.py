from subprocess import Popen, PIPE

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import permission_required


@csrf_exempt
@require_POST
@permission_required('is_superuser')
def execute_script_view(request):
    source = request.POST.get('source', '').replace('"', r'\"')
    proc = Popen('python -c "%s"' % source, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()

    return HttpResponse(out or err)