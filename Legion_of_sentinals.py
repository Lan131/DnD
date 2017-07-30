import numpy as np   
def demo():
    print("Usage:\nlegion_rolls(num,flank=0,bonus=0,caster_lev=8)")
    print("legion_damage(num,bonus=0,caster_lev=9)")
    
def legion_rolls(num,flank=0,bonus=0,caster_lev=8):
    
    print("Number of attacks: "+str(num))
    print("Number flanking: "+str(flank))
    print("Caster Lev: "+str(caster_lev))
    print("Misc bonus: "+str(bonus))
    flank_ct=0
    cast_bonus=np.minimum(np.floor(caster_lev/3),5)
    for i in range(num):
        if(flank_ct<flank):
            A=np.random.randint(1,20)+bonus #roll a d20
            A_=A+2+bonus+cast_bonus 
            print("Attack "+str(i)+" (flank):"+str(A)+"  +  "+str(cast_bonus)+"  +  "+str(bonus)+"+   2=  "+str(A_))
            while(A>=19):
                A=np.random.randint(1,20)
                print("Crit! Roll to confirm "+str(A)+"  +  "+str(2+bonus+cast_bonus)+"=  "+str(A+2+bonus+cast_bonus)+"\n") 
            flank_ct=flank_ct+1
        else:
            A=np.random.randint(1,20)+bonus #roll a d20
            A_=A+bonus+cast_bonus
            print("Attack "+str(i)+":"+str(A)+"  +  "+str(cast_bonus)+"  +  "+str(bonus)+"=  "+str(A_))
            while(A>=19):
                A=np.random.randint(1,20)
                print("Crit! Roll to confirm "+str(A)+"  +  "+str(bonus+cast_bonus)+"=  "+str(A+bonus+cast_bonus)+"\n")
            flank_ct=flank_ct+1
def legion_damage(num,bonus=0,caster_lev=8):
    cast_bonus=np.minimum(np.floor(caster_lev/3),5)
    for i in range(num):
        A=np.random.randint(1,8)
        A_=np.random.randint(1,8)+bonus+cast_bonus
        print("Damage:"+"  "+str(A)+" + "+str(cast_bonus)+" + "+str(bonus)+"="+str(A_))
        
