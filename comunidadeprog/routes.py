from flask import render_template, request, url_for, redirect, flash
from comunidadeprog import app, database, bcrypt
from comunidadeprog.forms import FormLongin, FormCriarConta, FormEditarPerfil, FormCriarPost
from comunidadeprog.models import Usuario, Post_usuario
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image

@app.route('/home')
def inicio():
    return render_template("home.html")

@app.route('/comunidade')
def comunidade():
    posts = Post_usuario.query.order_by(Post_usuario.id.desc())
    return render_template("comunidade.html", posts=posts)

@app.route('/doar')
@login_required
def doar():
    return render_template("conhecimento.html")

@app.route('/doando')
@login_required
def doando():
    return render_template("doando.html")

@app.route('/soft')
@login_required
def soft():
    return render_template("soft.html")

@app.route('/certificado')
@login_required
def certificado():
    return render_template("certificado.html")

@app.route('/ong')
def ong():
    return render_template("ongs.html")

@app.route('/saibamais')
def saibamais():
    return render_template("saibamais.html")

@app.route('/teste')
def conhecimento():
    return render_template("contato.html")

@app.route('/usuarios')
def usuarios():
    lista_usuarios = Usuario.query.all()
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)

@app.route('/login', methods=['get', 'post'])
def login():
    form_login = FormLongin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert alert-success')
            param_next = request.args.get('next')
            if param_next:
                return redirect(param_next)
            else:
                return redirect(url_for('doar'))

        else:
            flash(f'Falha no Login.E-mail ou Senha Incorretos: ', 'alert-danger')

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(nome=form_criarconta.nome.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()


        flash('Conta criada com sucesso no e-mail:'.format(form_criarconta.email.data), 'alert alert-success')
        return redirect(url_for('perfil'))

    return render_template("login.html", form_login=form_login, form_criarconta=form_criarconta)


@app.route('/cadastro', methods=['get', 'post'])
def cadastro():
    form_login= FormLongin()
    form_criarconta= FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert alert-success')
            param_next = request.args.get('next')
            if param_next:
                return redirect(param_next)
            else:
                return redirect(url_for('perfil'))

        else:
            flash(f'Falha no Login.E-mail ou Senha Incorretos: ', 'alert-danger')

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(nome=form_criarconta.nome.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()

        flash('Conta criada com sucesso no e-mail:'.format(form_criarconta.email.data), 'alert alert-success')
        return redirect(url_for('criar_post'))

    return render_template("cadastro.html", form_login=form_login, form_criarconta=form_criarconta)


@app.route('/cadastroong', methods=['get', 'post'])
def cadastroong():
    form_login= FormLongin()
    form_criarconta= FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert alert-success')
            param_next = request.args.get('next')
            if param_next:
                return redirect(param_next)
            else:
                return redirect(url_for('relatorioong'))

        else:
            flash(f'Falha no Login.E-mail ou Senha Incorretos: ', 'alert-danger')

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(nome=form_criarconta.nome.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()

        flash('Conta criada com sucesso no e-mail:'.format(form_criarconta.email.data), 'alert alert-success')
        return redirect(url_for('relatorioong'))

    return render_template("cadastroong.html", form_login=form_login, form_criarconta=form_criarconta)

@app.route('/relatorioong')
def relatorioong():
    return render_template("relatorioong.html")

@app.route('/criarpostong')
def criarpostong():
    return render_template("criarpostong.html")

@app.route('/confirmaçaoong')
def confirmaçaoong():
    return render_template("confirmaçaoong.html")

@app.route('/perfilong')
def perfilong():
    return render_template("perfilong.html")



@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'Logout Feito com Sucesso', 'alert alert-success')
    return redirect(url_for('comunidade'))

    pass

@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename='foto_perfil/{}'.format(current_user.foto_perfil))
    return render_template("perfil.html", foto_perfil=foto_perfil)

@app.route('/post/criar',methods=['get', 'post'])
@login_required
def criar_post():
    form = FormCriarPost()
    if form.validate_on_submit():
        post = Post_usuario(título=form.título.data, corpo=form.corpo.data, autor=current_user)
        database.session.add(post)
        database.session.commit()
        flash('Post Criado com Sucesso', 'alert-success')
        return redirect(url_for('comunidade'))
    return render_template("criarpost.html", form=form)

def salvar_imagem(imagem):
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_arquivo = nome + codigo + extensao
    caminho_completo = os.path.join(app.root_path, 'static/foto_perfil', nome_arquivo)

    tamanho = (400 , 400)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo)

    return nome_arquivo

    # add um codigo aleatorio no nome da imagem para nao correr o risco do usuario o arquivo com o mesmo nome
    # reduzir o tamanho da imagem
    # salvar a imagem na pasta fotos_perfil
    # mudar o campo foto_perfil do usuario para o novo nome da imagem

def atualizar_softskills(form):
    lista_softskills = []
    for campo in form:
        if 'softskills_' in campo.name:
            if campo.data:
            #adicionar o texto do campo.label (Empatia) na lista de softskills
                lista_softskills.append(campo.label.text)
    return ';'.join(lista_softskills)

@app.route('/perfil/editar',methods=['get', 'post'])
@login_required
def editar_perfil():
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.nome = form.nome.data

        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        current_user.softskills = atualizar_softskills(form)
        database.session.commit()
        flash(f'Perfil atualizado com Sucesso', ' alert alert-success')
        return redirect(url_for('perfil'))

    #PARA O FORMULARI0 JÁ APARECER PREENCHIDO
    elif request.method == "GET":
        form.email.data = current_user.email
        form.nome.data = current_user.nome



    foto_perfil = url_for('static', filename='foto_perfil/{}'.format(current_user.foto_perfil))
    return render_template("editarperfil.html", foto_perfil=foto_perfil, form=form)



@app.route('/post/<post_id>')
def exibir_post(post_id):
    post = Post_usuario.query.get(post_id)
    return render_template('post.html', post=post)