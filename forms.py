from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import Optional, DataRequired

class NumberInput(FlaskForm):
    num_a = FloatField('Insira o valor de A', validators=[DataRequired()])
    num_b = FloatField('Insira o valor de B', validators=[DataRequired()])
    num_c = FloatField('Insira o valor de C', validators=[DataRequired()])

    button_submit = SubmitField('Gerar')

class NumberInput_1(FlaskForm):
    num_a_1 = FloatField('Insira o valor de A', validators=[DataRequired()])
    num_b_1 = FloatField('Insira o valor de B', validators=[DataRequired()])

    button_submit_1 = SubmitField('Gerar')