from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField, IntegerField, \
    RadioField
from wtforms.validators import DataRequired, NumberRange


class MainForm(FlaskForm):
    min_len_word = IntegerField('Min length W.', validators=[NumberRange(min=3, max=30)], default=5)
    max_len_word = IntegerField('Max length W.', validators=[NumberRange(min=7, max=100)], default=7)
    population = IntegerField('Population', validators=[NumberRange(min=100, max=10000)], default=2000)
    mutation = IntegerField('Mutation %', validators=[NumberRange(min=1, max=100)], default=2)

    FileWord_btn = RadioField('From...', choices=[('TextArea', 'TextArea'), ('File', 'File(.txt)')], default='TextArea')
    Area = TextAreaField('Input Text')

    submit = SubmitField('Generate')
    erase = SubmitField('Erase')

    Area_out = TextAreaField('Out Text')
