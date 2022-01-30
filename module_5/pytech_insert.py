from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.pgrq0.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# students
thorin = {
    "student_id" : "1007",
    "first_name" : "Thorin",
    "last_name" : "Oakenshield",
    "enrollments" : [
        {
            "term" : "Session 2",
            "gpa" : "4.0",
            "start_date" : "July 10, 2020",
            "end_date" : "September 14, 2020",
            "courses" : [
                {
                    "course_id" : "CSD310",
                    "description" : "Database Development and Use",
                    "instructor" : "Professor Krasso",
                    "grade" : "A+"
                },
                {
                    "course_id" : "CSD320",
                    "description" : "Programming with Java",
                    "instructor" : "Professor Krasso",
                    "grade" : "A+"
                }
            ]
        }
    ]
}

bilbo = {
    "student_id" : "1008",
    "first_name" : "Bilbo",
    "last_name" : "Baggins",
    "enrollments" : [
        {
            "term" : "Session 2",
            "gpa" : "3.52",
            "start_date" : "July 10, 2020",
            "end_date" : "September 14, 2020",
            "courses" : [
                {
                    "course_id" : "CSD310",
                    "description" : "Database Development and Use",
                    "instructor" : "Professor Krasso",
                    "grade" : "B+"
                },
                {
                    "course_id" : "CSD320",
                    "description" : "Programming with Java",
                    "instructor" : "Professor Krasso",
                    "grade" : "A-"
                }
            ]
        }
    ]
}

frodo = {
    "student_id" : "1009",
    "first_name" : "Frodo",
    "last_name" : "Baggins",
    "enrollments" : [
        {
            "term" : "Session 2",
            "gpa" : "1.5",
            "start_date" : "July 10, 2020",
            "end_date" : "September 14, 2020",
            "courses" : [
                {
                    "course_id" : "CSD310",
                    "description" : "Database Development and Use",
                    "instructor" : "Professor Krasso",
                    "grade" : "C"
                },
                {
                    "course_id" : "CSD320",
                    "description" : "Programming with Java",
                    "instructor" : "Professor Krasso",
                    "grade" : "B"
                }
            ]
        }
    ]
}

students = db.students


print("\n  --INSERT STATEMENTS  --")
thorin_student_id = students.insert_one(thorin).inserted_id
print("  Inserted student record Thorin Oakenshield into the students collection with document_id " + str(thorin_student_id))

bilbo_student_id = students.insert_one(bilbo).inserted_id
print("  Inserted student record Bilbo Baggins into the students collection with document_id " + str(bilbo_student_id))

frodo_student_id = students.insert_one(frodo).inserted_id
print("  Inserted student record Frodo Baggins into the students collection with document_id " + str(frodo_student_id))

input("\n\n  End of program, press any key to exit... ")