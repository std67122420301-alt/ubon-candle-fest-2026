from ubcf import app, db

# สั่งสร้างตารางให้อัตโนมัติเมื่อเริ่มระบบบน Render
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)