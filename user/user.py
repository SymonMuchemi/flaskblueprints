from flask import session, redirect, request, url_for, render_template, flash
from user import bp

@bp.route('/user', methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template('user.html',email=email )
    else:
        flash("You are not logged in")
        return redirect(url_for("authentication.login"))