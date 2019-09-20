
#you can determine if a variable is protected = _ ie: self._myvariable
#you can determine if a variable is private = __ ie: self.__myvariable

class Person:
    def __init__(self,fname,lname,age,address,email,phone,gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.address = address
        self.email = email
        self.phone = phone
        self.gender = gender
    def isRelated(self,towho):
        if self.lname == towho.lname:
            print("Yes they're related");
        else:
            print("no they're not related");
class Student:
    def __init__(self,personal,school,gpa,classes):
        self.personal=personal
        self.school=school
        self.gpa=gpa
        self.classes=classes

    def isFailing(self,fail):
        if self.gpa < 2.5 :
            print("Yes, They're failing. ")
        else:
            print("No, They're not failing")

class Classes:
    def __init__(self):
        self.classDict={" ":" "} # initialize a dictionary in classes
    def addClass(self,classCode,className):#adds a class
        self.classDict.update({classCode:className})
        print("Successfully added " + classCode + " : "+className)
    def removeClass(self,classCode):#removes a class
        del self.classDict[classCode]
    def printClasses(self):
        for entry in self.classDict:
            print(entry +" : "+ self.classDict[entry]);
    
class University:
    def __init__(self):
        self.students=[];
        self.professors=[];
        self.classes=[];
    def addStudents(self,students):
        self.students=students
    def addANewStudent(self,student):
        self.students.append(student)
    def removeAStudent(self,student):
        self.students.remove(student)
    def addClasses(self,classes):
        self.classes=classes
    def addANewClass(self,aClass):
        self.classes.append(aClass)
    def removeAClass(self,aClass):
        self.classes.remove(aClass)
    def addProfessors(self,prof):
        self.professors=prof
    def addAProf(self,aProf):
        self.professors.append(aProf)
    def removeAProf(self,aProf):
        self.professors.remove(aProf)
        


        
kevin = Person("kevin","nguyen",23,"1234 Generic St.", "kevinnguyen@email.com","1112223456","Male");
ana = Person("Ana","espiritu",22,"4321 Generic St.","anaespiritu@email.com","2221114321","Female");
mom = Person("Bebe","nguyen",34,"1234 Generic St.","bebenguen@mgial.com","2131231233","Female");
teacher = Person("Teacher", "McTeach", 55, "1234 school address","teacher@email.com","123123123","Male");


kevClasses = Classes();
kevClasses.addClass("CS111","Intro to Computer Science")
kevClasses.addClass("CS211","Intro to Computer Science II")
anaClasses = Classes();
anaClasses.addClass("ACCT201","Intro to Accounting")
anaClasses.addClass("BUS304","Business Models")


kevinS = Student(kevin, "CSUSM", 3.133, kevClasses)
anaS = Student(ana,"CSUSM",3.133,anaClasses)
studentsList = [kevinS,anaS];


kevClasses.printClasses();
kevinS.personal.isRelated(mom);

CSUSM = University();
CSUSM.addANewStudent(kevinS)
CSUSM.addANewStudent(anaS)
CSUSM.addAProf(teacher)
CSUSM.addClasses(studentsList)
for i in range(len(CSUSM.students)):   
    print(CSUSM.students[i].personal.fname);

