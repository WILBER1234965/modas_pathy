import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cambiar-esta-clave'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'modas_pathy.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Para subir imágenes
    UPLOAD_FOLDER = os.path.join(basedir, 'static', 'uploads')
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2 MB máximo
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
