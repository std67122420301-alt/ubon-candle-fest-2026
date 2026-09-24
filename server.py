from ubcf import app, db
from ubcf.models import Role

with app.app_context():
    db.drop_all()   # ลบตารางเก่า
    db.create_all() # สร้างตารางใหม่
    
    # เพิ่มข้อมูล Role เริ่มต้น หากในตารางยังไม่มีข้อมูล
    if not Role.query.first():
        admin_role = Role(id=1, name='Admin')
        user_role = Role(id=2, name='User')
        db.session.add_all([admin_role, user_role])
        db.session.commit()