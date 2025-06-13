from flask import Blueprint,render_template,request
import mysql.connector


bp = Blueprint('admin',__name__,template_folder = 'template')


@bp.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')

@bp.route('/admin/classroom', methods = ['POST', 'GET'])
def admin_classroom():
    
    return render_template('admin/classroom.html')

@bp.route('/admin/instructor')
def admin_instructor():
    return render_template('admin/instructor.html')

@bp.route('/admin/student_list')
def admin_student_list():
    return render_template('admin/student_list.html')