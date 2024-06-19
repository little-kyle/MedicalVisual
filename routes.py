from flask import request, render_template, jsonify
from app import app, db
from models import *
from pydicom import dcmread
import os


@app.route("/")  # 表示访问根路由的时候就会执行下面这个函数；
def home():
    return render_template("index.html")


#从前端根据输入的患者信息对患者进行信息建档；
@app.route('/Archiving', methods=['POST'])
def patient_archive():
    id=request.form.get('Patient_ID')
    name=request.form.get('Patient_Name')
    sex=request.form.get('Sex')
    birthdate=request.form.get('Birth_Date')
    phone=request.form.get('Phone')
    doctor_id=request.form.get('Doctor_ID')
    patient=Patients.query.filter_by(Patient_ID=id).first()
    if patient: #表示该病人先前已经进行了存储存档，返回已经存在的提示；
        return jsonify({'exists': True, 'message': 'Patient\'s information already exists.'}), 200
    else:
        newcase=Patients(Patient_ID=id,Patient_Name=name,Sex=sex,Birth_Date=birthdate,Phone=phone)
        db.session.add(newcase)
        db.session.commit()
        newrelation=DoctorPatient(Doctor_ID=doctor_id,Patient_ID=id)
        db.session.add(newrelation)
        db.session.commit()
        return jsonify({'message': 'Patient\'s information has been archived succussfully'}), 200

#从前端接收用户上传的医学图像数据，根据指定的病人ID和姓名进行存储；
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    #name=request.form.get('Patient_Name')
    id=request.form.get('Patient_ID')
    modality=request.form.get('Modality')
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file:
        #filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        #file.save(filepath)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        dicom_data = dcmread(filepath)
        ds_bytes1=dicom_data.PixelData
        #print(ds_bytes1)

        image=Images(Image_Modality=modality,Patient_ID=id,Image_data=ds_bytes1)

        #user=DicomData(Patient_ID=id,Patient_Name=name,Examine_Data="20240615",Image_Modality="DDR",Image_data=ds_bytes1)
        db.session.add(image)
        db.session.commit()
        if os.path.exists(filepath):
            os.remove(filepath)
        return jsonify({'message': 'File successfully uploaded', 'filename': file.filename}), 200

@app.route('/query_data', methods=['POST'])
def query_data():
    id = request.form.get('Patient_ID')
    

    print(f"Received data - Patient_ID: {id}")

    # 处理数据
    images = Images.query.filter_by(Patient_ID=id)
    for image in images:
        print(image.Image_ID,image.Image_Modality,image.Examine_Date)
    print(type(images))

    response = {
        'message': 'Data queried successfully',
        'queried_data': id
    }

    return jsonify(response), 200
