from flask import Flask, Blueprint, request, render_template, redirect, url_for, flash, session, current_app
from .models import alch, Employee, Client, Individual, LegalEntity, Landlord, Client, IndividualLandlord, LegalEntityLandlord, Property, Application, Contract, Department, Position, Employee, Credentials
from .forms import LoginForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    user = Credentials.query.get(session['user_id'])
    applications = Application.query.all()
    contracts = Contract.query.all()
    properties = Property.query.all()
    landlords = Landlord.query.all()
    clients = Client.query.all()


    return render_template('index_application.html', user=user, applications=applications, contracts=contracts, properties=properties, landlords=landlords, clients=clients)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = Credentials.query.filter_by(login=form.username.data).first()
        if user and current_app.bcrypt.check_password_hash(user.password, form.password.data):
            session['user_id'] = user.employee_id
            return redirect(url_for('main.index'))
        flash('Неправильный ввод данных')
    return render_template('index_auth.html', form=form)

@main.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.login'))

@main.route('/application', methods=['GET', 'POST'])
def application():
    application = Application.query.all()
    return render_template('index_application.html', application=application)

@main.route('/contracts', methods=['GET', 'POST'])
def contract():
    contract = Contract.query.all()
    return render_template('index_lease_agreement.html', contract=contract)

@main.route('/property', methods=['GET', 'POST'])
def property():
    property = Property.query.all()
    return render_template('index_property.html', property=property)

@main.route('/landlord', methods=['GET', 'POST'])
def landlord():
    landlord = Landlord.query.all()
    return render_template('index_landlords.html', landlord=landlord)

@main.route('/client', methods=['GET', 'POST'])
def client():
    client = Client.query.all()
    return render_template('index_tenants.html', client=client)