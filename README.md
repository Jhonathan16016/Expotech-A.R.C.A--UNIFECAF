# A.R.C.A (Automação Residencial, Controle e Arcade)

Projeto desenvolvido para a **ExpoTech - UniFECAF**, unindo automação residencial e nostalgia com emulação de jogos diretamente na plataforma.

## Descrição
O A.R.C.A é uma plataforma centralizada para o controle e gerenciamento de uma casa inteligente, unindo praticidade no dia a dia e entretenimento. O sistema permite consultar moradores cadastrados e seus respectivos níveis de permissão, realizar o cadastro de novos usuários, atualizar registros e controlar aparelhos conectados de forma organizada.

Com foco na eficiência, segurança e usabilidade, a aplicação busca otimizar o gerenciamento residencial e facilitar o acesso aos controles da casa e a uma central de jogos retrô (arcade) por meio de uma interface simples e intuitiva. O projeto demonstra na prática a integração entre programação backend, banco de dados e interfaces web para criar uma experiência completa de automação e lazer doméstico.

## Requisitos para execução

Flask:
pip install Flask

Conector do MySQL:
pip install mysql-connector-python

**Colocar os comandos para usar sua senha no banco de dados**
Configuração do acesso ao banco
Abra o Prompt de Comando, PowerShell ou terminal do VS Code e execute:

setx ARCA_DB_USER "SEU_USUARIO_MYSQL"  

(Substitua SEU_USUARIO_MYSQL pelo usuário que você usa para acessar o MySQL)
Exemplo:
setx ARCA_DB_USER "root"

Depois configure sua senha:

setx ARCA_DB_PASSWORD "sua-senha-aqui"

exemplo:
setx ARCA_DB_PASSWORD "123456"

Observação importante:

ARCA_DB_USER é o usuário do MySQL (ex.: root).
Não use localhost aqui.
O endereço localhost já está configurado no sistema e indica onde o servidor MySQL está rodando.

Após executar os comandos, feche e abra novamente o terminal antes de iniciar o sistema.

## Requisitos para colocar jogos no emulatorJS

Ir no arquivo app.py procurar a linha de código

JOGOS = {
      'jogo':{'nome': 'nome do jogo', 'core': 'core do jogo', 'arquivo': 'arquivo do jogo'},
}

Depois altere os caminhos para se adequar ao seu jogo escolhido.
confira o core do jogo no site do emulatorJS [https://emulatorjs.org/docs4devs/cores] ou veja no arquivo emulatorjs.

## Tecnologias Utilizadas

Python
Flask
Werkzeug Security (criptografia de senhas com hash)
HTML5, CSS e JavaScript (atualizações dinâmicas e consumo de rotas)
MySQL (integração via `mysql-connector-python`)
**Módulo Arcade (Emulação):** [EmulatorJS](https://emulatorjs.org/)

## Credenciais de Teste

**Admins**

Usuário: Samantha.So / Senha: sam1980
Usuário: Fernando.Ka / Senha: fer1978 

**Moradores**

Usuário: Raoni.So / Senha: rao2018
Usuário: Moara.So / Senha: moa2018

## Observação:

Todas as credenciais e informações presentes no sistema são fictícias e foram criadas exclusivamente para fins acadêmicos e de demonstração.

## Créditos e Atribuições de Terceiros

Este projeto utiliza componentes de código aberto e recursos de audios criados pela comunidade. Todos os direitos autorais permanecem com seus respectivos criadores:

### Sistema de Emulação (Módulo Arcade)
* **Projeto:** [EmulatorJS](https://emulatorjs.org/)
* **Atribuição:** Utilizado como núcleo e interface para emulação de jogos diretamente no navegador.
* **Licença:** Distribuído sob a **GNU General Public License v3.0 (GPL-3.0)**, em conformidade com o arquivo [LICENSE](./LICENSE) deste repositório.

### 🎵 Trilhas Sonoras e Efeitos Sonoros
* **Plataforma:** [Pixabay](https://pixabay.com/)
* **Atribuição:** As músicas utilizadas na interface foram obtidos gratuitamente através do banco de mídia do Pixabay.

* **Autor das músicas:** DJARTMUSIC - Link do perfil no pixabay [https://pixabay.com/users/djartmusic-46653586/]

