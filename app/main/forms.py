# -*- coding:utf-8 -*-
# @Time    : 19-7-4 下午7:48
# @Author  : zhangshanling

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
	search = StringField('search', validators=[DataRequired()])

