count=0
fpp=open("obyov.csv","w")
batc=open("clusteredplayers/batout.txt","r")
row=batc.read().split('\n')
#bat_cli_inp=[x.split(',') for x in row]
bowlc=open("clusteredplayers/ballout.txt","r")
row=bowlc.read().split('\n')
bowl_cli_inp=[x.split(',') for x in row]
#print(bowl_cli_inp)
for i in range(636):
    lis=[]
    file=open("output/aaa"+str(i)+".csv","r")
    content=file.readlines()
    for i in content:
        if(len(i)>1):
            lis.append(i)
    lis=[x.split("\n")[0].split(',') for x in lis]
    overbyover1=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    overbyover2=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in lis:
        if(i[0]=="1st innings"):
            overbyover1[int(float(i[1])//1)].append(i)
        else:
            overbyover2[int(float(i[1])//1)].append(i)
    for i in overbyover1:
        if(len(i)<2):
            break
        boname=i[0][4]
        bowl_c, bowl_eco, bowl_avg,bat1_c,bat1_avg,bat1_sr,bat2_c,bat2_avg,bat2_sr,runs,wickets=0,0,0,0,0,0,0,0,0,0,0
        for j in i:
            if(len(j)>9):
                wickets+=1
            runs+=int(j[6])
        for j in bowl_cli_inp:
            try:
                if(j[1]==boname):
                    bowl_c=int(j[0])
                    try:
                        bowl_eco=float(j[2])
                    except:
                        bowl_eco=0
                    try:
                        bowl_avg=float(j[3])
                    except:
                        bowl_avg=0
                    break
            except:
                bowl_c=1
                bowl_eco=0
                bowl_avg=0
        lastname=i[-1][3]
        lastoppbat=i[-1][5]
        #print(lastname,lastoppbat)
        for j in bat_cli_inp:
            try:
                if(j[1]==lastname):
                    bat1_c=int(j[0])
                    try:
                        bat1_avg=float(j[2])
                    except:
                        bat1_avg=0
                    try:
                        bat1_sr=float(j[3])
                    except:
                        bat1_sr=0
                    break
            except:
                bat1_c=1
                bat1_avg=0
                bat1_sr=0
        for j in bat_cli_inp:
            try:
                if(j[1]==lastoppbat):
                    bat2_c=int(j[0])
                    try:
                        bat2_avg=float(j[2])
                    except:
                        bat2_avg=0
                    try:
                        bat2_sr=float(j[3])
                    except:
                        bat2_sr=0
                    break
            except:
                bat2_c=1
                bat2_avg=0
                bat2_sr=0
        fpp.write(str(bowl_c)+","+str(bowl_eco)+","+str(bowl_avg)+","+str(bat1_c)+","+str(bat1_avg)+","+str(bat1_sr)+","+str(bat2_c)+","+str(bat2_avg)+","+str(bat2_sr)+","+str(runs)+","+str(wickets)+"\n")
###############################################################################
    for i in overbyover2:
        if(len(i)<2):
            break
        boname=i[0][4]
        bowl_c, bowl_eco, bowl_avg,bat1_c,bat1_avg,bat1_sr,bat2_c,bat2_avg,bat2_sr,runs,wickets=0,0,0,0,0,0,0,0,0,0,0
        for j in i:
            if(len(j)>9):
                wickets+=1
            runs+=int(j[6])
        for j in bowl_cli_inp:
            try:
                if(j[1]==boname):
                    bowl_c=int(j[0])
                    try:
                        bowl_eco=float(j[2])
                    except:
                        bowl_eco=0
                    try:
                        bowl_avg=float(j[3])
                    except:
                        bowl_avg=0
                    break
            except:
                bowl_c=1
                bowl_eco=0
                bowl_avg=0
        lastname=i[-1][3]
        lastoppbat=i[-1][5]
        #print(lastname,lastoppbat)
        for j in bat_cli_inp:
            try:
                if(j[1]==lastname):
                    bat1_c=int(j[0])
                    try:
                        bat1_avg=float(j[2])
                    except:
                        bat1_avg=0
                    try:
                        bat1_sr=float(j[3])
                    except:
                        bat1_sr=0
                    break
            except:
                bat1_c=1
                bat1_avg=0
                bat1_sr=0
        for j in bat_cli_inp:
            try:
                if(j[1]==lastoppbat):
                    bat2_c=int(j[0])
                    try:
                        bat2_avg=float(j[2])
                    except:
                        bat2_avg=0
                    try:
                        bat2_sr=float(j[3])
                    except:
                        bat2_sr=0
                    break
            except:
                bat2_c=1
                bat2_avg=0
                bat2_sr=0
        fpp.write(str(bowl_c)+","+str(bowl_eco)+","+str(bowl_avg)+","+str(bat1_c)+","+str(bat1_avg)+","+str(bat1_sr)+","+str(bat2_c)+","+str(bat2_avg)+","+str(bat2_sr)+","+str(runs)+","+str(wickets)+"\n")
fpp.close()
print("complete")