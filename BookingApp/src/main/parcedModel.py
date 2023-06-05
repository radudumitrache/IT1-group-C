import json
from .models import StudentLectureTeacher, Lecture


def insert_json_data_Teacherdata():
    parsed_data = json.load()

    for item in parsed_data:
         studentModel = StudentLectureTeacher(json_data=item)
         studentModel.save()


def insert_json_data_RoomNumberdata():
    parsed_data = json.load()

    for item in parsed_data:
         studentModel = StudentLectureTeacher(json_data=item)
         studentModel.save()


def insert_json_data_LectureNamedata():
    parsed_data = json.load()

    for item in parsed_data:
         lectureModel = Lecture(json_data=item)
         lectureModel.save()


def insert_json_data_Datedata():
    parsed_data = json.load()

    for item in parsed_data:
         lectureModel = Lecture(json_data=item)
         lectureModel.save()


def insert_json_data_Timedata():
    parsed_data = json.load()

    for item in parsed_data:
         lectureModel = Lecture(json_data=item)
         lectureModel.save()


def insert_json_data_LectureTypedata():
    parsed_data = json.load()

    for item in parsed_data:
         lectureModel = Lecture(json_data=item)
         lectureModel.save()