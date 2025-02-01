import discord
import requests
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

TOTALVIRUS_API_KEY = os.getenv('TOTALVIRUS_API_KEY')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def check_file_status(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": TOTALVIRUS_API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Status {response.status_code}: {response.text}"}

def check_url_status(target_url):
    url = "https://www.virustotal.com/api/v3/urls"
    headers = {"x-apikey": TOTALVIRUS_API_KEY}
    data = {"url": target_url}
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
       
        scan_id = response.json()["data"]["id"]
        
        result_url = f"https://www.virustotal.com/api/v3/analyses/{scan_id}"
        result_response = requests.get(result_url, headers=headers)
        
        if result_response.status_code == 200:
            return result_response.json()
        else:
            return {"error": f"Status {result_response.status_code}: {result_response.text}"}
    else:
        return {"error": f"Status {response.status_code}: {response.text}"}

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!scan"):
        args = message.content.split()
        if len(args) < 2:
            await message.channel.send("⚠️ โปรดระบุ file hash หรือ URL ที่ต้องการตรวจสอบ")
            return
        
        target = args[1]
        await message.channel.send(f"🔍 กำลังตรวจสอบ `{target}` ...")
        
        if target.startswith("http://") or target.startswith("https://"):
            result = await asyncio.to_thread(check_url_status, target)
            if "error" not in result:
                attributes = result["data"]["attributes"]
                status = attributes.get("status", "unknown")
                stats = attributes.get("stats", {})
                
                if status == "queued":
                    response_message = (
                        f"ผลการตรวจสอบ URL: **{target}**\n"
                        f"สถานะ: **รอการประมวลผล (queued)**\n"
                        f"โปรดรอสักครู่แล้วตรวจสอบอีกครั้ง"
                    )
                else:
                    response_message = (
                        f"ผลการตรวจสอบ URL: **{target}**\n"
                        f"สถานะ: **{status}**\n"
                        f"รายละเอียด:\n"
                        f"  - Malicious: {stats.get('malicious', 0)}\n"
                        f"  - Suspicious: {stats.get('suspicious', 0)}\n"
                        f"  - Undetected: {stats.get('undetected', 0)}\n"
                        f"  - Harmless: {stats.get('harmless', 0)}\n"
                        f"  - Timeout: {stats.get('timeout', 0)}"
                    )
                await message.channel.send(response_message)
            else:
                await message.channel.send(f"❌ เกิดข้อผิดพลาด: {result['error']}")
        else:
            result = await asyncio.to_thread(check_file_status, target)
            if "error" not in result:
                attributes = result["data"]["attributes"]
                status = attributes.get("status", "unknown")
                stats = attributes.get("stats", {})
                
                if status == "queued":
                    response_message = (
                        f"ผลการตรวจสอบไฟล์ (hash): **{target}**\n"
                        f"สถานะ: **รอการประมวลผล (queued)**\n"
                        f"โปรดรอสักครู่แล้วตรวจสอบอีกครั้ง"
                    )
                else:
                    response_message = (
                        f"ผลการตรวจสอบไฟล์ (hash): **{target}**\n"
                        f"สถานะ: **{status}**\n"
                        f"รายละเอียด:\n"
                        f"  - Malicious: {stats.get('malicious', 0)}\n"
                        f"  - Suspicious: {stats.get('suspicious', 0)}\n"
                        f"  - Undetected: {stats.get('undetected', 0)}\n"
                        f"  - Harmless: {stats.get('harmless', 0)}\n"
                        f"  - Timeout: {stats.get('timeout', 0)}"
                    )
                await message.channel.send(response_message)
            else:
                await message.channel.send(f"❌ เกิดข้อผิดพลาด: {result['error']}")

client.run(DISCORD_TOKEN)
