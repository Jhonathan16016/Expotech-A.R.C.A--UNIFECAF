import random
import time
import os
import getpass
import mysql.connector
from ARCA_core import * 
from flask import Flask, jsonify, render_template, request, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
app=Flask(__name__)

def conectar_banco():
    return mysql.connector.connect(
        host='localhost',
        user=os.environ.get('ARCA_DB_USER'),
        password=os.environ.get('ARCA_DB_PASSWORD'),
        database='ARCA'
)

class luz:
    def __init__(self,nome):
        self.nome=nome
        self.ligada=False

    def ligar(self):
        self.ligada=True
        print(f'{self.nome}:Ligada')

    def desligar(self):
        self.ligada=False
        print(f'{self.nome}:Desligada')

    def estado(self):
        return 'Ligada' if self.ligada else 'Desligada'

class tv:
    def __init__(self,nome):
        self.nome=nome
        self.ligada=False

    def ligar(self):
        self.ligada=True
        print(f'{self.nome}:Ligada')

    def desligar(self):
        self.ligada=False
        print(f'{self.nome}:Desligada')

    def estado(self):
         return 'Ligada' if self.ligada else 'Desligada'

class porta:
    def __init__(self,nome):
        self.nome=nome
        self.ligada=False

    def aberta(self):
        self.ligada=True
        print(f'{self.nome}:Aberta')

    def fechada(self):
        self.ligada=False
        print(f'{self.nome}:Fechada')

    def estado(self):
        return 'Aberta' if self.ligada else 'Fechada'

class janela:
    def __init__(self,nome):
        self.nome=nome
        self.ligada=False

    def aberta(self):
        self.ligada=True
        print(f'{self.nome}:Aberta')

    def fechada(self):
            self.ligada=False
            print(f'{self.nome}:Fechada')

    def estado(self):
            return 'Aberta' if self.ligada else 'Fechada'

class cortina:
    def __init__(self,nome):
        self.nome=nome
        self.ligada=True

    def aberta(self):
        self.ligada=True
        print(f'{self.nome}:Aberta')

    def fechada(self):
            self.ligada=False
            print(f'{self.nome}:Fechada')

    def estado(self):
            return 'Aberta' if self.ligada else 'Fechada'

class arcondicionado:
    def __init__(self,nome):
        self.nome=nome
        self.ligado=False
        self.modo ='Desligado'
        self.temperatura_atual= 25.0
        self.temperatura_desejada=25.0

    def ligar_frio(self,temp_desejada=18.0):
         self.ligado=True
         self.modo='Frio'
         self.temperatura_desejada=temp_desejada
         print(f'{self.nome}:Ligado no modo FRIO / Alvo definido para {temp_desejada}')

    def ligar_quente(self, temp_desejada=30):
        self.ligado=True
        self.modo='Quente'
        self.temperatura_desejada=temp_desejada
        print(f'{self.nome}:Ligado no modo QUENTE / Alvo definido para {temp_desejada}')

    def ligar_ambiente(self, temp_desejada=25.0):
        self.ligado=True
        self.modo='Ambiente'
        self.temperatura_desejada=temp_desejada
        print(f'{self.nome}:Ligado no modo AMBIENTE / Alvo definido para {temp_desejada}')

    def estado(self):
         if not self.ligado:
              return 'Desligado'
         return f'Ligado - modo {self.modo}'

    def passagem_tempo(self):
        if not self.ligado:
            variacao = random.choice([-0.2,0.1,0.2])
            self.temperatura_atual += variacao
            return
        if self.temperatura_atual < self.temperatura_desejada:
            self.temperatura_atual +=0.5
            if self.temperatura_atual > self.temperatura_desejada:
                self.temperatura_atual=self.temperatura_desejada
        elif self.temperatura_atual > self.temperatura_desejada:
            self.temperatura_atual -= 0.5
            if self.temperatura_atual < self.temperatura_desejada:
                self.temperatura_atual=self.temperatura_desejada
       

    def desligar(self):
        self.ligado=False
        self.modo='Desligado'
        print(f'{self.nome}: Foi Desligado')
             
class fogao:
    def __init__(self,nome):
        self.nome=nome
        self.ligado=False
        self.modo ='Desligado'
        self.temperatura_atual=25.0
        self.temperatura_desejada=25.0

    def ligar_minimo(self,temp_desejada=160.0):
         self.ligado=True
         self.modo='Mínimo'
         self.temperatura_desejada=temp_desejada
         print(f'{self.nome}:Ligado no fogo Mínimo de temperatura / Alvo definido para {temp_desejada}')

    def ligar_baixo(self,temp_desejada=180.0):
         self.ligado=True
         self.modo='Baixo'
         self.temperatura_desejada=temp_desejada
         print(f'{self.nome}:Ligado no fogo Baixo / Alvo definido para {temp_desejada}')

    def ligar_medio(self,temp_desejada=200.0):
         self.ligado=True
         self.modo='Médio'
         self.temperatura_desejada=temp_desejada
         print(f'{self.nome}:Ligado no fogo Médio / Alvo definido para {temp_desejada}')

    def ligar_alto(self,temp_desejada=250.0):
         self.ligado=True
         self.modo='Alto'
         self.temperatura_desejada=temp_desejada
         print(f'{self.nome}:Ligado no fogo Alto / Alvo definido para {temp_desejada}')

    def desligar(self,temp_desejada=25.0):
         self.ligado=False
         self.modo='Desligado'
         self.temperatura_desejada=temp_desejada
         print(f'{self.nome}:Foi desligado')

    def passagem_tempo(self):
        if self.temperatura_atual < self.temperatura_desejada:
            self.temperatura_atual += 15.0
            if self.temperatura_atual > self.temperatura_desejada:
                self.temperatura_atual = self.temperatura_desejada
        elif self.temperatura_atual > self.temperatura_desejada:
            self.temperatura_atual -= 15.0
            if self.temperatura_atual < self.temperatura_desejada:
                self.temperatura_atual = self.temperatura_desejada

    def estado(self):
         return 'Ligado' if self.ligado else 'Desligado'

class maquina_lavar:
    def __init__ (self,nome):
        self.nome=nome
        self.ligado=False
        self.modo ='Desligado'

    def lavagem_diaria(self):
        self.ligado=True
        self.modo='Lavagem diária'
        print(f'A {self.nome} foi iniciada no Modo {self.modo}')

    def lavagem_rapida(self):
        self.ligado=True
        self.modo='Lavagem Rápida'
        print(f'A {self.nome} foi iniciada no Modo {self.modo}')

    def lavagem_pesada(self):
        self.ligado=True
        self.modo='Lavagem Pesada'
        print(f'A {self.nome} foi iniciada no Modo {self.modo}')

    def desligar(self):
        self.ligado=False
        self.modo='Desligada'
        print(f'A {self.nome} foi Desligada')

    def estado(self):
        return 'Ligado' if self.ligado else 'Desligado'
    
class privada:
    def __init__(self,nome):
        self.nome=nome
        self.ligado=True
        self.modo ='Desligado'
        self.temperatura_atual=17.0
        self.temperatura_desejada=17.0

    def descarga(self):
        self.ligado=True
        self.modo='Descarga'
        print(f'A {self.nome} iníciou a Descarga')

    def aquecimento(self,temp_desejada=25.0):
        self.ligado=True
        self.modo='Aquecimento'
        self.temperatura_desejada=temp_desejada
        print(f'A {self.nome} iníciou o aquecimento do acento ')

    def desligar_aque(self,temp_desejada=17.0):
            self.ligado=False
            self.modo='Desligado'
            self.temperatura_desejada=temp_desejada
            print(f'{self.nome}: O aquecimento foi Desligado')

    def passagem_tempo(self):
        if self.temperatura_atual < self.temperatura_desejada:
            self.temperatura_atual += 0.5
            if self.temperatura_atual > self.temperatura_desejada:
                self.temperatura_atual = self.temperatura_desejada
        elif self.temperatura_atual > self.temperatura_desejada:
            self.temperatura_atual -= 0.5
            if self.temperatura_atual < self.temperatura_desejada:
                self.temperatura_atual = self.temperatura_desejada

    def estado(self):
        return 'Ligado' if self.ligado else 'Desligado'

def menu_rep(variavel, funcao1, funcao2):
     while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Controle: {variavel.nome}')
        print('')
        print(f'Estado: {variavel.estado()}')
        print('1-Ligar    / Abrir')
        print('2-Desligar / Fechar')
        print('3-Sair')
        opcao=input('Opção: ')

        if opcao =='1':
            funcao1()
            salvar_estado(variavel)
        elif opcao =='2':
            funcao2()
            salvar_estado(variavel)
        elif opcao =='3':
            break
        else:
            print('Opção Inválida!')
            input('Pressione enter...')

def quen_frio (varialvel, velocidade_temp=0.5):
        print(f'{varialvel.nome} está ajustando a temperatura')
        while varialvel.temperatura_atual != varialvel.temperatura_desejada:
            varialvel.passagem_tempo()
            print(f'Temperatura atual: {varialvel.temperatura_atual}°C',end='\r',)
            time.sleep(velocidade_temp)
        salvar_temp(varialvel)
        input('Pressione enter para voltar')
     
def ar_condi (variavel):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Controle: {variavel.nome} - temperatura atual: {round(variavel.temperatura_atual,2)}')
        print('')
        print(f'Estado: {variavel.estado()}')
        print('1-Ligar: Modo Quente 30°C')
        print('2-Ligar: Modo Frio 18°C')
        print('3-Ligar: Modo Ambiente')
        print('4-Desligar / Fechar')
        print('5-Sair')
        opcao=input('Opção: ')
        if opcao =='1':
            variavel.ligar_quente()
            salvar_estado(variavel)
            quen_frio(variavel, velocidade_temp=1)
        elif opcao =='2':
            variavel.ligar_frio()
            salvar_estado(variavel)
            quen_frio(variavel, velocidade_temp=1)
        elif opcao =='3':
            variavel.ligar_ambiente()
            salvar_estado(variavel)
            quen_frio(variavel, velocidade_temp=1)
        elif opcao =='4':
            variavel.desligar()
            salvar_estado(variavel)
            print(f'{variavel.nome} foi desligado')
        elif opcao =='5':
            break
        else:
            print('Opção Inválida!')
            input('Pressione enter...')

def fo_gao(variavel):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Controle: {variavel.nome} - temperatura atual: {round(variavel.temperatura_atual,2)}')
        print('')
        print(f'Estado: {variavel.estado()} - Temperatura atual: {variavel.temperatura_atual}')
        print('1-Ligar: Modo Mínimo 160°C')
        print('2-Ligar: Modo Baixo 180°C')
        print('3-Ligar: Modo Médio 200°c')
        print('4-Ligar: Modo Alto 250°C')
        print('5-Desligar / Fechar')
        print('6-Sair')
        opcao=input('Selecione uma opção:')
        if opcao =='1':
            variavel.ligar_minimo()
            salvar_estado(variavel)
            quen_frio(variavel,velocidade_temp=1.5)
        elif opcao =='2':
            variavel.ligar_baixo()
            salvar_estado(variavel)
            quen_frio(variavel,velocidade_temp=1.5)
        elif opcao =='3':
            variavel.ligar_medio()
            salvar_estado(variavel)
            quen_frio(variavel,velocidade_temp=1.5)
        elif opcao =='4':
            variavel.ligar_alto()
            salvar_estado(variavel)
            quen_frio(variavel,velocidade_temp=1.5)
        elif opcao =='5':
            variavel.desligar()
            salvar_estado(variavel)
            quen_frio(variavel,velocidade_temp=1.5)
        elif opcao =='6':
            break
        else:
            print('Opção Inválida!')
            input('Pressione enter...')

def ma_quina(variavel):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Controle: {variavel.nome} - Modo atual {variavel.modo}')
        print('')
        print(f'Estado: {variavel.estado()}')
        print('1-Ligar: Lavagem Diária')
        print('2-Ligar: Lavagem Rápida')
        print('3-Ligar: Lavagem Pesada')
        print('4-Desligar / Fechar')
        print('5-Sair')
        opcao=input('Selecione uma opção:')
        segundos = 0
        if opcao =='1':
            variavel.lavagem_diaria()
            salvar_estado(variavel)
            segundos = 15
        elif opcao =='2':
            variavel.lavagem_rapida()
            salvar_estado(variavel)
            segundos = 8
        elif opcao =='3':
            variavel.lavagem_pesada()
            salvar_estado(variavel)
            segundos = 25
        elif opcao =='4':
            variavel.desligar()
            salvar_estado(variavel)
        elif opcao =='5':
            break
        else:
            print('Opção Inválida!')
            input('Pressione enter...')

        if segundos > 0:
            salvar_estado(variavel)
            for restante in range(segundos,0,-1):
                print(f'Tempo restante: {restante}s', end='\r')
                time.sleep(1)
            variavel.desligar()
            salvar_estado(variavel)
            print('Lavagem concluida!')
            input('Pressione enterpara voltar...')

def pri_vada (variavel):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Controle: {variavel.nome} - temperatura atual: {round(variavel.temperatura_atual,2)}')
        print('')
        print(f'Estado: {variavel.estado()} - Temperatura atual: {variavel.temperatura_atual}')
        print('1-Ligar: Descarga')
        print('2-Ligar: Aquecimento')
        print('5-Desligar / Fechar')
        print('6-Sair')
        opcao=input('Selecione uma opção:')
        segundos = 0
        if opcao =='1':
            variavel.descarga()
            salvar_estado(variavel)
            segundos = 7
        elif opcao =='2':
            variavel.aquecimento()
            salvar_estado(variavel)
            quen_frio(variavel,velocidade_temp=1.5)
        elif opcao =='5':
            variavel.desligar_aque()
            salvar_estado(variavel)
            quen_frio(variavel,velocidade_temp=1.5)
        elif opcao =='6':
            break
        else:
            print('Opção Inválida!')
            input('Pressione enter...')

        if segundos > 0:
            salvar_estado(variavel)
            for restante in range(segundos,0,-1):
                print(f'Tempo restante: {restante}s', end='\r')
                time.sleep(1)
            variavel.desligar_aque()
            salvar_estado(variavel)
            print('Lavagem concluida!')
            input('Pressione enterpara voltar...')

def menu_como(dicio,comodo,obj_ar=None,obj_fo=None,obj_ma=None,obj_pri=None):
    aparelhos= {}
    contador=1
    for dados in dicio.values():
        if dados[0] not in (obj_ar,obj_fo, obj_ma, obj_pri):
            aparelhos[str(contador)] = dados
            contador += 1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if obj_ar is not None:
            obj_ar.passagem_tempo()

        print(f'-{comodo}-')
        for chave, dados in aparelhos.items():
            objeto = dados[0]
            print(f'{chave} - {objeto.nome} está: {objeto.estado()}')

        if obj_ar is not None:
            print(f'AR - {obj_ar.nome} está: {obj_ar.estado()} - temperatura: {round(obj_ar.temperatura_atual, 2)}')
        if obj_fo is not None:
            print(f'FG - {obj_fo.nome} está: {obj_fo.estado()} - temperatura: {round(obj_fo.temperatura_atual, 2)}')
        if obj_pri is not None:
            print(f'PR - {obj_pri.nome} está: {obj_pri.estado()} - temperatura: {round(obj_pri.temperatura_atual, 2)}')
        if obj_ma is not None:
            print(f'MA - {obj_ma.nome} está no modo: {obj_ma.modo}')
        print('V - Voltar ao menu inicial')

        opcao = input('Selecione um aparelho: ').strip().upper()

        if opcao in aparelhos:
            item = aparelhos[opcao]
            menu_rep(item[0], item[1], item[2])
        elif opcao == 'AR' and obj_ar is not None:
            ar_condi(obj_ar)
        elif opcao == 'FG' and obj_fo is not None:
            fo_gao(obj_fo)
        elif opcao == 'PR' and obj_pri is not None:
            pri_vada(obj_pri)
        elif opcao =='MA' and obj_ma is not None:
            ma_quina(obj_ma)
        elif opcao == 'V':
            break
        else:
            print('Opção Inválida')
            input('Pressione enter...')

def como_banco(nome_comodo):
    conexao=conectar_banco()
    cursor= conexao.cursor(dictionary=True)

    sql = 'select disp_id, disp_nome, disp_tipo, disp_status, disp_temperatura from dispositivo_smart where disp_comodo = %s order by disp_id'
    cursor.execute(sql, (nome_comodo,))
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    dicionario_aparelhos = {}
    contador=1

    for lista in resultado:
        nome_disp = lista['disp_nome']
        tipo_disp = lista['disp_tipo']
        status_disp = lista['disp_status']

        ligado = status_disp.startswith (('Ligada','Ligado','Aberta'))

        if tipo_disp =='luz':
            objeto = luz(nome_disp)
            objeto.ligada =ligado
            funcao_liga=objeto.ligar
            funcao_desliga=objeto.desligar

        elif tipo_disp=='tv':
            objeto = tv(nome_disp)
            objeto.ligada =ligado
            funcao_liga=objeto.ligar
            funcao_desliga=objeto.desligar

        elif tipo_disp=='porta':
            objeto = porta(nome_disp)
            objeto.ligada =ligado
            funcao_liga=objeto.aberta
            funcao_desliga=objeto.fechada

        elif tipo_disp=='janela':
            objeto = janela(nome_disp)
            objeto.ligada =ligado
            funcao_liga=objeto.aberta
            funcao_desliga=objeto.fechada

        elif tipo_disp=='cortina':
            objeto = cortina(nome_disp)
            objeto.ligada =ligado
            funcao_liga=objeto.aberta
            funcao_desliga=objeto.fechada

        elif tipo_disp=='arcondicionado':
            objeto = arcondicionado(nome_disp)
            objeto.ligado =ligado
            restaurar_modo(objeto, status_disp)
            if lista['disp_temperatura'] is not None:
                objeto.temperatura_atual=lista['disp_temperatura']
            funcao_liga= None
            funcao_desliga=objeto.desligar


        elif tipo_disp=='fogao':
                objeto = fogao(nome_disp)
                objeto.ligado =ligado
                if lista['disp_temperatura'] is not None:
                    objeto.temperatura_atual=lista['disp_temperatura']
                funcao_liga= None
                funcao_desliga=objeto.desligar

        elif tipo_disp=='maquina':
                objeto = maquina_lavar(nome_disp)
                objeto.ligado =ligado
                funcao_liga= None
                funcao_desliga=objeto.desligar

        elif tipo_disp=='privada':
                objeto = privada(nome_disp)
                objeto.ligado =ligado
                if lista['disp_temperatura'] is not None:
                    objeto.temperatura_atual=lista['disp_temperatura']
                funcao_liga= None
                funcao_desliga=objeto.desligar_aque

        else:
            continue
        objeto.disp_id = lista['disp_id']
        dicionario_aparelhos[lista['disp_id']]= [objeto,funcao_liga,funcao_desliga]

    return dicionario_aparelhos

def salvar_estado(objeto):
    status = objeto.estado()
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql='update dispositivo_smart set disp_status = %s where disp_id = %s'
    cursor.execute(sql,(status,objeto.disp_id))

    conexao.commit()
    cursor.close()
    conexao.close()

def salvar_temp(objeto):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql='update dispositivo_smart set disp_temperatura = %s where disp_id = %s'
    cursor.execute(sql,(objeto.temperatura_atual,objeto.disp_id))

    conexao.commit()
    cursor.close()
    conexao.close()

#Vic funções

MAX_USUARIOS = 5
POSICOES = ('ADMINISTRADOR', 'MORADOR')
 
CAMPOS = {
    '1': ('usuario_nome',    'Nome'),
    '2': ('usuario_login',   'Login'),
    '3': ('usuario_senha',   'Senha'),
    '4': ('usuario_posicao', 'Posição'),
}
 
CAMPOS_MORADOR = {k: v for k, v in CAMPOS.items() if v[0] != 'usuario_posicao'}

def consultar(comando, valores=()):
    conexao = conectar_banco()
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(comando, valores)
        return cursor.fetchall()
    finally:
        conexao.close()

def executar(comando, valores=()):
    conexao = conectar_banco()
    try:
        cursor = conexao.cursor()
        cursor.execute(comando, valores)
        conexao.commit()
        return cursor.rowcount
    finally:
        conexao.close()

def fazer_login(login, senha):
    linhas = consultar(
        'SELECT usuario_id, usuario_nome, usuario_login, usuario_senha, usuario_posicao '
        'FROM usuario WHERE usuario_login = %s',
        (login,)
    )
    if not linhas:
        return None
    usuario = linhas[0]
    if not check_password_hash(usuario['usuario_senha'], senha):
        return None
    usuario.pop('usuario_senha')
    return usuario

def listar_usuarios_db():
    return consultar(
        'SELECT usuario_id, usuario_nome, usuario_posicao FROM usuario '
        'ORDER BY usuario_id'
    )
 
def buscar_usuario(usuario_id):
    linhas = consultar(
        'SELECT usuario_id, usuario_nome, usuario_posicao FROM usuario '
        'WHERE usuario_id = %s',
        (usuario_id,)
    )
    return linhas[0] if linhas else None
 
def contar_usuarios():
    return consultar('SELECT COUNT(*) AS total FROM usuario')[0]['total']
 
def contar_admins():
    return consultar(
        "SELECT COUNT(*) AS total FROM usuario "
        "WHERE UPPER(usuario_posicao) = 'ADMINISTRADOR'"
    )[0]['total']
 
def cadastrar_usuario_db(nome, login, senha, posicao):
    return executar(
        'INSERT INTO usuario (usuario_nome, usuario_login, usuario_senha, usuario_posicao) '
        'VALUES (%s, %s, %s, %s)',
        (nome, login, generate_password_hash(senha), posicao)
    )
  
def remover_usuario_db(usuario_id):
    return executar('DELETE FROM usuario WHERE usuario_id = %s', (usuario_id,))
 
def atualizar_usuario(usuario_id, coluna, novo_valor):
    if coluna == 'usuario_senha':
        novo_valor=generate_password_hash(novo_valor)
    return executar(
        f'UPDATE usuario SET {coluna} = %s WHERE usuario_id = %s',
        (novo_valor, usuario_id)
    )
 
def eh_admin(usuario):
    return usuario['usuario_posicao'].upper() == 'ADMINISTRADOR'
 
def mostrar_perfil(usuario_logado):
    print('--- Meu perfil ---')
    print(f"Nome: {usuario_logado['usuario_nome']}")
    print(f"Login: {usuario_logado['usuario_login']}")
    print(f"Posição: {usuario_logado['usuario_posicao']}")
 
def acao_listar():
    print('--- Usuários ---')
    usuarios = listar_usuarios_db()
    if not usuarios:
        print('Nenhum usuário cadastrado.')
    for u in usuarios:                      
        print(f"{u['usuario_id']} - {u['usuario_nome']} ({u['usuario_posicao']})")
 
def acao_cadastrar():
    print('')
    print('Cadastrando novo usuário...')
    if contar_usuarios() >= MAX_USUARIOS:
        print(f'Limite de {MAX_USUARIOS} usuários atingido.')
        return
 
    usuario_nome = input('Entre com o nome do Usuário: ').strip()
    usuario_login = input('Entre com o login do Usuário: ').strip()
    usuario_senha = getpass.getpass('Entre com a senha do Usuário: ').strip()
    usuario_posicao = input('Entre com a posição do Usuário (ADMINISTRADOR/MORADOR): ').strip().upper()
 
    if usuario_nome == '' or usuario_login == '' or usuario_senha == '' or usuario_posicao == '':
        print('Nenhuma inserção de dados pode ficar vazio.')
    elif usuario_posicao not in POSICOES:
        print('Posição inválida. Use ADMINISTRADOR ou MORADOR.')
    else:
        try:
            cadastrar_usuario_db(usuario_nome, usuario_login, usuario_senha, usuario_posicao)
        except mysql.connector.IntegrityError:
            print('Esse login já está em uso.')
        else:
            print('')
            print(f'Novo Usuário {usuario_nome} inserido com sucesso!')
            print('')
 
def acao_remover(usuario_logado):
    print('')
    print('Removendo usuário...')
    usuario_id = input('Entre com o ID do Usuário a ser removido: ').strip()
 
    if not usuario_id.isdigit():
        print('')
        print('Informe um ID numérico.')
        return
 
    alvo = buscar_usuario(usuario_id)
    if alvo is None:
        print('ID inexistente.')
    elif alvo['usuario_id'] == usuario_logado['usuario_id']:
        print('Você não pode remover a si mesmo.')
    elif alvo['usuario_posicao'].upper() == 'ADMINISTRADOR' and contar_admins() <= 1:
        print('Não é possível remover o único administrador.')
    else:
        remover_usuario_db(usuario_id)
        print('')
        print(f'Usuário com ID {usuario_id} removido com sucesso!')
        print('')
 
def acao_alterar():
    print('')
    print('Alterando dados do usuário...')
    print('')
    usuario_id = input('Entre com o ID do Usuário a ser alterado: ').strip()
 
    if not usuario_id.isdigit():
        print('Informe um ID numérico.')
        return
 
    alvo = buscar_usuario(usuario_id)
    if alvo is None:
        print('ID inexistente.')
        return
 
    print('Campos disponíveis para alteração:')
    for key, value in CAMPOS.items():
        print(f'{key} - {value[1]}')
    campo = input('Escolha o campo a ser alterado (número): ').strip()
 
    if campo not in CAMPOS:
        print('Campo inválido.')
        return
 
    coluna, rotulo = CAMPOS[campo]
    novo_valor = input(f'Entre com o novo valor para {rotulo}: ').strip()
 
    if novo_valor == '':
        print('Nenhuma inserção de dados pode ficar vazio.')
        return
 
    if coluna == 'usuario_posicao':
        novo_valor = novo_valor.upper()
        if novo_valor not in POSICOES:
            print('Posição inválida. Use ADMINISTRADOR ou MORADOR.')
            return
        if (novo_valor == 'MORADOR'
                and alvo['usuario_posicao'].upper() == 'ADMINISTRADOR'
                and contar_admins() <= 1):
            print('Não é possível rebaixar o único administrador.')
            return
 
    try:
        linhas = atualizar_usuario(usuario_id, coluna, novo_valor)
    except mysql.connector.IntegrityError:
        print('Esse login já está em uso.')
    else:
        if linhas == 0:
            print('Nada foi alterado (o valor já era esse).')
        else:
            print('')
            print(f'Usuário com ID {usuario_id} atualizado com sucesso!')
            print('')
 
def acao_atualizar_meus_dados(usuario_logado):
    print('')
    print('Atualizando meus dados...')
    print('Campos disponíveis para alteração:')
    for key, value in CAMPOS_MORADOR.items():
        print(f'{key} - {value[1]}')
    campo = input('Escolha o campo a ser alterado (número): ').strip()
 
    if campo not in CAMPOS_MORADOR:
        print('Campo inválido.')
        return
 
    coluna, rotulo = CAMPOS_MORADOR[campo]
    novo_valor = input(f'Entre com o novo valor para {rotulo}: ').strip()
    if novo_valor == '':
        print('Nenhuma inserção de dados pode ficar vazio.')
        return
 
    try:
        linhas = atualizar_usuario(usuario_logado['usuario_id'], coluna, novo_valor)
    except mysql.connector.IntegrityError:
        print('Esse login já está em uso.')
    else:
        if linhas == 0:
            print('Nada foi alterado (o valor já era esse).')
        else:
            if coluna == 'usuario_nome':
                usuario_logado['usuario_nome'] = novo_valor
            print('')
            print('Seus dados foram atualizados com sucesso!')
            print('')
 
def acao_excluir_minha_conta(usuario_logado):
    print('Excluindo minha conta...')
    if eh_admin(usuario_logado) and contar_admins() <= 1:
        print('Você é o único administrador. Promova outro usuário antes de excluir a conta.')
        return False
    
    print('ATENÇÃO: isso apaga a sua conta e não pode ser desfeito.')
    confirmacao = input('Digite EXCLUIR para confirmar: ').strip()
 
    if confirmacao != 'EXCLUIR':
        print('Operação cancelada.')
        return False
 
    remover_usuario_db(usuario_logado['usuario_id'])
    print('Sua conta foi excluída. Saindo...')
    return True

def acao_consultar_dispositivos():
    print('--- Dispositivos ---')
    dispositivos = consultar(
        'SELECT disp_id, disp_nome, disp_tipo, disp_status, disp_comodo FROM dispositivo_smart '
        'ORDER BY disp_id'
    )
    if not dispositivos:
        print('Nenhum dispositivo cadastrado.')
    for d in dispositivos:
        print(f"{d['disp_id']} - {d['disp_nome']} ({d['disp_tipo']}) - Status: {d['disp_status']} - Cômodo: {d['disp_comodo']}")

def acao_cadastrar_dispositivo():
    print('')
    print('Cadastrando novo dispositivo...')
    disp_nome = input('Entre com o nome do Dispositivo: ').strip()
    disp_tipo = input('Entre com o tipo do Dispositivo: ').strip()
    disp_status = input('Entre com o status do Dispositivo: ').strip().upper()
    disp_comodo = input('Entre com o cômodo do Dispositivo: ').strip()

    if disp_nome == '' or disp_tipo == '' or disp_status == '' or disp_comodo == '':
        print('Nenhuma inserção de dados pode ficar vazio.')
    else:
        try:
            executar(
                'INSERT INTO dispositivo_smart (disp_nome, disp_tipo, disp_status, disp_comodo) '
                'VALUES (%s, %s, %s, %s)',
                (disp_nome, disp_tipo, disp_status, disp_comodo)
            )
        except mysql.connector.Error as erro:
            print(f'Erro ao cadastrar dispositivo: {erro}')
        else:
            print('')
            print(f'Novo Dispositivo {disp_nome} inserido com sucesso!')
            print('')

def acao_remover_dispositivo():
    print('')
    print('Removendo dispositivo...')
    disp_id = input('Entre com o ID do Dispositivo a ser removido: ').strip()

    if not disp_id.isdigit():
        print('')
        print('Informe um ID numérico.')
        return

    linhas = executar('DELETE FROM dispositivo_smart WHERE disp_id = %s', (disp_id,))
    if linhas == 0:
        print('ID inexistente.')
    else:
        print('')
        print(f'Dispositivo com ID {disp_id} removido com sucesso!')
        print('')

def acao_consultar_comodos():
    print('--- Cômodos ---')
    comodos = consultar(
        'SELECT disp_comodo, COUNT(*) AS total FROM dispositivo_smart '
        'GROUP BY disp_comodo ORDER BY disp_comodo'
    )
    if not comodos:
        print('Nenhum cômodo cadastrado.')
    for c in comodos:
        print(f"- {c['disp_comodo']} ({c['total']} dispositivos)")

def acao_consultar_dispositivos_sala():
    print('')
    print('--- Dispositivos na Sala ---')
    dispositivos = consultar(
        'SELECT disp_id, disp_nome, disp_tipo, disp_status, disp_comodo FROM dispositivo_smart '
        'WHERE disp_comodo = %s ORDER BY disp_id',
        ('Sala',)
    )
    if not dispositivos:
        print('Nenhum dispositivo cadastrado na Sala.')
    for d in dispositivos:
        print(f"{d['disp_id']} - {d['disp_nome']} ({d['disp_tipo']}) - Status: {d['disp_status']}")

def acao_consultar_dispositivos_cozinha():
    print('')
    print('--- Dispositivos na Cozinha ---')
    dispositivos = consultar(
        'SELECT disp_id, disp_nome, disp_tipo, disp_status, disp_comodo FROM dispositivo_smart '
        'WHERE disp_comodo = %s ORDER BY disp_id',
        ('Cozinha',)
    )
    if not dispositivos:
        print('Nenhum dispositivo cadastrado na Cozinha.')
    for d in dispositivos:
        print(f"{d['disp_id']} - {d['disp_nome']} ({d['disp_tipo']}) - Status: {d['disp_status']}")

def acao_consultar_dispositivos_quarto_crianças():
    print('')
    print('--- Dispositivos no Quarto das Crianças ---')
    dispositivos = consultar(
        'SELECT disp_id, disp_nome, disp_tipo, disp_status, disp_comodo FROM dispositivo_smart '
        'WHERE disp_comodo = %s ORDER BY disp_id',
        ('Quarto das Crianças',)
    )
    if not dispositivos:
        print('Nenhum dispositivo cadastrado no Quarto das Crianças.')
    for d in dispositivos:
        print(f"{d['disp_id']} - {d['disp_nome']} ({d['disp_tipo']}) - Status: {d['disp_status']}")

def acao_consultar_dispositivos_quarto_adultos():
    print('')
    print('--- Dispositivos no Quarto dos Adultos ---')
    dispositivos = consultar(
        'SELECT disp_id, disp_nome, disp_tipo, disp_status, disp_comodo FROM dispositivo_smart '
        'WHERE disp_comodo = %s ORDER BY disp_id',
        ('Quarto dos Adultos',)
    )
    if not dispositivos:
        print('Nenhum dispositivo cadastrado no Quarto dos Adultos.')
    for d in dispositivos:
        print(f"{d['disp_id']} - {d['disp_nome']} ({d['disp_tipo']}) - Status: {d['disp_status']}")

def acao_consultar_dispositivos_banheiro():
    print('')
    print('--- Dispositivos no Banheiro ---')
    dispositivos = consultar(
        'SELECT disp_id, disp_nome, disp_tipo, disp_status, disp_comodo FROM dispositivo_smart '
        'WHERE disp_comodo = %s ORDER BY disp_id',
        ('Banheiro',)
    )
    if not dispositivos:
        print('Nenhum dispositivo cadastrado no Banheiro.')
    for d in dispositivos:
        print(f"{d['disp_id']} - {d['disp_nome']} ({d['disp_tipo']}) - Status: {d['disp_status']}")

def acao_consultar_dispositivos_lavanderia():
    print('')
    print('--- Dispositivos na Lavanderia ---')
    dispositivos = consultar(
        'SELECT disp_id, disp_nome, disp_tipo, disp_status, disp_comodo FROM dispositivo_smart '
        'WHERE disp_comodo = %s ORDER BY disp_id',
        ('Lavanderia',)
    )
    if not dispositivos:
            print('Nenhum dispositivo cadastrado na Lavanderia.')
    for d in dispositivos:
            print(f"{d['disp_id']} - {d['disp_nome']} ({d['disp_tipo']}) - Status: {d['disp_status']}")

print('='*19)
print('SMART HOUSE A.R.C.A')
print('='*19)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--Login A.R.C.A--')
    login=input('Usuário: ').strip()
    senha=getpass.getpass('Senha: ').strip()
    usuario_logado=fazer_login(login,senha)

    if usuario_logado is not None:
        break
    print('Login ou senha incorretos...')
    input('Pressione enter...')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Bem-vindo {usuario_logado['usuario_nome']}!")
    print('--Menu A.R.C.A--')
    print('                                 ')
    print('========================')
    print('  Selecione uma Opção  ')
    print('========================')
    print('                                 ')
    print('--- Menu de Usuários ---')
    print('007-Ver meu perfil')
    print('008-Ver meus recordes')
    print('009-Ranking')
    print('')
    print('Qual cômodo será acessado?')
    print('1-Sala')
    print('2-Cozinha')
    print('3-Quarto das Crianças')
    print('4-Quarto dos Adultos')
    print('5-Banheiro')
    print('6-Lavanderia')
    if eh_admin (usuario_logado):
        print('')
        print('~~~ Menu de Administrador ~~~')
        print('7-Listar usuários')
        print('8-Cadastrar novo usuário')
        print('9-Alterar dados do usuário')
        print('10-Remover usuário')
        print('11-Listar dispositivos')
        print('12-Listar comodos')
        print('13-Listar dispositivos por comodo')
        print('14-Cadastrar dispositivo')
        print('15-Excluir dispositivo')
        print('16-Excluir conta')
    print('0-sair')
    print('')
    opcao=input('Opção: ')
    if opcao == '1':
        dicio_sala= como_banco('Sala')
        objeto_ar_sala=None
        for chave, dados in dicio_sala.items():
            if isinstance(dados[0], arcondicionado):
                objeto_ar_sala=dados[0]
                break
        menu_como(dicio_sala,'Sala',objeto_ar_sala,None,None,None)
    elif opcao =='2':
        dicio_cozinha=como_banco('Cozinha')
        objeto_fogao=None
        for chave, dados in dicio_cozinha.items():
            if isinstance(dados[0], fogao):
                objeto_fogao=dados[0]
                break
        menu_como(dicio_cozinha,'Cozinha',None,objeto_fogao,None,None)
    elif opcao == '3':
        dicio_cri=como_banco('Quarto das Crianças')
        objeto_ar_quartocri=None
        for chave, dados in dicio_cri.items():
            if isinstance(dados[0], arcondicionado):
                objeto_ar_quartocri=dados[0]
                break
        menu_como(dicio_cri,'Quarto das Crianças',objeto_ar_sala,None,None,None)
    elif opcao=='4':
        dicio_adul=como_banco('Quartos dos Adultos')
        objeto_ar_quartoadul=None
        for chave, dados in dicio_adul.items():
            if isinstance(dados[0], arcondicionado):
                objeto_ar_quartoadul=dados[0]
                break
        menu_como(dicio_adul,'Quartos dos Adultos',objeto_ar_sala,None,None,None)
    elif opcao=='5':
        dicio_banheiro=como_banco('Banheiro')
        objeto_privada=None
        for chave, dados in dicio_banheiro.items():
            if isinstance(dados[0], privada):
                objeto_privada=dados[0]
                break
        menu_como(dicio_banheiro,'Banheiro',None,None,None,objeto_privada)
    elif opcao == '6':
        dicio_lavanderia=como_banco('Lavanderia')
        objeto_maquina=None
        for chave, dados in dicio_lavanderia.items():
            if isinstance(dados[0], maquina_lavar):
                objeto_maquina=dados[0]
                break
        menu_como(dicio_lavanderia,'Lavanderia',None,None,objeto_maquina,None)

# vic elifs
    elif opcao == '007':
            mostrar_perfil(usuario_logado)
            input('Pressione enter para voltar...')
    elif opcao in ('008', '009'):
                print('Função ainda não implementada.')
                input('Pressione enter para voltar...')
    elif opcao == '7' and eh_admin(usuario_logado):
                acao_listar()
                input('Pressione enter para voltar...')
    elif opcao == '8' and eh_admin(usuario_logado):
                acao_cadastrar()
                input('Pressione enter para voltar...')
    elif opcao == '9' and eh_admin(usuario_logado):
                acao_listar()
                acao_alterar()
                input('Pressione enter para voltar...')
    elif opcao == '10' and eh_admin(usuario_logado):
                acao_listar()
                acao_remover(usuario_logado)
                input('Pressione enter para voltar...')
    elif opcao == '11' and eh_admin(usuario_logado):
                acao_consultar_dispositivos()
                input('Pressione enter para voltar...')
    elif opcao == '12' and eh_admin(usuario_logado):
                acao_consultar_comodos()
                input('Pressione enter para voltar...')
    elif opcao == '13' and eh_admin(usuario_logado):
        acao_consultar_comodos()
        print('')
        print('Qual cômodo deseja consultar? ')
        como_disp= input('-> ').strip()
        if como_disp == 'Sala':
            acao_consultar_dispositivos_sala()
            input('Pressione enter para voltar...')
        elif como_disp == 'Cozinha':
            acao_consultar_dispositivos_cozinha()
            input('Pressione enter para voltar...')
        elif como_disp == 'Quarto das Crianças':
            acao_consultar_dispositivos_quarto_crianças()
            input('Pressione enter para voltar...')
        elif como_disp == 'Banheiro':
            acao_consultar_dispositivos_banheiro()
            input('Pressione enter para voltar...')
        elif como_disp == 'Lavanderia':
            acao_consultar_dispositivos_lavanderia()
            input('Pressione enter para voltar...')
        elif como_disp == 'Quarto dos Adultos':
            acao_consultar_dispositivos_quarto_adultos()
            input('Pressione enter para voltar...')
        else:
            print('Cômodo inválido...')
            input('Pressione enter para voltar...')
    elif opcao == '14' and eh_admin(usuario_logado):  
        acao_consultar_comodos()
        acao_cadastrar_dispositivo()
        input('Pressione enter para voltar...')
    elif opcao == '15' and eh_admin(usuario_logado):
        acao_consultar_dispositivos()
        acao_remover_dispositivo()
        input('Pressione enter para voltar...')
    elif opcao == '16' and eh_admin(usuario_logado):
        if acao_excluir_minha_conta(usuario_logado):
            break
        input('Pressione enter para voltar...')
    elif opcao == '0':
        break        
    else:          
        print('Acesso Negado')
        input('Clique enter para retornar ao menu...')        
    #except ValueError:
        #input('Login ou senha inválidos...')