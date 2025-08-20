# VirusTotal Discord Bot

A Discord bot that checks URLs and file hashes using the VirusTotal API. This bot helps filter potentially harmful links and files in your server.

![img](https://media.discordapp.net/attachments/1260613480545915001/1373549373748809739/image.png?ex=682ad10a&is=68297f8a&hm=c40a803aec90149f2d4462a31a2e6b58701240750d4de0b5e314bb2e79629ef5&=&format=webp&quality=lossless)

## Features
- Scan URLs to detect potential threats.
- Check file hashes against VirusTotal's database.
- Simple usage with the `!scan` command.

## Installation

### 1. Install Python and Dependencies
```bash
# Clone the repository and navigate to the project directory
git clone https://github.com/Premnoi/VirusTotal-Discord.git  
cd VirusTotal-Discord

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file and add the required API keys:
```plaintext
TOTALVIRUS_API_KEY=your_virustotal_api_key
DISCORD_TOKEN=your_discord_bot_token
```

### 3. Run the Bot
```bash
python bot.py
```

## Usage
Use the `!scan` command to check a URL or file hash:
```plaintext
!scan <URL or file hash>
```

### Example
```plaintext
!scan https://example.com
!scan d41d8cd98f00b204e9800998ecf8427e
```

## Notes
- A **Discord Bot Token** and **VirusTotal API Key** are required.
- Get an API Key from [VirusTotal](https://www.virustotal.com/gui/join-us).

 ---
<br />
<br />

#  VirusTotal Discord Bot

บอท Discord ที่ช่วยตรวจสอบ URL และไฟล์ผ่าน VirusTotal API
เหมาะสำหรับใช้กรองลิงก์และไฟล์ที่อาจเป็นอันตรายในเซิร์ฟเวอร์

##  ฟีเจอร์
- ตรวจสอบ URL ว่ามีความเสี่ยงหรือไม่
- ตรวจสอบค่า Hash ของไฟล์ที่เคยถูกสแกนบน VirusTotal
- ใช้งานง่ายแค่พิมคำสั่ง `!scan`

##  วิธีติดตั้ง

### 1️⃣ ติดตั้ง Python และไลบรารีที่จำเป็น
```bash
# โคลนโปรเจกต์และเข้าไปในโฟลเดอร์
git clone https://github.com/Premnoi/VirusTotal-Discord.git  
cd VirusTotal-Discord

# ติดตั้ง dependencies
pip install -r requirements.txt
```

### 2️⃣ ตั้งค่าไฟล์ `.env`
สร้างไฟล์ `.env` และเขียน API Key และ Token ของบอท  
```plaintext
TOTALVIRUS_API_KEY= (virustotal api key)
DISCORD_TOKEN= (discord bot token)
```

### 3️⃣ รันบอท
```bash
python bot.py
```

##  วิธีใช้งาน
ใช้คำสั่ง `!scan` เพื่อตรวจสอบ  
```plaintext
!scan <URL หรือ file hash>
```

 ตัวอย่างการใช้งาน:  
```plaintext
!scan https://example.com  
!scan d41d8cd98f00b204e9800998ecf8427e
```

##  หมายเหตุ
- ต้องมี **Discord Bot Token** และ **VirusTotal API Key** เพื่อให้บอททำงานได้  
- ขอ API Key ได้จาก [VirusTotal](https://www.virustotal.com/gui/join-us)


