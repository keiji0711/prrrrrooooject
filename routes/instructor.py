from flask import Blueprint, render_template

bp = Blueprint('instructor',__name__, template_folder = '../templates/instructor')

@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@bp.route('/instrcutor/grades')
def instrcutor_grades():
    return render_template('grades.html')


@bp.route('/instrcutor/attendance')
def instrcutor_attendance():
    return render_template('attendance.html')

