from calendar import Calendar

from icalendar import  *
import json

calendar_file = open('week-20-2023 (1).ics', 'rb')
cal = Calendar.from_ical(calendar_file.read())
dictionary = {}

def description_separation (summary : str):
    list_of_teachers = list()
    lecture_type = ""
    groups_present = list()
    lecture_type = summary.split(',')[0]
    summary = summary.replace(lecture_type, '')
    for element in summary.split(','):
        if ('-' in element and element.replace('-', '').isupper()):
            groups_present.append(element.strip())
            summary = summary.replace(element, '')

    list_of_teachers_unparsed = summary.split(',')
    list_of_teachers_unparsed = [x for x in list_of_teachers_unparsed if x != '']
    for i in range(0, len(list_of_teachers_unparsed)):
        if (i % 2 == 0):
            # list_of_teachers.append(f"{list_of_teachers_unparsed[i]} {list_of_teachers_unparsed[i+1]}".strip())
            continue

    return {"lecture type" : lecture_type, "groups_present" : groups_present, "list of teachers" : list_of_teachers}
    TeacherData[f'{id}'] = {"list of teachers": list_of_teachers}
    RoomNumberData[f'{id}'] = {'location': component.get('location')}
    LectureTypeData[f'{id}'] = {"lecture type" : lecture_type}
    LectureNameData[f'{id}'] = {'name' : component.get('name')}
    DateData[f'{id}'] = {'date' : date}
    TimeData[f'{id}'] = {'start' : start_time}

    json_Teacherdata = json.dumps(TeacherData)
    json_LectureTypedata = json.dumps(LectureTypeData)
    json_LectureNamedata = json.dumps(LectureNameData)
    json_Datedata = json.dumps(DateDate)
    json_Timedata = json.dumps(TimeData)
    json_RoomNumberdata = json.dumps(RoomNumberData)
    allDataHappyFace = (json_Timedata,json_Datedata,json_Teacherdata,json_RoomNumberdata,json_LectureNamedata,json_LectureTypedata)
    print(allDataHappyFace)

id = 0

for component in cal.walk() :
    if (component.name == 'VEVENT'):
        start_time = str(component.decoded('dtstart')).split('+')[0]
        date = start_time.split()[0]
        start_time = start_time.split()[1]
        end_time = str(component.decoded('dtend')).split('+')[0]
        end_time = end_time.split()[1]
        description = description_separation(component.get('summary'))
        dictionary[f'{id}'] = {'name' : component.get('name'),'description' : description, 'location' : component.get('location'),'date' : date,'start' : start_time, 'end' : end_time}
        id += 1

json_data = json.dumps(dictionary)



# print(json_data)
#description_separation('Doornbos, Jan (IC), IC-INF-IT1A, IC-INF-IT1B, IC-INF-IT1C, IC-INF-IT1D, IC-INF-IT1E, IC-INF-IT1F, IC-INF-IT1G, Oenen van, Gerjan (IC), Siersema, Elise (IC)')