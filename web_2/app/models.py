from . import alch
from flask import current_app
from sqlalchemy import ForeignKey
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property



class IndividualLandlord(alch.Model):
    __tablename__ = 'individual_landlords'
    __table_args__ = {'schema': 'db_accounting_schema'}
    individual_landlord_id = alch.Column(alch.Integer, primary_key=True)
    last_name = alch.Column(alch.String(100), nullable=False)
    first_name = alch.Column(alch.String(100), nullable=False)
    middle_name = alch.Column(alch.String(100))
    passport_number = alch.Column(alch.String(10), nullable=False)

class LegalEntityLandlord(alch.Model):
    __tablename__ = 'legal_entity_landlords'
    __table_args__ = {'schema': 'db_accounting_schema'}
    legal_landlord_id = alch.Column(alch.Integer, primary_key=True)
    company_name = alch.Column(alch.String(255))
    registration_number = alch.Column(alch.String(10), nullable=False)

class Individual(alch.Model):
    __tablename__ = 'individuals'
    __table_args__ = {'schema': 'db_accounting_schema'}
    individuals_id = alch.Column(alch.Integer, primary_key=True)
    last_name = alch.Column(alch.String(100), nullable=False)
    first_name = alch.Column(alch.String(100), nullable=False)
    middle_name = alch.Column(alch.String(100))
    birth_date = alch.Column(alch.Date, nullable=False)
    passport_number = alch.Column(alch.String(10), nullable=False)

class LegalEntity(alch.Model):
    __tablename__ = 'legal_entities'
    __table_args__ = {'schema': 'db_accounting_schema'}
    legal_client_id = alch.Column(alch.Integer, primary_key=True)
    company_name = alch.Column(alch.String(255), nullable=False)
    registration_number = alch.Column(alch.String(10), nullable=False)

class Client(alch.Model):
    __tablename__ = 'clients'
    __table_args__ = {'schema': 'db_accounting_schema'}
    client_id = alch.Column(alch.Integer, primary_key=True)
    client_type = alch.Column(alch.String(50), nullable=False)
    client_status = alch.Column(alch.String(50), nullable=False)
    phone_number = alch.Column(alch.String(20), nullable=False)
    email = alch.Column(alch.String(255), nullable=False)
    address = alch.Column(alch.String(255), nullable=False)
    individual_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.individuals.individuals_id'))
    legal_entity_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.legal_entities.legal_client_id'))
    individual = alch.relationship('Individual', backref=alch.backref('clients'))
    legal_entity = alch.relationship('LegalEntity', backref=alch.backref('clients'))

class Landlord(alch.Model):
    __tablename__ = 'landlords'
    __table_args__ = {'schema': 'db_accounting_schema'}
    landlord_id = alch.Column(alch.Integer, primary_key=True)
    landlord_type = alch.Column(alch.String(50), nullable=False)
    landlord_status = alch.Column(alch.String(50), nullable=False)
    phone_number = alch.Column(alch.String(20), nullable=False)
    email = alch.Column(alch.String(255), nullable=False)
    address = alch.Column(alch.String(255), nullable=False)
    individual_landlord_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.individual_landlords.individual_landlord_id'))
    legal_landlord_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.legal_entity_landlords.legal_landlord_id'))
    individual_landlord = alch.relationship('IndividualLandlord', backref=alch.backref('landlords'))
    legal_landlord = alch.relationship('LegalEntityLandlord', backref=alch.backref('landlords'))

class Property(alch.Model):
    __tablename__ = 'properties'
    __table_args__ = {'schema': 'db_accounting_schema'}
    property_id = alch.Column(alch.Integer, primary_key=True)
    properties_type = alch.Column(alch.String(50), nullable=False)
    area = alch.Column(alch.Numeric(10, 2), nullable=False)
    city = alch.Column(alch.String(100), nullable=False)
    address = alch.Column(alch.String(255), nullable=False)
    floor = alch.Column(alch.Integer, nullable=False)
    rental_cost = alch.Column(alch.Numeric(10, 2), nullable=False)
    condition = alch.Column(alch.String(100), nullable=False)
    furniture = alch.Column(alch.Boolean, nullable=True)
    rent_amount = alch.Column(alch.Numeric(10, 2), nullable=False)
    availability_date = alch.Column(alch.Date, nullable=True)
    description = alch.Column(alch.Text, nullable=True)
    status = alch.Column(alch.String(50), nullable=True)
    landlord_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.landlords.landlord_id'), nullable=False)
    landlord = alch.relationship('Landlord', backref=alch.backref('properties',))

class Application(alch.Model):
    __tablename__ = 'applications'
    __table_args__ = {'schema': 'db_accounting_schema'}
    application_id = alch.Column(alch.Integer, primary_key=True)
    client_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.clients.client_id'), nullable=False)
    property_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.properties.property_id'), nullable=False)
    application_date = alch.Column(alch.Date, nullable=False)
    start_date = alch.Column(alch.Date, nullable=True)
    end_date = alch.Column(alch.Date, nullable=True)
    application_status = alch.Column(alch.String(50), nullable=False)
    description = alch.Column(alch.Text, nullable=True)
    processing_deadline = alch.Column(alch.Date, nullable=True)
    rejection_reason = alch.Column(alch.Text, nullable=True)
    client = alch.relationship('Client', backref=alch.backref('applications'))
    property = alch.relationship('Property', backref=alch.backref('applications'))

class Contract(alch.Model):
    __tablename__ = 'contracts'
    __table_args__ = {'schema': 'db_accounting_schema'}
    contract_id = alch.Column(alch.Integer, primary_key=True)
    client_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.clients.client_id'), nullable=False)
    landlord_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.landlords.landlord_id'), nullable=False)
    property_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.properties.property_id'), nullable=False)
    signing_date = alch.Column(alch.Date, nullable=False)
    start_date = alch.Column(alch.Date, nullable=False)
    end_date = alch.Column(alch.Date, nullable=False)
    rent_price = alch.Column(alch.Numeric(10, 2), nullable=False)
    lease_conditions = alch.Column(alch.Text, nullable=True)
    contract_status = alch.Column(alch.String(50), nullable=False)
    notes = alch.Column(alch.Text, nullable=True)
    client = alch.relationship('Client', backref=alch.backref('contracts'))
    landlord = alch.relationship('Landlord', backref=alch.backref('contracts'))
    property = alch.relationship('Property', backref=alch.backref('contracts'))

class Department(alch.Model):
    __tablename__ = 'departments'
    __table_args__ = {'schema': 'db_accounting_schema'}
    department_id = alch.Column(alch.Integer, primary_key=True)
    department_name = alch.Column(alch.String(100), unique=True, nullable=False)

class Position(alch.Model):
    __tablename__ = 'positions'
    __table_args__ = {'schema': 'db_accounting_schema'}
    position_id = alch.Column(alch.Integer, primary_key=True)
    position_name = alch.Column(alch.String(100), unique=True, nullable=False)
    salary = alch.Column(alch.Numeric(10, 2), nullable=False)

class Employee(alch.Model):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'db_accounting_schema'}
    employee_id = alch.Column(alch.Integer, primary_key=True)
    first_name = alch.Column(alch.String(255), nullable=False)
    last_name = alch.Column(alch.String(255), nullable=False)
    middle_name = alch.Column(alch.String(255))
    passport_number = alch.Column(alch.String(255), nullable=False)
    email = alch.Column(alch.String(255), nullable=False)
    phone_number = alch.Column(alch.String(20), nullable=False)
    position_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.positions.position_id'), nullable=False)
    department_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.departments.department_id'), nullable=False)
    hire_date = alch.Column(alch.Date, nullable=False)
    position = alch.relationship('Position', backref=alch.backref('employees'))
    department = alch.relationship('Department', backref=alch.backref('employees'))

class Credentials(alch.Model):
    __tablename__ = 'credentials'
    __table_args__ = {'schema': 'db_accounting_schema'}
    employee_id = alch.Column(alch.Integer, alch.ForeignKey('db_accounting_schema.employees.employee_id'), primary_key=True)
    login = alch.Column(alch.String(255), unique=True, nullable=False)
    password = alch.Column(alch.Text, nullable=False)
    online = alch.Column(alch.Boolean)