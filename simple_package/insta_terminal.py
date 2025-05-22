import instaloader
import sys
import time
import os
from colorama import Fore, init
import msvcrt  # Funciona no Windows

init(autoreset=True)

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + """
 ██████╗ ██████╗ ███████╗██╗     ██╗  ██╗ ██████╗ 
██╔════╝██╔═══██╗██╔════╝██║     ██║  ██║██╔═══██╗
██║     ██║   ██║█████╗  ██║     ███████║██║   ██║
██║     ██║   ██║██╔══╝  ██║     ██╔══██║██║   ██║
╚██████╗╚██████╔╝███████╗███████╗██║  ██║╚██████╔╝
 ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
🚀 TERMINAL DE BUSCA BLACK MIRROR V2 - MODE HACKER 🚀
    """)


def hacker_effect(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def buscar_dados(username):
    loader = instaloader.Instaloader()

    try:
        hacker_effect(f"\n{Fore.CYAN}🔍 Hackeando os dados de @{username}...")
        profile = instaloader.Profile.from_username(loader.context, username)

        print("\n===== 🔍 Dados do Perfil =====")
        print(f"👤 Nome: {profile.full_name}")
        print(f"📝 Bio: {profile.biography}")
        print(f"📸 Posts: {profile.mediacount}")
        print(f"🧠 Seguidores: {profile.followers}")
        print(f"🔗 Seguindo: {profile.followees}")
        print(f"🔒 Privado: {'Sim' if profile.is_private else 'Não'}")
        print(f"✅ Verificado: {'Sim' if profile.is_verified else 'Não'}")
        print("==============================\n")

        if profile.is_private:
            hacker_effect(f"{Fore.RED}🚫 ACESSO NEGADO! Este perfil é PRIVADO.\n⚠️ Dados limitados sem acesso autorizado.\n")
        else:
            hacker_effect(f"{Fore.GREEN}✔️ Perfil público detectado!\n")
            hacker_effect(f"{Fore.GREEN}✅ Dados coletados com sucesso! 🗂️\n")

    except Exception as e:
        hacker_effect(f"{Fore.RED}❌ Erro: {e}")

def main():
    banner()  # Agora exibe o banner na inicialização
    print(Fore.GREEN + "\n🚀 INICIANDO O TERMINAL BLACK MIRROR 🚀\n")
    user = input(Fore.YELLOW + "Digite o @ (sem o @): ").strip()
    buscar_dados(user)

if __name__ == "__main__":
    main()
