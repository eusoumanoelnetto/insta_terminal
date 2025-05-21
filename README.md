<p align="center">
  <img src="assets/banner.png" alt="Insta Terminal Banner" />
</p>

![Insta Terminal](https://img.shields.io/badge/InstaTerminal-BlackMirror%20Mode-000000?style=for-the-badge&logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

# 🚀 Insta Terminal 🔍  
🧠 Ferramenta de Consulta de Perfis do Instagram via Terminal — **Estilo Hacker Black Mirror**

---

## 📑 Descrição

O **Insta Terminal** é uma aplicação em Python que permite consultar informações públicas de perfis do Instagram diretamente pelo terminal.

Feito pra quem gosta daquele ar de hacker, com efeito de digitação, telinha preta, vibes cyberpunk e comandos que parecem coisa de filme futurista.  

Apesar do clima descontraído, o projeto segue boas práticas de desenvolvimento, organização de pacotes e testes, simulando um software real de produção.

---

## 🎯 Funcionalidades

- 🔍 Consulta dados públicos de qualquer perfil:
  - ✅ Nome completo
  - ✅ Biografia
  - ✅ Quantidade de posts
  - ✅ Seguidores
  - ✅ Seguindo
  - ✅ Verifica se é privado
  - ✅ Verifica se é verificado
- 📥 Download da foto de perfil e das postagens (apenas se for público)
- 🧠 Terminal interativo com animações estilo *Black Mirror*
- ⚙️ Código limpo, modular e escalável
- 🚫 Tratamento de erros com feedback visual direto no terminal

---

## 🏗️ Estrutura do Projeto

```
insta_terminal/
├── simple_package/
│   ├── __init__.py
│   └── insta_terminal.py  # 🚀 Código principal
├── tests/
│   └── test_insta_terminal.py  # ✅ Testes unitários
├── banner.png  # 🎨 Banner do projeto
├── requirements.txt  # 📦 Dependências
├── pyproject.toml  # 🔧 Configuração do projeto
├── README.md  # 📖 Documentação
```

---

## 🚀 Tecnologias

- 🐍 Python 3.10+
- 📦 Instaloader
- 🎨 Colorama
- 🔧 Pytest
- ⚙️ Padrões PEP8 + pyproject.toml

---

## 🧠 Como Executar

### ✅ Pré-requisitos:
- Python 3.10+
- Pip atualizado

### 🔥 Instale as dependências:
```bash
pip install -r requirements.txt
```

Ou manualmente:
```bash
pip install instaloader colorama
```

### ▶️ Execute o projeto:
```bash
python simple_package/insta_terminal.py
```

### ✨ Exemplo rodando no terminal:
```
🚀 INICIANDO O TERMINAL BLACK MIRROR 🚀

Digite o @(sem o @): eusoumanoelnetto
🔍 Hackeando os dados de @eusoumanoelnetto...

===== 🔍 Dados do Perfil =====
👤 Nome: Manoel Coelho
📝 Bio: Desenvolvedor Python | IA | Geek
📸 Posts: 45
🧠 Seguidores: 1200
🔗 Seguindo: 800
🔒 Privado: Não
✅ Verificado: Não
==============================

✔️ Download concluído com sucesso! 🗂️
```

---

## 🧪 Testes
Execute os testes com:
```bash
pytest
```

---

## 🚧 Limitações

- 🔒 Perfis privados não permitem download de dados ou fotos sem login.
- 🚫 Login não está implementado (intencionalmente para respeitar termos de uso).

---

## 🌟 Melhorias Futuras

- 💻 Interface gráfica (GUI) com Tkinter ou PyQt
- 📊 Exportação de dados para PDF ou CSV
- 🔑 Suporte a login (opcional, se permitido)
- 🔉 Sons, animações e mais interatividade no terminal
- 🌐 Integração com API oficial da Meta (se viável)

---

## 🏆 Autor

Desenvolvido por **Manoel Coelho** 🧠🚀  
[![GitHub](https://img.shields.io/badge/GitHub-eusoumanoelnetto-000?style=for-the-badge&logo=github)](https://github.com/eusoumanoelnetto)  
📫 Contato: [seuemail@exemplo.com](mailto:seuemail@exemplo.com)

---

## 📜 Licença

Licenciado sob a Licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">
  🚀 Feito com 🧠 e café ☕
</p>
