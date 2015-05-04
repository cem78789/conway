__author__ = 'ICY'
## Simple Conway's Game Of Life simulator. Based on few rules. Population and food.
import pygame,time,math,random
from msvcrt import getch
olu = (255,0,0)
yasayan = (0,255,0)
bos = (255,255,255)
siyah = (0,0,0)
satirs = 20
sutuns = 20
hucrekoordinatx = []
hucrekoordinaty = []
hucreyasam = []
hucrekordinat = []
yasakli = [19, 39, 59, 79, 99, 119, 139, 159, 179, 199, 219, 239, 259, 279, 299, 319, 339, 359, 379, 399]
secilim = [-21,-20,-19,-1,1,19,20,21]
class ekran:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))
        cizgixp = 640/satirs
        print cizgixp
        cizgiyp = 480/sutuns
        i = 0
        self.yaricap = math.sqrt((cizgixp*cizgixp+cizgiyp*cizgiyp)/4) - 9
        while i < satirs:
            a = i + i*cizgiyp
            #pygame.draw.line(self.screen,siyah,(0,a),(640,a),1)
            i1 = 0
            while i1 < satirs:
                self.circle(cizgiyp/2+i*cizgixp,cizgiyp/2+cizgiyp*i1,bos,1,0,"")
                i1 = i1 + 1
            i = i +1
        print i
        i = 0
        a = 0
        i1 = 0
        a1 = 0
        while i < sutuns:
            a = i + i*cizgixp
            #pygame.draw.line(self.screen,siyah,(a,0),(a,480),1)
            i = i +1
        print i
        i = 0
        pygame.display.flip()
    def circle(self,x,y,d,sifir,i,durum):
        if sifir == 1:
            pygame.draw.circle(self.screen,d,(x,y),int(self.yaricap))
            hucrekoordinatx.append(x)
            hucrekoordinaty.append(y)
            if d == yasayan:
                hucreyasam.append("1")
            else:
                hucreyasam.append("0")
        elif sifir == 0:
            if i > 0 and i<399:
                pygame.draw.circle(self.screen,d,(hucrekoordinatx[i],hucrekoordinaty[i]),int(self.yaricap))
                if d == (255,255,255):
                    hucreyasam[i] = "0"
                elif d == (0,255,0):
                    hucreyasam[i] = "1"
                    return "OK"
                elif d == (0,0,255):
                    hucreyasam[i] = "B1"
                    #print "Besin"
                for abc in yasakli:
                    pygame.draw.circle(self.screen,(255,0,0),(hucrekoordinatx[abc],hucrekoordinaty[abc]),int(self.yaricap))
                    hucreyasam[abc] = "0"
        pygame.display.update()
        pygame.event.get()
def yasaol():
    yasaolus = 0
    besin = 0
    i = 0
    byon = ""
    for canli in hucreyasam:
        yasaolus = 0
        besin = 0

        try:
            if hucreyasam[i - 1] == "1":
                yasaolus = yasaolus + 1
            if (hucreyasam[i-1].startswith("B") and i-1>=0) or (hucreyasam[i-2].startswith("B") and i-2>=0):
                besin = besin + 1
                byon = "Y"
        except:
            pass
        try:
            if hucreyasam[i + 1] == "1":
                yasaolus = yasaolus + 1
            if (hucreyasam[i+1].startswith("B") and i+1>=0) or (hucreyasam[i+2].startswith("B") and i+2>=0):
                besin = besin + 1
                byon = "A"
        except:
            pass
        try:
            if hucreyasam[i - 20] == "1":
                yasaolus = yasaolus + 1
            if (hucreyasam[i-20].startswith("B") and i-20>=0) or (hucreyasam[i-40].startswith("B") and i-40>=0) :
                besin = besin + 1
                byon = "S"
        except:
            pass
        try:
            if hucreyasam[i - 19] == "1":
                yasaolus = yasaolus + 1
            if (hucreyasam[i-19].startswith("B") and i-19>=0) or (hucreyasam[i-38].startswith("B") and i-38>=0):
                besin = besin + 1
                byon = "S"
        except:
            pass
        try:
            if (hucreyasam[i - 21] == 1):
                yasaolus = yasaolus + 1
            if (hucreyasam[i-21].startswith("B") and i-21>=0) or (hucreyasam[i-42].startswith("B") and i-42>=0):
                besin = besin + 1
                byon = "S"
        except:
            pass
        try:
            if hucreyasam[i + 20] == "1":
                yasaolus = yasaolus + 1
            if (hucreyasam[i+20].startswith("B") and i+20>=0) or (hucreyasam[i+40].startswith("B") and i+40>=0):
                besin = besin + 1
                byon = "SA"
        except:
            pass
        try:
            if hucreyasam[i + 21] == "1":
                yasaolus = yasaolus + 1
            if (hucreyasam[i+21].startswith("B") and i+21>=0) or (hucreyasam[i+42].startswith("B") and i+42>=0):
                besin = besin + 1
                byon = "SA"
        except:
            pass
        try:
            if hucreyasam[i + 19] == "1":
                yasaolus = yasaolus + 1
            if hucreyasam[i+19].startswith("B") and i+19>=0 or (hucreyasam[i+38].startswith("B") and i+38>=0):
                besin = besin + 1
                byon = "SA"
        except:
            pass
        if str(hucreyasam[i]).startswith("G"):
            hys = hucreyasam[i]
            if hys.endswith("9"):
                if random.randint(0,2) == 0:
                    hucreyasam[i] = "B1"
                    ekrana.circle(0,0,(0,0,255),0,i,"")
                else:
                    hucreyasam[i] = "0"
            else:
                hysl = list(hys)
                hysl[-1] = str(int(hysl[-1]) + 1)
                hucreyasam[i] = ''.join(hysl)

        if str(hucreyasam[i]).startswith("B"):
            hys = hucreyasam[i]
            if hys.endswith("9"):
                if random.randint(0,2) == 0:
                    ekrana.circle(0,0,(255,255,255),0,i,"")
                    hucreyasam[i] = "B1"
                else:
                    hysl = list(hys)
                    hysl[-1] = str(1)
                    hucreyasam[i] = ''.join(hysl)
                    print hucreyasam[i]
            else:
                hysl = list(hys)
                hysl[-1] = str(int(hysl[-1]) + 1)
                hucreyasam[i] = ''.join(hysl)

        if ((yasaolus == 0) or (yasaolus == 3)) and (hucreyasam[i] == "1") and besin !=0:
            while 1:

                secim = random.randint(0,2)
                if byon == "S":
                    yon = secilim[0:3]
                    if ekrana.circle(0,0,(0,255,0),0,(i + yon[secim]),"") == "OK":
                        break
                if byon == "SA":
                    yon = secilim[5:8]
                    if ekrana.circle(0,0,(0,255,0),0,(i + yon[secim]),"") == "OK":
                        break
                if byon == "Y":
                    yon = secilim[0],secilim[3],secilim[5]
                    if ekrana.circle(0,0,(0,255,0),0,(i + yon[secim]),"") == "OK":
                        break
                if byon == "A":
                    yon = secilim[2],secilim[4],secilim[7]
                    print i + yon[secim]
                    if ekrana.circle(0,0,(0,255,0),0,(i + yon[secim]),"") == "OK":
                        break




        elif (yasaolus >= 4) and hucreyasam[i] == "1" :
            ekrana.circle(0,0,(255,255,255),0,i,"")
            hucreyasam[i] = "G1"
            #ol
            # "ol"
        elif (yasaolus == 3 or yasaolus == 4) and (hucreyasam[i] == "0"):
            ekrana.circle(0,0,(0,255,0),0,i,"")
        elif (yasaolus < 2) and (hucreyasam[i] == "1"):
            hucreyasam[i] = "G1"
            ekrana.circle(0,0,(255,255,255),0,i,"")
        i = i + 1

class rastgeleolustur:
    def __init__(self):
        yasayansayi = 50
        i = 0
        while i < yasayansayi:
            konum = random.randint(0,399)
            ekrana.circle(0,0,(0,255,0),0,konum,"")
            i = i + 1
    def besin(self):
        besinsayi = 0
        besinsayi = 20
        i = 0
        while i < besinsayi:
            konum = random.randint(0,399)
            ekrana.circle(0,0,(0,0,255),0,konum,"")
            i = i + 1
ekrana = ekran()
baslat = rastgeleolustur()
baslat.besin()
ekrana.circle(0,0,(0,255,0),0,205,"")
ekrana.circle(0,0,(0,0,255),0,207,"")

print hucrekoordinatx
print hucrekoordinaty
print len(hucrekoordinaty),len(hucrekoordinatx)
print hucreyasam
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            #for a in hucrekoordinatx:
            #   print mouseX
            #    x_good = a in range(mouseX - 20, mouseX + 20)
            # for b in hucrekoordinaty:
            #     y_good = b in range(mouseY - 20, mouseY + 20)
            #print x_good
            #print y_good
            #if hucrekoordinatx.count(mouseX) != 0 and hucrekoordinaty.count(mouseY) != 0:
            #    print "test"
    print 'Olustur:\n'
    input_char = getch()

    if input_char.isdigit():
        print 'YES'
        hucreyasam[input_char] == "1"
    yasaol()
    time.sleep(1)
time.sleep(9999)
