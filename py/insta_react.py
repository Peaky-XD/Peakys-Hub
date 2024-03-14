import requests
import random
from getuseragent import UserAgent
from rich import print
from rich.panel import Panel


class InstagramBooster:
    def __init__(self):
        self.ua = UserAgent("ios").Random()

    def boost_post(self, user: str, link: str) -> dict:
        email = f"x_spoilt{random.randint(100000, 999999)}@gmail.com"
        headers = {
            "Host": "api.likesjet.com",
            "content-length": "137",
            "sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "user-agent": self.ua,
            "sec-ch-ua-platform": "\"Android\"",
            "origin": "https://likesjet.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://likesjet.com/",
            "accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5"
        }
        data = {"instagram_username": user, "link": link, "email": email}
        response = requests.post('https://api.likesjet.com/freeboost/7', json=data, headers=headers).json()
        return response


def main():
    logo = """
    [bold cyan]Coded by :[/] [bold yellow]@x_spoilt[/]
    [bold cyan]Team :[/] [bold yellow]@peaky_xd[/]
    """
    print(Panel(logo, title="[bold green]Instagram Booster[/]"))
    booster = InstagramBooster()
    user = input('> InstaGram Username : ')
    link = input('> Post Link : ')
    response = booster.boost_post(user, link)
    result_message = f"Status: {'[bold green]Success[/]' if response.get('status') else '[bold red]Failed[/]'}\nMessage: {response.get('message')}"
    print(Panel(result_message, title="[bold blue]Boost Result[/]"))

if __name__ == "__main__":
    main()
