import requests
from ics import Calendar
import datetime
import re

# Fetch the calendar feed data
url = 'https://nhlstenden.myx.nl/api/InternetCalendar/feed/f6afeda5-97f4-4633-b240-7f897fc95ce9/cecd7dc1-0f74-4867-a6f6-02df81d2d47a'
response = requests.get(url)

if response.status_code == 200:
    # Parse the calendar feed
    c = Calendar(response.text)

    # Get the current week of the year
    current_week = datetime.datetime.now().isocalendar()[1]

    # Filter events for the current week
    filtered_events = [event for event in c.events if event.begin.isocalendar()[1] == current_week]

    if filtered_events:
        # Create a dictionary to store events for each room
        room_schedules = {}

        for event in filtered_events:
            # Check if the event has a location
            if event.location is None:
                continue

            # Extract the room numbers from the event location
            room_numbers = event.location.split(',')

            for room_number in room_numbers:
                room_number = room_number.strip()

                # Check if the room number already exists in the dictionary
                if room_number in room_schedules:
                    # Add the event to the existing room schedule
                    room_schedules[room_number].events.add(event)
                else:
                    # Create a new calendar for the room and add the event
                    room_calendar = Calendar()
                    room_calendar.events.add(event)

                    # Add the room calendar to the dictionary
                    room_schedules[room_number] = room_calendar

        # Save each room's schedule to a separate file
        for room_number, room_calendar in room_schedules.items():
            # Simplify the file name to include only the 4-digit room number
            simplified_room_number = re.sub(r'\D', '', room_number)

            filename = f'week-{current_week}-{simplified_room_number.zfill(4)}.ics'
            with open(filename, 'w', encoding='utf-8') as file:
                file.writelines(room_calendar)

            print(f'Calendar for room {room_number} in week {current_week} saved as "{filename}".')

    else:
        print('No events found for the current week.')
else:
    print('Failed to fetch the calendar feed.')
