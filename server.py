from ubcf import app, db

# สั่งสร้างตารางให้อัตโนมัติเมื่อเริ่มระบบบน Render
with app.app_context():
    db.drop_all()   # ลบตารางโครงสร้างเดิมที่มีปัญหาทิ้ง
    db.create_all() # สร้างตารางใหม่ด้วยขนาดคอลัมน์ใหม่