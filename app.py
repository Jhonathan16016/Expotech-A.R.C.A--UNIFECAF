from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from ARCA_core import (fazer_login, como_banco, salvar_estado, salvar_temp, eh_admin, listar_usuarios_db,cadastrar_usuario_db, login_existe, arcondicionado, fogao, maquina_lavar, privada)
import os,secrets

app=Flask(__name__)
app.secret_key='arrozpretosixsevenaura'

@app.route('/', methods=['GET', 'POST'])
def login():
    erro=None
    if request.method =='POST':
        usuario=fazer_login(request.form['login'], request.form['senha'])
        if usuario:
            session['usuario'] = usuario
            return redirect(url_for('menu'))
        erro = 'Login ou senha incorretos.'
    return render_template('index.html', erro=erro)

@app.route('/menu')
def menu():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('menu.html', usuario=session['usuario'])


JOGOS = {
      'jogo':{'nome': 'nome do jogo', 'core': 'core do jogo', 'arquivo': 'arquivo do jogo'},
}    
    

COMANDOS = {
    arcondicionado: {'quente': 'ligar_quente', 'frio': 'ligar_frio',
                     'ambiente': 'ligar_ambiente', 'desligar': 'desligar'},
    fogao:          {'minimo': 'ligar_minimo', 'baixo': 'ligar_baixo', 'medio': 'ligar_medio',
                    'alto': 'ligar_alto', 'desligar': 'desligar'},
    maquina_lavar:  {'diaria': 'lavagem_diaria', 'rapida': 'lavagem_rapida',
                    'pesada': 'lavagem_pesada', 'desligar': 'desligar'},
    privada:        {'descarga': 'descarga', 'aquecimento': 'aquecimento',
                    'desligar': 'desligar_aque'},
}

BOTOES = {
    'arcondicionado':   [('quente', 'Quente 30°C'), ('frio', 'Frio 18°C'),
                        ('ambiente', 'Ambiente'), ('desligar', 'Desligar')],
    'fogao':            [('minimo', 'Mínimo'), ('baixo', 'Baixo'), ('medio', 'Médio'),
                        ('alto', 'Alto'), ('desligar', 'Desligar')],
    'maquina_lavar':    [('diaria', 'Diária'), ('rapida', 'Rápida'),
                        ('pesada', 'Pesada'), ('desligar', 'Desligar')],
    'privada':          [('descarga', 'Descarga'), ('aquecimento', 'Aquecimento'),
                        ('desligar', 'Desligar')],
}

@app.route('/arcade')
def arcade():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('arcade.html',jogos=JOGOS)

@app.route('/jogo/<id_jogo>')
def jogo(id_jogo):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    dados= JOGOS.get(id_jogo)
    if dados is None:
        return redirect(url_for('arcade'))
    return render_template('jogo.html', dados=dados)

COMODOS= ['Sala', 'Cozinha', 'Quarto das Crianças', 'Quarto dos Adultos', 'Banheiro', 'Lavanderia']

@app.route('/casa')
def casa():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('casa.html', comodos=COMODOS)

@app.route('/comodos/<nome>')
def comodos(nome):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    if nome not in COMODOS:
        return redirect(url_for('casa'))
    return render_template('comodos.html', nome=nome, aparelhos=como_banco(nome), botoes=BOTOES)

@app.route('/acao/<nome>/<int:disp_id>/<acao>', methods=['POST'])
def acao(nome,disp_id, acao):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    item = como_banco(nome).get(disp_id)
    if item:
        objeto, liga, desliga = item
        if acao == 'ligar' and liga:
            liga()
        elif acao == 'desligar' and desliga:
            desliga()
        salvar_estado(objeto)
    return redirect(url_for('comodos', nome=nome))



@app.route('/especial/<nome>/<int:disp_id>/<comando>', methods=['POST'])
def especial(nome, disp_id, comando):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    item= como_banco(nome).get(disp_id)
    if item:
        objeto= item[0]
        metodo= COMANDOS.get(type(objeto), {}). get(comando)
        if metodo:
            getattr(objeto, metodo)()
            salvar_estado(objeto)
    return redirect(url_for('comodos', nome=nome))

@app.route('/api/temp/<nome>/<int:disp_id>')
def api_temp(nome, disp_id):
    if 'usuario' not in session:
        return jsonify(erro='login'), 401
    item = como_banco(nome).get(disp_id)
    if not item or not hasattr(item[0], 'temperatura_atual'):
        return jsonify(erro='nao encontrado'), 404
    objeto= item[0]
    if not (isinstance(objeto, arcondicionado) and not objeto.ligado):
        objeto.passagem_tempo()
        salvar_temp(objeto)
    return jsonify(temperatura=round(objeto.temperatura_atual, 1))

@app.route('/sair')
def sair():
    session.clear()
    return redirect(url_for('login'))

@app.route('/admin')
def admin():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    if not eh_admin(session['usuario']):
        return redirect(url_for('menu'))
    return render_template('admin.html', usuarios=listar_usuarios_db())

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=False)
