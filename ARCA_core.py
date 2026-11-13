import random
import mysql.connector
import os
import time
from werkzeug.security import generate_password_hash, check_password_hash

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
        if not self.ligado:
            return 'Desligado'
        return f'Ligado - modo {self.modo}'

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
        if not self.ligado:
            return 'Desligado'
        return f'Ligado - modo {self.modo}'
    
class privada:

    def __init__(self,nome):
        self.nome=nome
        self.ligado=False
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
        if not self.ligado:
            return 'Desligado'
        return f'Ligado - modo {self.modo}'    

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

ALVOS = {'Frio': 18.0, 'Quente': 30.0, 'Ambiente': 25.0,
        'Mínimo': 160, 'Baixo': 180.0, 'Médio': 200.0, 'Alto': 250.0,
        'Aquecimento': 25.0}

def restaurar_modo(objeto, status_disp):
    if objeto.ligado and ' - modo ' in status_disp:
        modo=status_disp.split(' - modo ')[1].strip()
        objeto.modo=modo
        if hasattr(objeto, 'temperatura_desejada'):
            objeto.temperatura_desejada = ALVOS.get(modo, objeto.temperatura_desejada)

def como_banco(nome_comodo):
    conexao=conectar_banco()
    cursor= conexao.cursor(dictionary=True)

    sql = 'select disp_id, disp_nome, disp_tipo, disp_status, disp_temperatura from dispositivo_smart where disp_comodo = %s order by disp_id'
    cursor.execute(sql, (nome_comodo,))
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    dicionario_aparelhos = {}

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
                restaurar_modo(objeto, status_disp)
                if lista['disp_temperatura'] is not None:
                    objeto.temperatura_atual=lista['disp_temperatura']
                funcao_liga= None
                funcao_desliga=objeto.desligar

        elif tipo_disp=='maquina':
                objeto = maquina_lavar(nome_disp)
                objeto.ligado =ligado
                restaurar_modo(objeto, status_disp)
                funcao_liga= None
                funcao_desliga=objeto.desligar

        elif tipo_disp=='privada':
                objeto = privada(nome_disp)
                objeto.ligado =ligado
                restaurar_modo(objeto, status_disp)
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

def cadastrar_usuario_db(nome, login, senha, posicao):
    return executar(
        'INSERT INTO usuario (usuario_nome, usuario_login, usuario_senha, usuario_posicao) '
        'VALUES (%s, %s, %s, %s)',
        (nome, login, generate_password_hash(senha), posicao)
    )

def atualizar_usuario(usuario_id, coluna, novo_valor):
    if coluna == 'usuario_senha':
        novo_valor=generate_password_hash(novo_valor)
    return executar(
        f'UPDATE usuario SET {coluna} = %s WHERE usuario_id = %s',
        (novo_valor, usuario_id)
    )

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

def remover_usuario_db(usuario_id):
    return executar('DELETE FROM usuario WHERE usuario_id = %s', (usuario_id,))

POSICOES=('ADMINISTRADOR', 'MORADOR')

def login_existe(login):
    return bool(consultar('select 1 from usuario where usuario_login = %s', (login,)))

def eh_admin(usuario):
    return usuario['usuario_posicao'].upper() == 'ADMINISTRADOR'