from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, DecimalField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
from .models import Credentials  # Импортируем модель сотрудников для проверки логина

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

    def validate_username(self, username):
        user = Credentials.query.filter_by(login=username.data).first()
        if not user:
            raise ValidationError('Нет аккаунта с таким именем пользователя.')