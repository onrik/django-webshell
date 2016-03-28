import sys
import traceback
from contextlib import contextmanager
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import permission_required


@contextmanager
def catch_stdout(buff):
    stdout = sys.stdout
    sys.stdout = buff
    yield
    sys.stdout = stdout


@require_POST
@permission_required('is_superuser')
def execute_script_view(request):
    buff = StringIO()
    try:
        with catch_stdout(buff):
            exec(request.POST.get('source', ''))
    except:
        traceback.print_exc(file=buff)

    return HttpResponse(buff.getvalue())
