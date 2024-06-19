import datetime
from app import db
from sqlalchemy import Enum
import enum

class UserRole(enum.Enum):
    DOCTOR = 'doctor'
    ADMIN = 'admin'

#下面对应了数据库的表文件
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role=db.Column(Enum(UserRole), nullable=False)

class Doctors(db.Model):
    __tablename__ = "doctors"
    Doctor_ID = db.Column(db.String(50), primary_key=True, nullable=False)
    Doctor_Name = db.Column(db.String(100), nullable=False)
    Specialization = db.Column(db.Text)
    User_ID=db.Column(db.Integer,db.ForeignKey('users.User_ID'))

class Patients(db.Model):
    __tablename__ = "patients"
    Patient_ID = db.Column(db.String(50), primary_key=True, nullable=False)
    Patient_Name = db.Column(db.String(100), nullable=False)
    Sex=db.Column(db.String(2),nullable=False)
    Birth_Date=db.Column(db.Date,nullable=False)
    Phone=db.Column(db.String(11),nullable=True)

class Images(db.Model):
    __tablename__ = "images"
    Image_ID=db.Column(db.Integer, primary_key=True, autoincrement=True)
    Examine_Date = db.Column(db.DateTime, default=datetime.datetime.now,nullable=False)
    Image_Modality = db.Column(db.String(10),nullable=False)
    Body_Part=db.Column(db.String(20))
    Patient_ID=db.Column(db.String(50),db.ForeignKey('patients.Patient_ID'))
    Diagnosis_Notes=db.Column(db.Text)
    Image_data = db.Column(db.LargeBinary,nullable=False)

class DoctorPatient(db.Model):
    __tablename__="doctorpatient"
    Doctor_ID = db.Column(db.String(50),db.ForeignKey('doctors.Doctor_ID'), primary_key=True)
    Patient_ID = db.Column(db.String(50), db.ForeignKey('patients.Patient_ID'), primary_key=True)
