
from comunidadeprog.models import Usuario, Post_usuario
from comunidadeprog import app
from comunidadeprog import database

with app.app_context():
    usuario_teste = Usuario.query.filter_by(email='luis035@gmail.com').first()
    print((usuario_teste))
    print(usuario_teste.senha)
    print(usuario_teste.nome)
    print(usuario_teste.email)
    print(usuario_teste.softskills)

with app.app_context():
    post_teste = Post_usuario.query.first()
    print((post_teste))
    print(post_teste.título)
    print(post_teste.corpo)



    # database.drop_all()
    #database.create_all()

   #meus_usuarios = Usuario.query.all()
    #print(meus_usuarios)
    #prog =Usuario.query.first()
    #print(prog)
    #print(prog.nome)
    #print(prog.email)
    #print(prog.senha)