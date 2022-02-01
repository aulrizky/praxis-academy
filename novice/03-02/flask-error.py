from flask import Flask, json, render_template,template_rendered
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import werkzeug
from werkzeug.exceptions import HTTPException
from flask_bootstrap import Bootstrap
from contextlib import contextmanager

# sentry_sdk.init('YOUR_DSN_HERE', integrations=[FlaskIntegration()])

app = Flask(__name__)
bootstrap = Bootstrap(app)
# @app.errorhandler(werkzeug.exceptions.BadRequest)
# def handle_bad_request(e):
#     return 'bad request!', 400

# @app.errorhandler(HTTPException)
# def handle_exception(e):
#     """Return JSON instead of HTML for HTTP errors."""
#     # start with the correct headers and status code from the error
#     response = e.get_response()
#     # replace the body with JSON
#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#     })
#     response.content_type = "application/json"
#     return response


# @app.errorhandler(Exception)
# def handle_exception(e):
#     # pass through HTTP errors
#     if isinstance(e, HTTPException):
#         return e

#     return render_template("500_generic.html", e=e), 500

# @app.errorhandler(404)
# def not_found(e):
#     return render_template('404.html')

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html')

# @app.errorhandler(HTTPException)
# def handle_exception(e):
#     response = e.get_response()
#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#     })
#     response.content_type = 'application/json'
#     return response
# @app.route("/")
# @app.errorhandler(Exception)
# def handle_exception(e):
#     if isinstance(e, HTTPException):
#         return e
#     return render_template("500.html", e=e), 500

# @app.errorhandler(InternalServerError)
# def handle_500(e):
#     original = getattr(e, "original_exception", None)

#     if original is None:
#         # direct 500 error, such as abort(500)
#         return render_template("500.html"), 500

#     # wrapped unhandled error
#     return render_template("500_unhandled.html", e=original), 500

@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

# with captured_templates(app) as templates:
#     rv = app.test_client().get('/')
#     assert rv.status_code == 200
#     assert len(templates) == 1
#     template, context = templates[0]
#     assert template.name == 'base.html'
#     assert len(context['items']) == 10

if __name__ == "__main__":
    app.run(debug=True)
