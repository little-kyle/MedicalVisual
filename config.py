class Config:
    # MySQL所在的主机名字；
    HOSTNAME = "127.0.0.1"
    # MySQL监听的端口号，默认为3306
    PORT = 3306
    # 连接数据库的用户名，
    USERNAME = "root"
    # 连接数据库的密码；
    PASSWORD = "123456"
    # mysql上创建的数据库名称
    DATABASE = "medical_images"
    
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER='E:/VisualSystem/Medicalimages/data'
