from sqlalchemy import text
from app import *
from models import User, DicomData

def init_db():
    with app.app_context():
        #db.create_all()
        with db.engine.connect() as conn:
            rs = conn.execute(text("select 1"))
            print(rs.fetchone())

if __name__ == "__main__":
    init_db()
