##Simple Code to manage lectures.
##Input Format:
##first line: Name
##second line: No. of lectures attended
##third line: No. of lectures delivered

name=input("Enter Name: ")
lecturesAttended=int(input("No. of lectures attended: "))
totalLectures=int(input("No. of lectures delivered: "))
attendence=lecturesAttended*100/totalLectures
if(attendence>75):
    bunk=0
    while(attendence>75):
        totalLectures+=1
        attendence=lecturesAttended*100/totalLectures
        if(attendence>=75):
            bunk+=1
    print(name,", Bunks allowed to keep attendence in safe zone :",bunk)
elif(attendence<75):
    attend=0
    while(attendence<75):
        attend+=1
        lecturesAttended+=1
        totalLectures+=1
        attendence=lecturesAttended*100/totalLectures
    print(name,", Minimum lectures required to attend to get to the safe zone :",attend)
else:
    print(name,", No bunks allowed as attendence is 75%")
