from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import current_user

#from .. import movie_client
from ..forms import AttackRegisterForm, AttackUpdate, AttackSubmit
from ..models import User, Attack
from ..utils import current_time
import dice


# create blue print
attacks = Blueprint("attacks", __name__)

#functions

@attacks.route("/", methods=["GET", "POST"])
def index():
    #index is essentially the register attack page..
    form = AttackRegisterForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        attack = Attack(
            owner=current_user._get_current_object(),
            name=form.name.data,
            type = form.type.data,
            damage = form.damage.data,
        )
        attack.save()
        return redirect(request.path)

    return render_template("index.html", form = form)


@attacks.route("/all/<username>", methods=["GET", "POST"])
def all(username):
    
    user = User.objects(username=username).first()
    attacks = Attack.objects(owner=user)

    return render_template("all.html", attacks = attacks)


@attacks.route("/calculate", methods=["GET", "POST"])
def calculate():
    output = 0
    form = AttackSubmit()
    if form.validate_on_submit() and current_user.is_authenticated:
        output = dice.roll(form.damage.data + "t")
        if "true" in form.isCrit.data:
            output = output*2
        print(output)

    return render_template("calculate.html", output= output, form = form)

@attacks.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")
