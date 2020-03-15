from flask import Blueprint, render_template

error = Blueprint(
    "error", __name__, template_folder="../templates", static_folder="../static"
)


@error.app_errorhandler(404)
def error_404(e):
    return render_template("beagle/pages-404.html"), 404


@error.app_errorhandler(403)
def error_403(e):
    return render_template("beagle/pages-404.html"), 403


@error.app_errorhandler(500)
def error_500(e):
    return render_template("beagle/pages-404.html"), 500


@error.app_errorhandler(413)
def error_413(e):
    return render_template("beagle/pages-404.html"), 413
