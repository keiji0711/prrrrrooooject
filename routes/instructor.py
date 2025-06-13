from flask import Blueprint, render_template
import mysql.connector

bp = Blueprint('instructor',__name__, template_folder = 'template' )

@bp.route('/dashboard')
def dashboard():

    return render_template('instructor/dashboard.html')


@bp.route('/instrcutor/grades')
def instrcutor_grades():
    return render_template('instructor/grades.html')


@bp.route('/instrcutor/attendance')
def instrcutor_attendance():
    return render_template('instructor/attendance.html')


@bp.route('/instrcutor/sub_and_sched')
def instructor_sub_sched():
    return render_template('instructor/sub_and_sched.html')

@bp.route('/instrcutor/reports')
def instructor_reports():
    return render_template('instructor/reports.html')
