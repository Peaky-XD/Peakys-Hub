import os 
import sys

def find(key, flpth):
    print("> ENTER TXT FOLDER PATH")
    fld = input("> ENTER PATH : ")
    print("------------------------")
    files = os.listdir(fld)
    for file in files:
        for uxd in open(os.path.join(fld, file), 'r').read().splitlines():
            if key in uxd:
                print(f"> DATA : {uxd}")
                print("------------------------")
                with open(f"{flpth}.txt", "a") as outfile:
                    outfile.write(uxd + "\n")
    try:
        ttl = len(open(f"{flpth}.txt", "r").read().splitlines())
        print(f"> TOTAL DATA EXTRACTED: {ttl}")
        print("-------------------------")
    except:
        print("> NOT FOUND OR SOMETHING WRONG")
        sys.exit()

def main():
    os.system("clear")
    print("-------------------------")
    print("[A]> CPANEL EXTRACTOR")
    print("[B]> FACEBOOK IDS EXTRACTOR")
    print("[C]> TARGET KEYWORD EXTRACTOR")
    print("-------------------------")
    x1 = input("> ENTER OPTION : ")
    print("-------------------------")
    if x1.lower() == "a":
        find(":2038", "cpanel")
    elif x1.lower() == "b":
        find("facebook", "facebook")
    elif x1.lower() == "c":
        x2 = input("> ENTER KEYWORD : ")
        find(x2, x2)
    else:
        main()

main()
