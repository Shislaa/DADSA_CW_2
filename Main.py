import csv

# Initalizing Patient class

class Patient():
    global feeding, grv, issue,GRV,Type,age,W,IssUpdate,DayLog,RankPoint
    def __init__(self):
        self.items = self
        self.items.feeding = [[0] * 24 for i in range(24)]
        self.items.grv = [[0] * 24 for i in range(24)]
        self.items.issue = [[0] * 24 for i in range(24)]
    def setRankPoint(self,value):
        self.items.RankPoint = value
    def getRankPoint(self):
        return self.items.RankPoint
    def getDayLog(self):
        return self.items.DayLog
    def setDayLog(self,value):
        self.items.DayLog = value
    def getIssueUpdate(self):
        return self.items.IssUpdate
    def setIssueUpdate(self,value):
        self.items.IssUpdate = value
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
                    if PA.getWeight() < 40:
                        PA.setGRVStandard(5 * PA.getWeight())
                    else:
                        PA.setGRVStandard(250)

                if row == dayrow:
                    time = int(0)
                    day = int(int(j[0]) - 1)
                    dayrow += 24
                if row >= 3:
                    Patient.setFeedingStatus(PA,day,time,j[2])
                    if j[3] != '':
                        Patient.setGRVStatus(PA,day,time,int(j[3]))
                    else:
                        Patient.setGRVStatus(PA, day, time, j[3])
                    Patient.setIssueStatus(PA,day,time,j[4])
                    time += 1
                row += 1
            PatientList.add(PA)



Data()
print("Hello ",PatientList.itemAt(3).getFeedingStatus(0,0))
def LR(PA,daycounter,Type):
    if Type == "LR":
        feedinit = int(5)
    elif Type == "HR":
        temp = PA.getFeedingStatus(2,20)
        feedinit = int(temp[0] + temp[1])
    grvstandard = PA.getGRVStandard()
    refercounter = int(0)
    for day in range(daycounter,5):
        for hr in range(0,24):
            if day == 0 and hr < 4 and Type == "LR":
                PA.setIssueStatus(day,hr,"NONE")
            elif day == 3 and hr < 3 and Type == "HR":
                PA.setIssueStatus(day,hr,"NONE")
            else:
                PGRVStatus = PA.getGRVStatus(day,hr)
                if PGRVStatus != '':
                    if(PGRVStatus <= grvstandard) and (PGRVStatus != 0):
                        GRVLower = True
                        feedinit += 5
                        PA.setFeedingStatus(day,hr,feedinit)
                        PA.setIssueUpdate("NONE")
                        PA.setIssueStatus(day,hr,PA.getIssueUpdate())
                        refercounter = 0
                    elif (PGRVStatus > grvstandard) and (PGRVStatus != 0):
                        GRVLower = False
                        if refercounter >= 2:
                            PA.setIssueUpdate("REFER TO DIETICIAN")
                            PA.setIssueStatus(day,hr,PA.getIssueUpdate())
                            refercounter = 0
                        else:
                            PA.setFeedingStatus(day,hr,"NO FEEDING")
                            PA.setIssueUpdate("FEEDING STOPPED")
                            PA.setIssueStatus(day,hr,PA.getIssueUpdate())
                            refercounter += 1
                else:
                    PA.setIssueStatus(day,hr,PA.getIssueUpdate())
                    if GRVLower == True :
                        PA.setFeedingStatus(day,hr,feedinit)
                    elif refercounter < 2 and PA.getIssueUpdate == "FEEDING STOPPED":
                        PA.setFeedingStatus(day,hr,"NO FEEDING")



def ranking(PAL):
    # Traverse through 1 to len(arr)
    for i in range(0,PAL.size()):
        PA = PAL.itemAt(i)
        DayLogTemp = List()
        for i in range(0,5):
            DayLogTemp.add(PA.getIssueStatus(i,23))
        PA.setDayLog(DayLogTemp)
    # [[[[[[[[  TESTING  ]]]]]]]]
    # TestList = List()
    #     # P1 = ["NONE", "NONE", "FEEDING STOPPED","FEEDING STOPPED","NONE", "NONE"]
    #     # P2 = ["FEEDING STOPPED","FEEDING STOPPED","REFER TO DIETICIAN","REFER TO DIETICIAN", "NONE", "NONE"]
    #     # P3 = ["NONE", "NONE", "NONE", "NONE", "NONE", "NONE"]
    #     # P4 = ["NONE", "NONE","FEEDING STOPPED", "NONE","REFER TO DIETICIAN", "NONE"]
    #     # TestList.add(P1)
    #     # TestList.add(P2)
    #     # TestList.add(P3)
    #     # TestList.add(P4)
    for i in range(0, PAL.size()):
        PA = PAL.itemAt(i)
        temp = PA.getDayLog()
        initpoint = int(20)
        rankpoint = int(0)
        none = int(1)
        stopfeed = int(2)
        refer = int(3)
        bns = int(0)
        bnd = int(0)
        ls = int(0)
        notNone = False
        for i in range(0, 5):
            print(temp.itemAt(i), " ", end='')
            if temp.itemAt(i) == "NONE":
                if notNone == True:
                    bns = 0
                    bnd = 0
                rankpoint += initpoint - none + bns + bnd
                bns += 1
                bnd = i * 2
                ls = 0
                notNone = False
            if temp.itemAt(i) == "FEEDING STOPPED":
                notNone = True
                rankpoint += initpoint - stopfeed - ls
                ls += 1
            if temp.itemAt(i) == "REFER TO DIETICIAN":
                notNone = True
                rankpoint += initpoint - refer - ls
                ls += 2
        PA.setRankPoint(rankpoint)
        print(" RankPoint: ", rankpoint)




    # for i in range(1, len(PAL)):
    #
    #     key = arr[i]
    #
    #     # Move elements of arr[0..i-1], that are
    #     # greater than key, to one position ahead
    #     # of their current position
    #     j = i - 1
    #     while j >= 0 and key < arr[j]:
    #         arr[j + 1] = arr[j]
    #         j -= 1
    #     arr[j + 1] = key

def main():
    for i in range(0,PatientList.size()):
        PA = PatientList.itemAt(i)
        if(PA.getType() == "HR"):
            LR(PA,3,"HR")
        else:
            LR(PA,0,"LR")
    ranking(PatientList)
main()

for i in range(0, PatientList.size()):
    PAtemp = PatientList.itemAt(i)
    if (PAtemp.getType() == "LR"):
        LR(PAtemp,0,"LR")
        print("////[[[[ PATIENT ", i, "]]]]")
        print("Day     Time     Feed     GRV     Issues")
        for i in range(0,5):
            print(i,end = '')
            for j in range(0,24):
                print("      ", j,"     ",PAtemp.getFeedingStatus(i,j),"     ",PAtemp.getGRVStatus(i,j),"     ",PAtemp.getIssueStatus(i,j))
        print("[[[[[[[ ]]]]]]]]")
#
