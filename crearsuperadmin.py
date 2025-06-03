from app import app, db, User  # Asegúrate de importar app, db y User

with app.app_context():
    if not User.query.filter_by(username='superadmin').first():
        user = User(username='superadmin', name='Super Administrador', password='1234', is_superadmin=True)
        db.session.add(user)
        db.session.commit()
        print("Superadmin creado correctamente")
    else:
        print("Ya existe un superadmin.")
