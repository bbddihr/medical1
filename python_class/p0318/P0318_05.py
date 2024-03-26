class Tv:  #클래스 선언-설계도 
    channel =0
    color ="black"
    size =65
    volume= 0
    
    def __init__(self,color,size,volume,channel):
        self.color=color
        self.size=size
        self.volume=volume
        self.channel=channel
        

    # def __init__(self,color="",size=0,volume=0,channel=0):
    
    
    def up_volume(self,volume):
        self.volume +=volume
    def down_volume(self,volume):
        self.volume -= volume
    def up_channel(self,channel):
        self.channel += channel
    def down_channel(self,channel):
        self.channel -= channel

#철수-화이트,채널10변경, 2증가  
# 영희-핑크,채널7, 채널 5증가 
# 반장-실버,1 
t1=Tv()
t1.color="white"
t1.size =65
t1.volume=0
t1.channel=10
t1.up_channel(2)
print(f"철수 : {t1.color},{t1.channel},{t1.size}, {t1.volume}")


# t1=Tv(10,"white",)


# t2=Tv(f"핑크",65,0,7)
# print(f"영희TV: {t2.channel},{t2.color},{t2.size}, {t2.volume}")

# t2.color="pink"
# t2.channel=7
# t2.upchannel(5)

# t3=Tv(7,"pink")
# t3.color("silver")
# # print(" ": "channel","color","size", "volume")

