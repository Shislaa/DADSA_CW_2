import csv

# Initalizing Patient class
class Patient():
    global feeding, grv, issue,GRV,Type,age,W
    def __init__(self):
        self.items = self
        self.items.feeding = [[0] * 24 for i in range(24)]
        self.items.grv = [[0] * 24 for i in range(24)]
        self.items.issue = [[0] * 24 for i in range(24)]
    def getFeedingStatus(self,day,hr):
        return self.items.feeding[day][hr]
    def setFeedingStatus(self,day,hr,value):
        self.items.feeding[day][hr] = value
    def getGRVStatus(self,day,hr):
        return self.items.grv[day][hr]
    def setGRVStatus(self,day,hr,value):
        self.items.grv[day][hr] = value
    def getIssueStatus(self,day,hr):
        return self.items.issue[day][hr]
    def setIssueStatus(self,day,hr,value):
        self.items.issue[day][hr] = value
    def getGRVStandard(self):
        return self.items.GRV
    def setGRVStandard(self,value):
        self.items.GRV = value
    def getType(self):
        return self.items.Type
    def setType(self,value):
        self.items.Type = value
    def getAge(self):
        return self.items.age
    def setAge(self,value):
        self.items.age = value
    def getWeight(self):
        return self.items.W
    def setWeight(self,value):
        self.items.W = value
class List(Patient):
    def __init__(self):
        self.items = []
    def add(self,item):
        self.items.append(item)
    def size(self):
        return len(self.items)
    def removeAt(self,i):
        self.items.remove(self.items[i])
    def itemAt(self,i):
        return self.items[i]

PatientList = List()

def Data():
    filename = List()
    filename.add("PATIENT DATA - PATIENT A1.csv")
    filename.add("PATIENT DATA - PATIENT A2.csv")
    filename.add("PATIENT DATA - PATIENT A3.csv")
    filename.add("PATIENT DATA - PATIENT B1.csv")
    filename.add("PATIENT DATA - PATIENT B2.csv")
    filename.add("PATIENT DATA - PATIENT B3.csv")
    filename.add("PATIENT DATA - PATIENT B4.csv")
    filename.add("PATIENT DATA - PATIENT B5.csv")
    filename.add("PATIENT DATA - PATIENT B6.csv")
    filename.add("PATIENT DATA - PATIENT B7.csv")
    for i in range(0,10):
        with open(filename.itemAt(i)) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            PA = Patient()
            row = int(0)
            dayrow = int(3)
            for j in reader:
                if row == 0:
                    PA.setType(j[1])
                    temp = j[2]
                    age = int(temp[4]+temp[5])
                    PA.setAge(age)
                    temp = j[4]
                    weight = float(temp[7]+temp[8]+temp[9])
                    PA.setWeight(weight)
                if row == dayrow and dayrow < 100:
                    time = int(0)
                    day = int(j[0])
                    dayrow += 24
                if row >= 3 and dayrow < 100:
                    Patient.setFeedingStatus(PA,day,time,j[2])
                    Patient.setGRVStatus(PA,day,time,j[3])
                    Patient.setIssueStatus(PA,day,time,j[4])
                    time += 1
                row += 1
            PatientList.add(PA)



Data()
print("Hello ",PatientList.itemAt(0).getFeedingStatus(3,4))