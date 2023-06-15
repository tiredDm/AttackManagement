import waitress
import run
waitress.serve(run.app, listen='*:8000', threads=1, expose_tracebacks=True)