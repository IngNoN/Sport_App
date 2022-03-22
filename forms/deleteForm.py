from flask_wtf import FlaskForm
from sqlalchemy import Numeric
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import HiddenField

class DeleteItemForm(FlaskForm):
    teacher_Id = HiddenField("teacher_Id")
    departmentManager_Id = HiddenField("departmentManager_Id")
    group_of_teachers_Id = HiddenField("group_of_teachers_Id")
