import webbrowser
import time

total_breaks = 3
break_count = 0
url = "https://calendar.google.com/calendar/render?cid=aWtmdXEyNzhsN245ZHZmODB2bms1bm8ydDRAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ#main_7%7Cmonth"
chrome_path = "open -a /Applications/Google\ Chrome.app %s"

print ("This 'Take a Break' program started on" +time.ctime())
while break_count < total_breaks:
    time.sleep(25*60) # delay for 25 min
    webbrowser.get(chrome_path).open(url)
    break_count += 1
