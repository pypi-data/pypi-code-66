class consoleCanvas:
    def __init__(self):
        #这些字符是盲文字符
        self.li=["⠀", "⠁", "⠂", "⠃", "⠄", "⠅", "⠆", "⠇", "⠈", "⠉", "⠊", "⠋", "⠌", "⠍", "⠎", "⠏",
            "⠐", "⠑", "⠒", "⠓", "⠔", "⠕", "⠖", "⠗", "⠘", "⠙", "⠚", "⠛", "⠜", "⠝", "⠞", "⠟",
            "⠠", "⠡", "⠢", "⠣", "⠤", "⠥", "⠦", "⠧", "⠨", "⠩", "⠪", "⠫", "⠬", "⠭", "⠮", "⠯",
            "⠰", "⠱", "⠲", "⠳", "⠴", "⠵", "⠶", "⠷", "⠸", "⠹", "⠺", "⠻", "⠼", "⠽", "⠾", "⠿",

            "⡀", "⡁", "⡂", "⡃", "⡄", "⡅", "⡆", "⡇", "⡈", "⡉", "⡊", "⡋", "⡌", "⡍", "⡎", "⡏",
            "⡐", "⡑", "⡒", "⡓", "⡔", "⡕", "⡖", "⡗", "⡘", "⡙", "⡚", "⡛", "⡜", "⡝", "⡞", "⡟",
            "⡠", "⡡", "⡢", "⡣", "⡤", "⡥", "⡦", "⡧", "⡨", "⡩", "⡪", "⡫", "⡬", "⡭", "⡮", "⡯",
            "⡰", "⡱", "⡲", "⡳", "⡴", "⡵", "⡶", "⡷", "⡸", "⡹", "⡺", "⡻", "⡼", "⡽", "⡾", "⡿",

            "⢀", "⢁", "⢂", "⢃", "⢄", "⢅", "⢆", "⢇", "⢈", "⢉", "⢊", "⢋", "⢌", "⢍", "⢎", "⢏",
            "⢐", "⢑", "⢒", "⢓", "⢔", "⢕", "⢖", "⢗", "⢘", "⢙", "⢚", "⢛", "⢜", "⢝", "⢞", "⢟",
            "⢠", "⢡", "⢢", "⢣", "⢤", "⢥", "⢦", "⢧", "⢨", "⢩", "⢪", "⢫", "⢬", "⢭", "⢮", "⢯",
            "⢰", "⢱", "⢲", "⢳", "⢴", "⢵", "⢶", "⢷", "⢸", "⢹", "⢺", "⢻", "⢼", "⢽", "⢾", "⢿",

            "⣀", "⣁", "⣂", "⣃", "⣄", "⣅", "⣆", "⣇", "⣈", "⣉", "⣊", "⣋", "⣌", "⣍", "⣎", "⣏",
            "⣐", "⣑", "⣒", "⣓", "⣔", "⣕", "⣖", "⣗", "⣘", "⣙", "⣚", "⣛", "⣜", "⣝", "⣞", "⣟",
            "⣠", "⣡", "⣢", "⣣", "⣤", "⣥", "⣦", "⣧", "⣨", "⣩", "⣪", "⣫", "⣬", "⣭", "⣮", "⣯",
            "⣰", "⣱", "⣲", "⣳", "⣴", "⣵", "⣶", "⣷", "⣸", "⣹", "⣺", "⣻", "⣼", "⣽", "⣾", "⣿"]
    def ProduceCanvas(self,Width, height):
        #生成画布
        map_c=[[0 for i in range(Width)]  for i in range(height)]
        for wi in range((len(map_c)%3)+(len(map_c)%3)):#补齐行数不足宽度
            map_c.append([0 for i in range(len(map_c[0]))])

        for hi in map_c:##补齐列数不足宽度
            for n in range((len(map_c)%3)+(len(map_c)%3)):
                hi.append(0)    
        self. map_c=  map_c
        return self.map_c

    def reviseCanvas(self,position, data):
        #绘制像素点
        self.map_c[position[0]][position[1]]=data
        return self

    def getnum(self,data):
        #匹配字符索引
        q=[
        [1,8],
        [2,16],
        [4,32],
        [64,128],]
        num=0
        for w in range(len(data)):
            for h in range(len(data[w])):
                if (data[w][h]==1):
                    num+=q[w][h]
        return num


    def show(self,map_c=""):
        #渲染画布
        if map_c=="":
            map_c=self.map_c

        list_data=[]
        for w in range(0,len(map_c),3): #切片地图，变换地图
            lis=[]
            for i in range(0,len(map_c[w]),2):
                lis.append([map_c[w][i:i+2],map_c[w+1][i:i+2],map_c[w+2][i:i+2]])
                
            list_data.append(lis)

        for  i in list_data: #显示地图
            for x in i:
                num=self.getnum(x)
                print(self.li[num],end="")
            print()

if __name__ == "__main__":
    
    #绘制圆形
    import os,time
    A=consoleCanvas()#初始化
    A.ProduceCanvas(80,80)#创建画布

    a=50
    b=50
    r=20
    A.reviseCanvas([0,0],1)


    for x in range(a-r,a+r):
        y=int((((r**2)-(x-a)**2)**(1/2))+b)
        A.reviseCanvas([x,y],1)#绘制画布像素
    for x in range(a+r,a-r,-1):
        y=int(-1*(((r**2)-(x-a)**2)**(1/2))+b)
        A.reviseCanvas([x,y],1)#绘制画布像素
    A.show() #显示画布





    # for i in range(80):
    #     A.reviseCanvas([i,i],0)
    #     A.show() #显示画布
    #     time.sleep(0.1)
    #     os.system("cls")    
    
    # import cv2
    # img=cv2.imread("3.png")
    # image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转灰度
    # blur = cv2.GaussianBlur(image,(5,5),0) # 阈值一定要设为 0 ！高斯模糊
    # ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # 二值化 0 = black ; 1 = white
    # print(type(th3.tolist()))
    # open("1.txt","w").write(str(th3.tolist()))
    # cv2.imshow('image', th3)
    # a = cv2.waitKey(0)
    # # cv2.imshow('image', th3)
    