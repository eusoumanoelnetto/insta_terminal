import requests
import argparse
from rich import print
from rich.panel import Panel

def get_instagram_data(username):
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
headers = {
    "User-Agent": "Instagram 155.0.0.37.107",
}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    data = response.json()
    user = data.get("graphql", {}).get("user", {})
    return {
        "Nome": user.get("full_name"),
        "Bio": user.get("biography"),
        "Seguidores": user.get("edge_followed_by", {}).get("count"),
        "Seguindo": user.get("edge_follow", {}).get("count"),
        "Posts": user.get("edge_owner_to_timeline_media", {}).get("count")
    }

def run():
    parser = argparse.ArgumentParser(description="Consulta de perfil público do Instagram.")
    parser.add_argument('--user', help='Nome do usuário do Instagram', required=True)
    args = parser.parse_args()

    profile = get_instagram_data(args.user)
    if profile:
        print(Panel.fit(f"[bold cyan]{args.user}[/bold cyan]\n\n" + "\n".join([f"[bold]{k}:[/bold] {v}" for k,v in profile.items()])))
    else:
        print("[bold red]Usuário não encontrado ou bloqueado![/bold red]")
