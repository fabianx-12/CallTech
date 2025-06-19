from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Optional

class ContactForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    phone = StringField('Teléfono', validators=[DataRequired()])
    email = StringField('Email', validators=[Optional(), Email()])
    company = StringField('Empresa', validators=[Optional()])
    notes = TextAreaField('Notas', validators=[Optional()])
    submit = SubmitField('Guardar')

class RegisterForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    phone = StringField('Teléfono', validators=[DataRequired()])
    submit = SubmitField('Entrar a CallTech')
