# 🦠 VirusTotal Discord Bot

บอท Discord ที่ช่วยตรวจสอบ URL และไฟล์ผ่าน VirusTotal API  
เหมาะสำหรับใช้กรองลิงก์และไฟล์ที่อาจเป็นอันตรายในเซิร์ฟเวอร์ของคุณ  

## 🚀 ฟีเจอร์
- ตรวจสอบ URL ว่ามีความเสี่ยงหรือไม่  
- ตรวจสอบค่า Hash ของไฟล์ที่เคยถูกสแกนบน VirusTotal  
- ใช้งานง่ายผ่านคำสั่ง `!scan`  

## 🛠 วิธีติดตั้ง

### 1️⃣ ติดตั้ง Python และไลบรารีที่จำเป็น
```bash
# โคลนโปรเจกต์และเข้าไปในโฟลเดอร์
git clone https://github.com/USERNAME/REPOSITORY.git  
cd REPOSITORY  

# ติดตั้ง dependencies
pip install -r requirements.txt
```

### 2️⃣ ตั้งค่าไฟล์ `.env`
สร้างไฟล์ `.env` และกำหนดค่า API Key และ Token ของบอท  
```plaintext
TOTALVIRUS_API_KEY=your_virustotal_api_key
DISCORD_TOKEN=your_discord_bot_token
```

### 3️⃣ รันบอท
```bash
python bot.py
```

## ⚡ วิธีใช้งาน
ใช้คำสั่ง `!scan` เพื่อตรวจสอบ  
```plaintext
!scan <URL หรือ file hash>
```

🔹 ตัวอย่างการใช้งาน:  
```plaintext
!scan https://example.com  
!scan d41d8cd98f00b204e9800998ecf8427e
```

## 📝 หมายเหตุ
- ต้องมี **Discord Bot Token** และ **VirusTotal API Key** เพื่อให้บอททำงานได้  
- สามารถขอ API Key ได้ที่ [VirusTotal](https://www.virustotal.com/gui/join-us)

## 📜 License
This project is licensed under the MIT License.

