import sys, random, os

def getinfo(id):
    print(f"Connecting User ID: {id}")
    print(f"Searching Database...\n")
    
    ipbas = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    ip = ipbas + "." + str(random.randint(0, 255))
    guiadd = ipbas + ".0/" + str(random.randint(10, 90))
    port = str(random.randint(1, 65535))
    mac = random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) + \
          random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) + \
          ":" + random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) + \
          random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) + \
          ":" + random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) + \
          random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) + \
          ":" + random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) + \
          random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) + \
          ":" + random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) + \
          random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) + \
          ":" + random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]) + random.choice(["A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    
    userver = str(random.randint(100, 500))
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4714.71 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4748.71 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4779.71 Safari/537.3"
    ]
    ua= random.choice(user_agents)
    mesvar = random.randint(1000, 100000)
    print(f"8 Log Found\n")
    print(f"IP Address: {ip}\nNet Gui Address: {guiadd}\nPort: {port}\nConnection: {ip}:{port}\nMac Address: {mac}\nUser Version: {userver}\nUser Agent: {ua}\nMessage Count: {mesvar}\n")
    json = {"userid": id, "ipaddress": ip, "port": port, "connect": ip+":"+port, "mac": mac, "user-agent": ua, "mescount": mesvar, "version": userver}
    print(f"Json Data: {json}")

def start(id):
    if len(id) == 19:
        getinfo(id)
    else:
        print("Error ID Invalid")

def menu():
    os.system("clear")
    print(f"""\033[92m   ___  _____    ____     __      
  / _ \/ ___/___/ __/__ _/ /_____ 
 / // / /__/___/ _// _ `/  '_/ -_)
/____/\___/   /_/  \_,_/_/\_\\__/ 
     \033[93mFake Discord Hack Tool\n""")
    print("[ 1 ] \033[92mStart Hack\033[93m [ 2 ] \033[92mExit Tool")
    selec = input("\nSelect Option: ")
    if selec == "1":
        id = input("\nDiscord User ID: ")
        start(id)
        enter = input("\n[ Enter to menu ]")
        menu()
    elif selec == "2":
        sys.exit()
    else:
        menu()

menu()
