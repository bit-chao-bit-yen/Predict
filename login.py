"""รันครั้งแรกครั้งเดียว: เปิด browser ให้ล็อกอิน Google เอง session เก็บใน browser.profile_dir"""
import os  # ใช้เปลี่ยนโฟลเดอร์ทำงาน
from pathlib import Path  # จัดการ path ไฟล์

os.chdir(Path(__file__).resolve().parent)  # ให้ path ใน config อ้างจากโฟลเดอร์โปรเจกต์

from teenoi_data.browser import login  # noqa: E402  ฟังก์ชันเปิด browser รอผู้ใช้ล็อกอิน
from teenoi_data.config import load_config  # noqa: E402  โหลด config + ตรวจ key ที่จำเป็น 

if __name__ == "__main__":  # รันตรงด้วย python login.py
    login(load_config("configs/Predict_config.yml", ["browser.profile_dir"]))  # ต้องมี profile_dir ไว้เก็บ session
