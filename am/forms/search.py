from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
class BasicSearchForm(FlaskForm):
    name = StringField('名称')
    search = SubmitField('查询')