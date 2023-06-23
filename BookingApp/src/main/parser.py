from icalendar import *
import json

def description_separation(summary: str):
    list_of_teachers = list()
    lecture_type = ""
    groups_present = list()
    lecture_type = summary.split(',')[0]

    summary = summary.replace(lecture_type, '')
    for element in summary.split(','):
        if '-' in element and element.replace('-', '').isupper():
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
    dictionary = {}
    id = 0
    cal = Calendar.from_ical(calendar.read())
    for component in cal.walk():
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

    TeacherData = {}
    RoomNumberData = {}
    LectureTypeData = {}
    LectureNameData = {}
    DateData = {}
    TimeData = {}

    for key, value in dictionary.items():
        TeacherData[key] = {"list of teachers": value['description']['list of teachers']}
        RoomNumberData[key] = {'location': value['location']}
        LectureTypeData[key] = {"lecture type": value['description']['lecture type']}
        LectureNameData[key] = {'name': value['name']}
        DateData[key] = {'date': value['date']}
        TimeData[key] = {'start': value['start']}

    json_Teacherdata = json.dumps(TeacherData)
    json_LectureTypedata = json.dumps(LectureTypeData)
    json_LectureNamedata = json.dumps(LectureNameData)

# description_separation(',Doornbos, Jan (IC), IC-INF-IT1A, IC-INF-IT1B, IC-INF-IT1C, IC-INF-IT1D, IC-INF-IT1E, IC-INF-IT1F, IC-INF-IT1G, Oenen van, Gerjan (IC), Siersema, Elise (IC)')