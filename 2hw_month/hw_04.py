class GeeksPeople: 
    def __init__(self, name, email, phone): 
        self.name = name  
        self.email = email 
        self.phone = phone 
                  
    def __str__(self): 
        return f"Имя - {self.name}, Email - {self.email}, Номер телефона - {self.phone}, " 
     
 
class Student(GeeksPeople): 
    def __init__(self, name, email, phone, student_id, group_where_study): 
        GeeksPeople.__init__(self, name, email, phone) 
        self.student_id = student_id 
        self.group_where_study = group_where_study 
         
         
    def study(self): 
        print(f"Студента - {self.name} учится в {self.group_where_study} группе") 
         
    def __str__(self): 
        return super().__str__() + f"ID студента {self.student_id}, Группа студента {self.group_where_study}" 
         
class Player(GeeksPeople): 
    def __init__(self, name, email, phone): 
        GeeksPeople.__init__(self, name, email, phone) 
         
    def __str__(self): 
        print(self.name) 
 
class Teacher(GeeksPeople): 
    def __init__(self, name, email, phone, teacher_id, group_where_teach): 
        GeeksPeople.__init__(self,name, email, phone) 
        self.teacher_id =teacher_id 
        self.group_where_teach = group_where_teach 
         
                 
    def teach(self): 
        print(f"Учитель - {self.name} преподает {self.group_where_teach} группе") 
         
    def __str__(self): 
        return super().__str__() + f"ID учителя {self.teacher_id}, Группа учителя {self.group_where_teach}, " 
         
 
 
 
class Admin(GeeksPeople): 
    def __init__(self, name, email, phone, admin_id): 
        GeeksPeople.__init__(self, name, email, phone) 
        self.admin_id = admin_id 
     
    def create_group(self, cours_name): 
        print(f"Админ - {self.name} Создал {cours_name} группу") 
         
    def __str__(self): 
        return super().__str__() + f"ID админа {self.admin_id}" 
 
 
class Mentor(Student, Teacher): 
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach): 
        super().__init__(name, email, phone, student_id, group_where_study) 
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach) 
         
student = Student("Хожиакбар", "takhirow77@gmail.com", "0990530084", 7878, "15-2B") 
print(student) 
student.study() 
 
teacher= Teacher("Сыймык", "syimyk@gmail.com", "07535725758252", 5555, "15-2B") 
print(teacher) 
teacher.teach() 
 
admin = Admin("Улан", "ulan@gmail.com", "030242424324", 4353) 
print(admin) 
admin.create_group("15-2B") 
 
mentor = Mentor("Нурай", "nuraij6963@gmail.com", "0755750238", 112313, "12-2B", 252525, "15-2B") 
print(mentor) 
mentor.study() 
mentor.teach()
