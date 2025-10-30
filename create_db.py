import os
from app import app, db
from models import Student, Major
import datetime as dt

# ✅ Make sure the instance directory exists
instance_path = os.path.join(os.path.dirname(__file__), 'instance')
os.makedirs(instance_path, exist_ok=True)

with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of majors
    majors = [
        'Aerospace Engineering', 'Biology', 'Civil Engineering', 'Computer Science',
        'Electrical Engineering', 'Finance', 'Information Systems', 'Marketing',
        'Mechanical Engineering'
    ]
    for each_major in majors:
        print(each_major)
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()

    # Initial loading of students
    students = [
        {
            'student_id': '1',
            'first_name': 'Robert',
            'last_name': 'Smith',
            'major_id': 3,
            'email': 'gfhorizon@umd.edu',
            'birth_date': dt.datetime(2005, 6, 1),
            'is_honors': True
        },
        {
            'student_id': '2',
            'first_name': 'Leo',
            'last_name': 'Van Munching',
            'major_id': 6,
            'email': 'rsmith4039@umd.edu',
            'birth_date': dt.datetime(2004, 3, 24),
            'is_honors': False
        },
    ]

    for each_student in students:
        print(f'{each_student["first_name"]} {each_student["last_name"]} inserted into Student')
        a_student = Student(
            first_name=each_student["first_name"],
            last_name=each_student["last_name"],
            major_id=each_student["major_id"],
            email=each_student["email"],
            birth_date=each_student["birth_date"],
            is_honors=each_student["is_honors"]
        )
        db.session.add(a_student)
        db.session.commit()

