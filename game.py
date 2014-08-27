#coding:utf-8
import time,sys,os
class ProgressBar():#进度条
    def __init__(self, width=50):
        self.pointer = 0
        self.width = width
    def __call__(self,x):
         # x in percent
         self.pointer = int(self.width*(x/100.0))
         return "|" + "#"*self.pointer + "-"*(self.width-self.pointer)+\
                "|\n %s%s 正在加载中" %(x,'%')
class People:#父类
    def __init__(self,name,age,gender,issers,stature):
        self.name=name
        self.age=age
        self.gender=gender
        self.issers=issers
        self.stature=stature
    def tallking(self,who,t_what):
        self.who=who
        self.t_what=t_what
        print "%s:%s"%(self.who,self.t_what)
        time.sleep(1.5)
    def self_info(self):
        print "我叫%s,今年%s岁,我是一个%s,我的身高是%s,我的资产是%s"%\
        (self.name,self.age,self.gender,self.issers,self.stature)
        time.sleep(1.5)

class loser(People):#屌丝
    skill=[]
    def learn(self,where,w_learn,learn_time):
        self.where=where
        self.w_learn=w_learn
        self.learn_time=learn_time
        print "%s在%s学习%s要%s毕业,经过艰苦的奋战终于毕业."%\
        (self.name,self.where,self.w_learn,self.learn_time)
        time.sleep(1.5)
    def change_work(self,company,salary):
        self.company=company
        self.salary=salary
        print "%s现在在%s工作,月薪%s."%(self.name,self.company,self.salary)
        time.sleep(1.5)
    def add_salary(self,salary):
        self.salary=salary
        print "%s现在的工资是%s"%(self.name,self.salary)
        time.sleep(1.5)
class beauty(People):#美女类
    def change_lover(self,b_who):
        self.b_who=b_who
        print "%s,现在的男朋友是%s."%(self.name,self.b_who)
        time.sleep(1.5)
class handsome(People):#高富帅类
    def lie(self,h_who):
        self.h_who=h_who
        print "%s:hi %s你真漂亮,让我心都碎了,,,,,,我很有钱，我们在一起吧！"%(self.name,self.h_who)
        time.sleep(1.5)

            
class House:#父类房子
    def __init__(self,h_type,H_name):
        self.h_type=h_type
        self.H_name=H_name
        
class School(House):#学校
    S_name='OLDBOY'
    headmaster="老男孩"
    teacher='Alex'
    def __init__(self,name,course,teacher,s_time,h_type,H_name):
        self.course=course
        self.teacher=teacher
        self.s_time=s_time
        self.name=name
        self.h_type=h_type
        self.H_name=H_name
    def study(self):
        print '%s在这里学习了%s个月时间的%s'\
        %(self.name,self.s_time,self.course)
        time.sleep(1.5)
    def end_study(self,student,grade):
        self.student=student
        self.grade=grade
        if self.grade=='yes':
            print "校长开了毕业典礼,因为我的成绩非常优秀，还奖励了我一朵大红花.推荐我去谷歌进行面试."
            print "-------------------------------------------------------------------"           
            time.sleep(1.5)
        elif self.grade=='no':
            print "校长开了毕业典礼,因为我成绩很差,不准我毕业,并让我再重读。"
    def self_info(self):
        print "这是一个很%s的学校,在%s,名字叫%s,但是教%s的%s老师很负责,你需要在这里学习%s"\
        %(self.h_type,self.H_name,self.S_name,self.course,School.teacher,self.course)
        time.sleep(1.5)
class Company(House):#公司
    name=None
    address=None
    jobs=['保安','python开发','技术支持']
       
    def interview(self,interview,skill):
        self.interview=interview
        self.skill=skill
        while True:    
            print "%s:您要面试什么职位？"%self.interview
            for i,k in enumerate(Company.jobs):
                print i+1,k
            what_i=raw_input("what do you choose!")
            if what_i not in ['1','2','3']:
                print "sorry,您只能选择1-3的数字..."
                continue
            else:    
                print "让我先看看你的简历,我得知道你会哪些东西."
                print "-------------------------------------------------------"
                time.sleep(2)
                a=set(self.skill)
            
                if len(list(a))<3:
                    print "对不起，你会的东西实在是太少了,先去多学几个技能吧。"
                    print "-------------------------------------------------------"
                    return 'shao'
                else:
                    print '\t'.join(a)
                    print "ok.很好,现在回答我的几个问题吧！"
                    total=0
                    try:
                        linux=int(raw_input("linux:1.了解 2.熟练 3.精通:"))
                        python=int(raw_input("python:1.了解 2.熟练. 3.精通:"))
                        xueli=int(raw_input("学历：1.大专. 2.本科 3.硕士:"))
                        English=int(raw_input("英文水平:1.会音标 2.4级 3.6级:"))
                        if linux>3 or python>3 or xueli>3 or English>3:
                            print "操作错误,只能选择1-3的选项."
                            continue
                        else:    
                            total=linux+python+xueli+English
                            if what_i=='1':
                                if total<=5:
                                    print "面试失败"
                                    return False
                                else:
                                    print "面试成功欢迎你来到谷歌公司上班"
                                    return "保安"
                            elif what_i=='2':
                                if total<=10:
                                    print "面试失败."
                                    return False
                                else:
                                    print "面试成功欢迎你来到谷歌公司上班."
                                    return "python"
                            elif what_i=='3':
                                if total<8:
                                    print "面试失败."
                                    return False
                                else:
                                    print "面试成功欢迎你来到谷歌公司上班."
                                    return "技术支持"
                            else:
                                print "\033[5;35;10m没有这个职位.\033[0m"
                                break
                    except:
                        print "你只能输入1-3的数字"
                        continue
#------------------------------------------------------------------------------
def learn_english():#学习英语的过程
    oldboy=School('Jhon','English','美女','3','小','青年创业大厦')
    oldboy.study()
    Jhon.skill.append('English')
    oldboy.self_info()
    Jhon.learn('OLDBOY','English','3个月')
    time.sleep(1.5)
    oldboy.end_study('Jhon','yes')
def inter():#面试的过程
    google_com=Company('大厦','谷歌')
    what_skill=Jhon.skill
    a=google_com.interview('面试官',what_skill)
    if a=="技术支持" or a == "保安":
        print "若干年后....." 
        time.sleep(1)
        print"jhon 的工资5千一个月，在北京住着地下室....."
        time.sleep(0.5)
        print "有一天,偶然看见了Liz,发现她已经被甩了,"
        time.sleep(0.5)
        Liz.tallking('Liz','Jhon,别幸灾乐祸，你这样我就是死也不会跟你一起的。')
        raw_input("\033[5;35;10m请按确认键继续,或者Ctrl+C退出\033[0m")
    elif a == False:
        print "您现在可能不适合干这份工作，明年再来吧！"
    elif a=="python":
        Jhon.change_work('谷歌','50000')
        time.sleep(1)
        print "万万没想到,若干年后.....Jhon升职加薪当上总经理,出任CEO,走向人生巅峰"
        time.sleep(0.5)
        print"jhon 的工资50万一个月，在北京买了车和房....."
        time.sleep(0.5)
        print "有一天,偶然看见了Liz,发现她已经被甩了,"
        Jhon.add_salary('50万')
        Liz.tallking('Liz','Jhon,我们和好好吗？')
        what_say=raw_input("Jhon说:")
        if  len(what_say)!=0:
            pass
        else:
            what_say="beach. I don't want to be with you anymore."
        Jhon.tallking('Jhon',what_say)
        sys.exit("本次游戏结束.")
#--------------------游戏开始-----------------------        
os.system('clear')
pb = ProgressBar()
for i in range(101):
    os.system('clear')
    print pb(i)
    time.sleep(0.07)
while True:    
    person=['handsome','beauty','loser']
    for k,v in enumerate(person):
        print k+1,v
    Peter=handsome('Peter','28','handsome','1.8','100WRMB')
    Jhon=loser('Jhon','23','loser','1.6','100RMB')
    Liz=beauty('Liz','23','beauty','1.5','0')
    charater=raw_input("Please select a character:")#选择角色
    if charater=='1':#handsome
        print "暂时还未开放此角色!"
        raw_input("\033[5;35;10m请按任意键继续.\033[0m")
        continue
    elif charater=='2':#beauty
        print "暂时还未开放此角色!"
        raw_input("\033[5;35;10m请按任意键继续.\033[0m")
        continue
    elif charater=='3':#loser
        os.system("clear")
        print "Liz和Jhon是高中时期的一对恋人,可是Liz考上了北京城市学院后,Jhon确没有......"
        time.sleep(1)
        print "\033[5;31;10m游戏开始.....................\033[0m"
        Jhon.self_info()
        Jhon.tallking('Jhon',"Hi,Liz我没有考上大学.")
        Liz.tallking('Liz',"Hi,Jhon没关系的我还是会爱着你。")
        Jhon.tallking('Jhon',"Liz 你真好。")
        Liz.tallking('Liz',"呵呵~~~!")
        #jhon 无奈当上网管
        print "Jhon,你现在只能去北京打工当网管来给你女朋友教学费,你要去吗？"
        cos=None
        while True:
            j_w1=raw_input('Y/N:')
            if j_w1=="Y" or j_w1=="y":
                Jhon.change_work('网吧','2500')
                time.sleep(0.5)
                Jhon.skill.append('linux')
                cos='ok'
            elif j_w1=='N' or j_w1=="n":
                print "游戏到这里结束,Jhon决定当一辈子的屌丝"
                time.sleep(1)
                raw_input("\033[5;35;10m任意键重玩儿.退出CTRL+C\033[0m")
                break
            else:
                print "\033[5;31;10m亲，你只能接受或者拒绝.\033[0m"
                continue
            break
        if cos =='ok':
            print "三年后...Liz拿着Jhon的钱终于毕业了...结果却是..."
            time.sleep(2.5)
            os.system('clear')
            Peter.self_info()
            time.sleep(0.5)
            Peter.lie('Liz')
            time.sleep(0.5)
            Liz.change_lover('Peter')
            time.sleep(0.5)
            print "两人终于苟且的生活在了一起!当Jhon发现后...."
            time.sleep(1)
            print("john，你甘心当一辈子的网管吗？")
            wg=None
            while True: 
                a=raw_input('Y/N:')
                if a=='Y' or a == 'y':
                    print "活该一辈子被人甩,你继续当你的网管去吧！"
                    raw_input("\033[5;35;10m任意键重玩儿.退出CTRL+C\033[0m")
                elif a=='N' or a=='n':
                    os.system('clear')    
                    print "很好，你是一个有上进心的男人..."
                    b_list=['老男孩学习python','黑马学习java']
                    time.sleep(1)
                    wg='ok'
                else:
                    print "\033[5;31;10m亲.你确定有这个选项吗?\033[0m"
                    continue
                break
            if wg=='ok':    
              while True:
                for i,k in enumerate(b_list):
                    print i+1,k
                b=raw_input('那么你是准备怎么做呢?请选择:')
                if b=='1':
                    oldboy=School('Jhon','Python','Alex','4','小','青年创业大厦')
                    oldboy.study()
                    oldboy.self_info()
                    Jhon.learn('OLDBOY','python','4个月')
                    time.sleep(1.5)
                    by=raw_input("1+1=?")
                    if by=='2':
                       Jhon.skill.append('Python')
                       while True:     
                           print "你可以继续留在这儿继续学习学英语."
                           list_school=['不用了我要去面试','继续学习英语']
                           for i,k in enumerate(list_school):
                               print i+1,k
                           con_learn=raw_input("您的选择是?:")
                           if con_learn=='1':
                               oldboy.end_study('Jhon','yes')
                               os.system('clear')
                               print '---------------------------------------------'
                               print "jhon 来到谷歌的公司后......"
                               time.sleep(0.5)
                               google_com=Company('大厦','谷歌')
                               what_skill=Jhon.skill
                               a=google_com.interview('面试官',what_skill)
                               if a=="shao":
                                 while True:  
                                   sha_le=raw_input("Jhon,你要继续学英语吗？Y/N:")
                                   if sha_le=='Y' or sha_le=='y':
                                        learn_english()
                                        os.system('clear')
                                        while True:
                                            once=raw_input("Jhon,你还是要谷歌面试吗?Y/N:")
                                            if once=='Y' or once=='y':
                                                print "Jhon 再次来到谷歌的公司之后...."
                                                time.sleep(0.5)
                                                inter()
                                            elif once=='N' or once=='n':
                                                print "游戏到此结束"
                                                raw_input("\033[5;35;10m任意键返回.退出CTRL+C\033[0m")
                                                continue
                                            else:
                                                print "\033[5;35;10m没有这个选项.\033[0m"
                                                continue   
                                   elif sha_le=='N' or sha_le=='n':
                                        print "游戏到此结束"
                                        raw_input("\033[5;35;10m任意键返回.退出CTRL+C\033[0m")
                                        continue
                                   else:
                                        print "\033[5;35;10m没有这个选项.\033[0m"
                                        continue
                           elif con_learn=='2':
                               learn_english()
                               os.system('clear')
                               print '---------------------------------------------'
                               print "jhon 来到谷歌的公司后......"
                               time.sleep(0.5)
                               inter() 
                           else:
                               print "\033[5;35;10m没有这个选项.\033[0m"
                               continue      
                    else:
                        print "这么简单的题目都答不出来，怪不得，是矮矬穷。你在重新学一遍吧........"
                        raw_input("\033[5;35;10m任意键重玩儿.退出CTRL+C\033[0m")
                    continue
                elif b=='2':
                    print "jhon 由于在黑马受到非人类般的虐待，半个月后见佛祖去了....."
                    raw_input("\033[5;35;10m任意键返回.退出CTRL+C\033[0m")
                    continue
                else:
                    print "\033[5;35;10m没有这个选项哦.\033[0m"
                    continue
            else:
                continue        
        else:
            continue        
    else:
        print "您只能选择(1-3)"
        raw_input("\033[5;35;10m任意键重玩儿.退出CTRL+C\033[0m")
        continue
    break    
