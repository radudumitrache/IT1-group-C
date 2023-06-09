from icalendar import *
import json
from pprint import pprint

calendar_file = open('week-24-2023.ics', 'rb')
calendar = Calendar.from_ical(calendar_file.read())
dictionary = {}


def description_separation(summary: str):
    list_of_teachers = list()
    groups_present = list()
    lecture_type = summary.split(',')[0]

    summary = summary.replace(lecture_type, '')
    for element in summary.split(','):
        if '-' in element and element.replace('-', '').isupper():
            groups_present.append(element.strip())
            summary = summary.replace(element, '')
        elif "INF" in element:
            groups_present.append(element.strip())
            summary = summary.replace(element, '')

    list_of_teachers_unparsed = summary.split(',')
    list_of_teachers_unparsed = [x for x in list_of_teachers_unparsed if x != '']
    for i in range(0, len(list_of_teachers_unparsed)):
        if i % 2 == 0:
            list_of_teachers.append(f"{list_of_teachers_unparsed[i]} {list_of_teachers_unparsed[i + 1]}".strip())
            continue

    return {"lecture type": lecture_type, "groups_present": groups_present, "list of teachers": list_of_teachers}


def calendar_parse(calendar):
    id = 0
    for component in calendar.walk():
        if component.name == 'VEVENT':
            start_time = str(component.decoded('dtstart')).split('+')[0]
            date = start_time.split()[0]
            start_time = start_time.split()[1]
            end_time = str(component.decoded('dtend')).split('+')[0]
            end_time = end_time.split()[1]
            description = description_separation(component.get('summary'))
            dictionary[f'{id}'] = {'name': component.get('name'), 'description': description,
                                   'location': component.get('location'), 'date': date, 'start': start_time,
                                   'end': end_time}
            id += 1

    return dictionary


calendar_parse(calendar)
json_data = json.dumps(dictionary)
f = open("jsonText.txt", "w")
f.write(json_data)
f.close()
