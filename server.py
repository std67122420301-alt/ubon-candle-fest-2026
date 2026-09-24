from ubcf import app, db
from ubcf.models import Role

with app.app_context():
    db.create_all()  # เปิดใช้งานไว้ เพื่อให้ระบบสร้างตารางให้อัตโนมัติหากยังไม่มี
    
    if not Role.query.first():
        admin_role = Role(id=1, name='Admin')
        user_role = Role(id=2, name='User')
        db.session.add_all([admin_role, user_role])
        db.session.commit()