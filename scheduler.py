import schedule
import time
from main import main

# Agendar postagens 3 vezes ao dia
schedule.every().day.at("08:00").do(main)
schedule.every().day.at("14:00").do(main)
schedule.every().day.at("20:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
