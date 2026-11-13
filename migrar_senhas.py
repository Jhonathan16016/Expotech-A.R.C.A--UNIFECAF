import getpass
import mysql.connector
from werkzeug.security import generate_password_hash

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password=getpass.getpass('Senha do MySQL: '),
    database='ARCA'
)
cursor = conexao.cursor()

cursor.execute('SELECT usuario_id, usuario_senha FROM usuario')
convertidas = 0
for usuario_id, senha in cursor.fetchall():
    if senha.startswith('scrypt:'):
        continue
    cursor.execute(
        'UPDATE usuario SET usuario_senha = %s WHERE usuario_id = %s',
        (generate_password_hash(senha, method='scrypt'), usuario_id)
    )
    convertidas += 1

conexao.commit()
conexao.close()
print(f'{convertidas} senha(s) convertida(s).')