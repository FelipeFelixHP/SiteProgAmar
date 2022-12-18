from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeprog.models import Usuario, Post_usuario
from flask_login import current_user

#tudo que você vai criar de novo, todos os objetos etc, vai ser uma classe no python
#metodo post você esta enviando alguma informação para o servidor, em formulario é obrigadorio
#enctype="multipart/form-data" passar esse parametro sempre que no formulario tiver que subir um arquivo, (FileField ) dentro do forme htl voce passara esse parametro


class FormCriarConta(FlaskForm):
    nome = StringField('Nome do usuário', validators=[DataRequired()])
    email =StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmaçao_senha = PasswordField ('Confirmação de senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField ('Criar conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')

class FormLongin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField('Lembrar Dados de acesso')
    botao_submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    nome = StringField('Nome do usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto do Perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])

    softskills_empatia = BooleanField('Empatia')
    softskills_comunicaçao = BooleanField('Comunicação')
    softskills_trabalhoEquipe = BooleanField('Trabalho em Equipe')
    softskills_organizaçao = BooleanField('Organização')
    softskills_renociaçao = BooleanField('Negociação')
    softskills_pensamento_criativo = BooleanField('Pensamento criativo')
    softskills_liderança = BooleanField('Liderança')

    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        #verificar se o cara mudou de email
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail. Cadastre outro e-mail')


class FormCriarPost(FlaskForm):
    título = StringField('Título do Post', validators=[DataRequired()])
    corpo = TextAreaField('Escreva seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')
