import csv
from datetime import datetime, timedelta
from icalendar import Calendar, Event
from pytz import timezone

tz = timezone('Europe/Bucharest')
cal = Calendar()

with open('forest_sessions.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        start_time = tz.localize(datetime.strptime(row[0], '%d-%m-%Y %H:%M'))
        duration = int(row[1])
        end_time = start_time + timedelta(minutes=duration)
        title = row[2] if len(row) > 2 else "Forest Session"

        event = Event()
        event.add('summary', title)
        event.add('dtstart', start_time)
        event.add('dtend', end_time)
        event.add('description', f'{title} via Forest Extension')
        cal.add_component(event)

with open('forest.ics', 'wb') as f:
    f.write(cal.to_ical())

print("✅ forest.ics elkészült.")
