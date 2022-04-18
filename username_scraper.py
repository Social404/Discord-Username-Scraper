import discum,sys,os
from colorama import Fore
from time import sleep

if os.name == 'nt':
	os.system("cls")
else:
	os.system("clear")
    
print(f'''{Fore.RED}
 ░█▀▄░▀█▀░█▀▀░█▀▀░█▀█░█▀▄░█▀▄
 ░█░█░░█░░▀▀█░█░░░█░█░█▀▄░█░█
 ░▀▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀░
 ░█▀▀░█▀▀░█▀▄░█▀█░█▀█░█▀▀░█▀▄
 ░▀▀█░█░░░█▀▄░█▀█░█▀▀░█▀▀░█▀▄
 ░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░░░▀▀▀░▀░▀ {Fore.RESET} Username Edition''')

TOKEN = input(f"{Fore.RED} Token: {Fore.RESET}")
SERVER_ID = input(f"{Fore.RED} Server ID: {Fore.RESET}")
CHANNEL_ID = input(f"{Fore.RED} Channel ID: {Fore.RESET}")

if (TOKEN == "" or SERVER_ID == "" or CHANNEL_ID == ""):
    print(f"{Fore.RED} Your provided an invalid token, server or channel id!{Fore.RESET}")
    sys.exit()

discord = discum.Client(token=TOKEN)
discord.gateway.log = False

def close(resp, guild_id):
    if discord.gateway.finishedMemberFetching(guild_id):
        discord.gateway.removeCommand({'function': close, 'params': {'guild_id': guild_id}})
        discord.gateway.close()

def fetch(guild_id, channel_id):
    discord.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    discord.gateway.command({'function': close, 'params': {'guild_id': guild_id}})
    discord.gateway.run()
    discord.gateway.resetSession()
    return discord.gateway.session.guild(guild_id).members

members_list = fetch(SERVER_ID, CHANNEL_ID)
id_list = []

for IDS in members_list:
    id_list.append(members_list[IDS]['username'])

file = open("users.txt", "a")

for id in id_list:
    if id not in open("users.txt").read():
        file = open("users.txt", 'a')

        try:
            file.write(id + "\n")
        except:
            pass

        file.close()


sleep(1)

file2 = open("users.txt", "r")
total = len(file2.readlines())

sleep(1)
    
input(f"{Fore.LIGHTGREEN_EX}Total Scraped: {total} {Fore.RESET}")

# Not Made By Social404
