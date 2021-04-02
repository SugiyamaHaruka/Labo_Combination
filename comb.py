import numpy.random

#BeforeMember1、BeforeMember2...前回のメンバー
BeforeMember1, BeforeMember2 = 0, 0
count = 0
#Countmax...講義の回数
Countmax = 100
#｛メンバーの名前、回数｝
MemberDictionary = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
while(count < Countmax):
    #CurrentMember1、CurrentMember2...今回のメンバー
    CurrentMember1, CurrentMember2 = numpy.random.randint(1, 6, 2)
    #上記改善必須（現在は一様分布のランダムを利用中）
    if CurrentMember1 == CurrentMember2 or CurrentMember1 == BeforeMember1 or CurrentMember1 == BeforeMember2 or CurrentMember2 == BeforeMember1 or CurrentMember2 == BeforeMember2:
        pass
        #検証用↓
        #print("false! Member1 : " + str(CurrentMember1) + " Member2 : " + str(CurrentMember2))
    else:
        BeforeMember1 = CurrentMember1
        BeforeMember2 = CurrentMember2
        MemberDictionary[str(CurrentMember1)] = MemberDictionary[str(CurrentMember1)]+1
        MemberDictionary[str(CurrentMember2)] = MemberDictionary[str(CurrentMember2)]+1
        count = count+1
        print("Member1 : " + str(CurrentMember1) + " Member2 : " + str(CurrentMember2))

print(MemberDictionary)
