from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = "26067517"
API_HASH = "7673bb2ce1bc57a0fe667ea819d5c809"

BOT_TOKEN = "7832133867:AAHMWDyZ5BaRXicdqeVc0Z"
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = "6856510372"

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = "BQGNwj0Afa_UKpzIfcO7b9VoU2T-IFiS7xQGn4q2gREiYRyn5z5yw--rVMFzFya_GO1anUWYIHIoGF-odW7tYQUTxmHum2ZFdbj_mHVTJQ6ZW4QKeVabp7NFpvSug5rChULbaBYl6d3b9sb6uhadOLzus0_Ga31Q2fk7zR9ZfinOV-sGQ0MGWt-N-Uk4SGzRsgjXqxT106GD_KlIuA39-tX25B2Y5B5z6S8cbaqa0-n5V0N1SOyWe25rLSu2uCakFHe4SDRDX4_ZCC2x7cZ80X0L04CdXtWO6kJTDhBlV4iAWHeiAyxnf-lOclca1Czo7Mm31g2fuoF6JzzNAxUqPlzH7vIxbAAAAAF7fLFTAA"

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
