import pandas as pd
import pywhatkit
import time
import logging
import os
from datetime import datetime
import pyautogui

# Ensure logs directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Setup logging
logging.basicConfig(
    filename='logs/whatsapp_log_3rd.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

TEMPLATE = """Hey {name}!

I’m reaching out on behalf of Chitti, GITAM’s fastest-growing exam prep startup 🚀

In our last two launches, 8,000+ students used Chitti for their exam prep. In our most recent monetized launch, we even generated over ₹40,000 in revenue, proving the demand for high-quality content from toppers.
Now, we’re scaling this up for the upcoming August 28th Mid Exams, and we’re onboarding a few standout 3rd semester students as Subject Experts.
Based on your 1st year performance, we believe you'd be a perfect fit. This is a paid opportunity + a chance to be a core part of something big at GITAM! 🌟
Let me know if you’re interested — would love to share more details!

– Team Chitti
"""

def send_whatsapp_message(name, number, message, wait_time=15):
    try:
        pywhatkit.sendwhatmsg_instantly(f"+91{number}", message, wait_time=wait_time, tab_close=True)
        time.sleep(2)  # Wait for message to be typed
        pyautogui.press('enter')
        logging.info(f"3rd sem | {name} | {number} | Message sent")
        return True
    except Exception as e:
        logging.error(f"3rd sem | {name} | {number} | Failed to send message: {e}")
        return False

def process_csv(file_path):
    df = pd.read_csv(file_path)
    for idx, row in df.iterrows():
        name = row[0]
        number = str(row[1]).strip()
        message = TEMPLATE.format(name=name)
        success = send_whatsapp_message(name, number, message)
        log_msg = f"3rd sem | {name} | {number} | {'Success' if success else 'Failed'}"
        print(log_msg)
        time.sleep(5)  # To avoid being flagged as spam

if __name__ == "__main__":
    print("Starting WhatsApp automation for 3rd semester...")
    process_csv("details/students_3rd_sem.csv")
    print("Done. Check logs/whatsapp_log_3rd.txt for details.") 