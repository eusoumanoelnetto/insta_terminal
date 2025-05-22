import instaloader
import sys
import time
import os
import json
from colorama import Fore, init
import getpass
import msvcrt  # Apenas para Windows

init(autoreset=True)

# ===================== BANNER COM EFEITO =====================
def banner_effect():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_text = """
 ██████╗ ██████╗ ███████╗██╗     ██╗  ██╗ ██████╗ 
██╔════╝██╔═══██╗██╔════╝██║     ██║  ██║██╔═══██╗
██║     ██║   ██║█████╗  ██║     ███████║██║   ██║
██║     ██║   ██║██╔══╝  ██║     ██╔══██║██║   ██║
╚██████╗╚██████╔╝███████╗███████╗██║  ██║╚██████╔╝
 ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
🚀 TERMINAL DE BUSCA BLACK MIRROR V3 - MODE HACKER 🚀
"""
    for char in banner_text:
        print(Fore.GREEN + char, end="", flush=True)
        time.sleep(0.0015)
    print()

# ===================== TEXTO ESTILO HACKER =====================
def hacker_effect(text, delay=0.02):
    for char in text:
        print(Fore.LIGHTGREEN_EX + char, end="", flush=True)
        time.sleep(delay)
    print()

# ===================== INPUT COM ASTERISCOS =====================
def input_password(prompt="🔑 Senha: "):
    print(Fore.CYAN + prompt, end="", flush=True)
    password = ""
    while True:
        ch = msvcrt.getch()
        if ch in {b'\r', b'\n'}:
            print('')
            break
        elif ch == b'\x08':  # Backspace
            if len(password) > 0:
                password = password[:-1]
                print('\b \b', end="", flush=True)
        elif ch == b'\x03':  # Ctrl+C
            raise KeyboardInterrupt
        else:
            try:
                char = ch.decode('utf-8')
                if char.isprintable():
                    password += char
                    print('*', end="", flush=True)
            except UnicodeDecodeError:
                pass
    return password

# ===================== LOGIN =====================
def login_instagram(loader):
    hacker_effect("\n🔐 FAÇA LOGIN NO INSTAGRAM PARA ACESSO TOTAL\n")
    username = input(Fore.CYAN + "👤 Usuário: ").strip()
    password = input_password()

    try:
        loader.login(username, password)
        hacker_effect(f"✅ Login bem-sucedido como @{username}\n")
    except Exception as e:
        hacker_effect(f"{Fore.RED}❌ Erro no login: {e}")
        sys.exit()

# ===================== BUSCA E LOG =====================
def buscar_dados(username, loader):
    try:
        hacker_effect(f"\n🔍 Hackeando os dados de @{username}...\n")
        profile = instaloader.Profile.from_username(loader.context, username)

        dados = {
            "👤 Nome": profile.full_name,
            "🔗 Usuário": username,
            "📝 Bio": profile.biography,
            "🧠 Seguidores": profile.followers,
            "➡️ Seguindo": profile.followees,
            "📸 Posts": profile.mediacount,
            "🔒 Privado": "Sim" if profile.is_private else "Não",
            "✅ Verificado": "Sim" if profile.is_verified else "Não",
            "🖼️ Foto de Perfil": profile.profile_pic_url
        }

        print(Fore.LIGHTBLACK_EX + "\n===== 🔍 Dados do Perfil =====")
        for chave, valor in dados.items():
            print(Fore.LIGHTWHITE_EX + f"{chave}: {valor}")
        print(Fore.LIGHTBLACK_EX + "===============================\n")

        if profile.is_private:
            hacker_effect(f"{Fore.RED}🚫 Este perfil é PRIVADO. Dados limitados.\n")
        else:
            hacker_effect(f"{Fore.GREEN}✔️ Perfil público detectado!\n")

        # 🔥 Salvar log e foto
        salvar_log(dados)
        baixar_foto_perfil(profile, username)

    except Exception as e:
        hacker_effect(f"{Fore.RED}❌ Erro: {e}")

# ===================== SALVAR LOG EM JSON =====================
def salvar_log(dados):
    pasta_logs = "logs"
    if not os.path.exists(pasta_logs):
        os.makedirs(pasta_logs)

    filename = f"{pasta_logs}/{dados['🔗 Usuário']}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

    hacker_effect(f"💾 Log salvo em {filename}\n")

# ===================== BAIXAR FOTO DE PERFIL =====================
def baixar_foto_perfil(profile, username):
    pasta_fotos = "fotos_perfil"
    if not os.path.exists(pasta_fotos):
        os.makedirs(pasta_fotos)

    filepath = os.path.join(pasta_fotos, f"{username}_profile_pic.jpg")
    loader = instaloader.Instaloader(download_pictures=False, download_videos=False,
                                     download_video_thumbnails=False, download_geotags=False,
                                     download_comments=False, save_metadata=False, compress_json=False)

    loader.download_profilepic(profile)

    hacker_effect(f"🖼️ Foto de perfil salva em {filepath}\n")

# ===================== MAIN =====================
def main():
    banner_effect()
    print(Fore.GREEN + "\n🚀 INICIANDO O TERMINAL BLACK MIRROR 🚀\n")

    loader = instaloader.Instaloader()

    # 🔐 Login real
    login_instagram(loader)

    while True:
        user = input(Fore.YELLOW + "\nDigite o @ (sem o @) ou 'sair': ").strip()

        if user.lower() == "sair":
            hacker_effect("🛑 Encerrando... Até mais, Sr. Stark.\n")
            break

        if user == "":
            hacker_effect("⚠️ Usuário inválido. Tente novamente.\n")
            continue

        buscar_dados(user, loader)

# ===================== EXECUÇÃO =====================
if __name__ == "__main__":
    main()
