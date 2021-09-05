from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#connect to database
engine = create_engine('mysql://root:''@localhost/example', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

#create table

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

Base.metadata.create_all(engine)

#Insert data into table

student1 = Student(name = "darshan", age = "23", grade = "Fifth")
student2 = Student(name = "Karan", age = "21",grade = "Fourth")
student3 = Student(name = "Akash", age = "21", grade = "Third")
#session.add(student1)
session.add_all([ student2, student3])

session.commit()

#Read data from database or table

students = session.query(Student)

for student in students:

    print(student.name, student.age, student.grade)


students = session.query(Student).order_by(Student.name)

for student in students:
    print(student.name)

students = session.query(Student).filter(Student.name.like("Ak%"))
students_count = session.query(Student).filter(Student.name.like("Ak%")).count()
print(students_count)

for student in students:
    print(student.name, student.age)


#update table

#student =   session.query(Student).filter(Student.name == 'Karan').first()

#Student.name = "Yash"

#session.commit()

student = session.query(Student).filter(Student.name == 'Akash').first()

#session.delete(student)

#session.commit()

print(student.name)