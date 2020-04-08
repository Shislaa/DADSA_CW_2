import csv

# [[ Initialize Patient class ]]

class Patient():
    global feeding, grv, issue,GRV,Type,age,W,IssUpdate,DayLog,RankPoint,name
    def __init__(self):
        self.items = self
# [[ Initialize feeding, grv and issue as 2-dimensional arrays ]]
        self.items.feeding = [[0] * 24 for i in range(24)]
        self.items.grv = [[0] * 24 for i in range(24)]
        self.items.issue = [[0] * 24 for i in range(24)]
# [[ Initialize Getters and Setters ]]
    def setName(self,value):
        self.items.name = value
    def getName(self):
        return self.items.name
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

# [[ Initialize List class ]]
class List(Patient):
    def __init__(self):
        self.items = []
# [[ Adding Method ]]
    def add(self,item):
        self.items.append(item)
# [[ Return the size of the List ]]
    def size(self):
        return len(self.items)
# [[ Remove the item at given index in the List ]]
    def removeAt(self,i):
        self.items.remove(self.items[i])
# [[ Return the item at given index in the List ]]
    def itemAt(self,i):
        return self.items[i]
# [[ Swap 2 items in the List at given indexes ]]
    def swap(self,index,indexswap):
        temp = self.items[index]
        self.items[index] = self.items[indexswap]
        self.items[indexswap] = temp

# [[ Initilize Patient List ]]
PatientList = List()

# [[ Method for processing data from files ]]
def Data():
# [[ Adding files' name to a List ]]
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
# [[ Loop through each file to process data ]]
    for i in range(0,10):
        with open(filename.itemAt(i)) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            nameTemp = filename.itemAt(i)
            PA = Patient()
            PA.setName(nameTemp[len(nameTemp) - 6] + nameTemp[len(nameTemp) - 5])
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
# [[ Run the Data method to input data from files to the PatientList ]]
Data()
# [[ Method to process data received from the files ]]
# [[ Process is explained in detail in the Pseudocode ]]
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
# [[ Since the GRV readings for LR patient only exist after 4 hr, we ignore the first 3 hr of the data ]]
            if day == 0 and hr < 4 and Type == "LR":
                PA.setIssueStatus(day,hr,"NONE")
# [[ The same goes for the HR patient, where the GRV readings only exist after day 3 and hr 3, we ignore the previous data ]]
            elif day == 3 and hr < 3 and Type == "HR":
                PA.setIssueStatus(day,hr,"NONE")
            else:
                # [[ Getting the GRV reading by day and hour ]]
                PGRVStatus = PA.getGRVStatus(day,hr)
                # [[ Check if the GRV reading is not empty ]]
                if PGRVStatus != '':
                    # [[ If the patient GRV reading is lower than the critical value, process according to the chart, the same goes for the other condition ]]
                    if(PGRVStatus <= grvstandard) and (PGRVStatus != 0):
                        GRVLower = True
                        # [[ Increase the feding value by 5 ]]
                        feedinit += 5
                        feedingvalue = str(feedinit) + "ML /2 HRS"
                        PA.setFeedingStatus(day,hr,feedingvalue)
                        PA.setIssueUpdate("NONE")
                        PA.setIssueStatus(day,hr,PA.getIssueUpdate())
                        # [[ Reset the refercounter ( explained in the Pseudocode ) if the GRV reading is lower than the critical value ]]
                        refercounter = 0
                    elif (PGRVStatus > grvstandard) and (PGRVStatus != 0):
                        GRVLower = False
                        # [[ Check if the refercounter is > 2 ( the patient has been stopped feeding for more than 2 times consecutively  )]]
                        if refercounter >= 2:
                            PA.setIssueUpdate("REFER TO DIETICIAN")
                            PA.setIssueStatus(day,hr,PA.getIssueUpdate())
                            refercounter = 0
                        else:
                            PA.setFeedingStatus(day,hr,"NO FEEDING")
                            PA.setIssueUpdate("FEEDING STOPPED")
                            PA.setIssueStatus(day,hr,PA.getIssueUpdate())
                            refercounter += 1
                # [[ This is to fill in the Issue and Feeding tatus of the patient in which row the GRV reading is empty ]]
                else:
                    PA.setIssueStatus(day,hr,PA.getIssueUpdate())
                    if GRVLower == True :
                        feedingvalue = str(feedinit) + "ML /2 HRS"
                        PA.setFeedingStatus(day,hr,feedingvalue)
                    elif refercounter < 2 and PA.getIssueUpdate == "FEEDING STOPPED":
                        PA.setFeedingStatus(day,hr,"NO FEEDING")

# [[ Method to rank the patient bases on their performance ]]
# [[ The algorithm is explained in detail in the Pseudocode ]]
def ranking(PAL):
    # [[ Getting the last entry of the day of a patient ]]
    for i in range(0,PAL.size()):
        PA = PAL.itemAt(i)
        DayLogTemp = List()
        for j in range(0,5):
            DayLogTemp.add(PA.getIssueStatus(j,23))
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
# [[ Refer to the Pseudocode for more detail about this section ]]
    for i in range(0, PAL.size()):
        PA = PAL.itemAt(i)
        temp = PA.getDayLog()
        initpoint = int(20)
        rankpoint = int(0)
        none = int(1)
        stopfeed = int(2)
        refer = int(8)
        bns = int(0)
        bnd = int(0)
        ls = int(0)
        ld = int(0)
        notNone = False
        for i in range(0, 5):
#            print(temp.itemAt(i), " ", end='')
            if temp.itemAt(i) == "NONE":
                if notNone == True:
                    bns = 0
                    bnd = 0
                rankpoint += initpoint - none + bns + bnd
                bns += 1
                bnd = i * 2
                ls = 0
                ld = 0
                notNone = False
            if temp.itemAt(i) == "FEEDING STOPPED":
                notNone = True
                rankpoint += initpoint - stopfeed - ls - ld
                ls += 1
                ld  = i*2
            if temp.itemAt(i) == "REFER TO DIETICIAN":
                notNone = True
                rankpoint += initpoint - refer - ls - ld
                ls += 2
                ld = i*2
        PA.setRankPoint(rankpoint)
#        print(" RankPoint: ", rankpoint)


# [[[ Sorting by rankpoint ]]]
    for i in range(PAL.size()):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, PAL.size()):
            if PAL.itemAt(min_idx).getRankPoint() < PAL.itemAt(j).getRankPoint():
                min_idx = j

                # Swap the found minimum element with
        # the first element
        PAL.swap(min_idx,i)
# [[ Rank printing method ]]
def printranking():
    # [[ Process patients' data using LR() method ]]
    for i in range(0,PatientList.size()):
        PA = PatientList.itemAt(i)
        if(PA.getType() == "HR"):
            LR(PA,3,"HR")
        else:
            LR(PA,0,"LR")
    # [[ Run the Ranking method ]]
    ranking(PatientList)
    # [[ Loop through the List to print out the ranking ]]
    for i in range(0,PatientList.size()):
        daylog = PatientList.itemAt(i).getDayLog()
        print("PATIENT ",PatientList.itemAt(i).getName(),": [ ",end ='')
        for j in range(0,5):
            canprint = True
            if PatientList.itemAt(i).getName() == "B1" and j == 4:
                canprint = False
            if canprint is True:
                print(daylog.itemAt(j)," ",end = '')
        print("] RankPoint: ", PatientList.itemAt(i).getRankPoint())
# [[ Patients' Data printing method ]]
def printdata():
    # [[ Process the patient Data while also printing it out ]]
    for i in range(0, PatientList.size()):
        PAtemp = PatientList.itemAt(i)
        if (PAtemp.getType() == "LR"):
            LR(PAtemp, 0, "LR")
        else:
            LR(PAtemp,3,"HR")
        print("////[[[[ PATIENT ", PAtemp.getName(), "]]]]")
        print("Day     Time     Feed     GRV     Issues")
        if PAtemp.getName() == "B1":
            daycounter = 4
        else:
            daycounter = 5
        for i in range(0, daycounter):
            print(i + 1, end='')
            for j in range(0, 24):
                print("      ", j, "     ", PAtemp.getFeedingStatus(i, j), "     ", PAtemp.getGRVStatus(i, j),
                      "     ", PAtemp.getIssueStatus(i, j))
        print("[[[[[[[ ]]]]]]]]")
# [[ The main method ]]
def main():
    print("Welcome to PICU Data Processing Software")
    print("Press 1 for processed patients' data, 2 for patients' ranking, 0 to exit : ")
    tempinput = input()
    if tempinput == "1":
        printdata()
        print("If you wish to continue, press 1, otherwise press 0: ")
        tempinput1 = input()
    if tempinput == "2":
        printranking()
        print("If you wish to continue, press 1, otherwise press 0: ")
        tempinput1 = input()
    if tempinput == "0":
        tempinput1 = 0
    if tempinput1 == "1":
        main()
    elif tempinput1 != "1" or tempinput == "0":
        print("Thank you for using the software!")
        print("Made by Minh H Nguyen.")

# Running the main method

main()


