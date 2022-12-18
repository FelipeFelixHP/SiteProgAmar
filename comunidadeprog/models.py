from comunidadeprog import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))



class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post_usuario', backref='autor', lazy=True)
    softskills =database.Column(database.String, nullable=False, default='Não Informado')

class Post_usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    título = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criaçao = database.Column(database.DateTime, nullable=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)