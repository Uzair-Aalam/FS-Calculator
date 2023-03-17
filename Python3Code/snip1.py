from dictData import *
import dictData

#=========================================================================
Dict_names={'C110DEG':C110DEG,'C120DEG':C120DEG,'C130DEG':C130DEG,\
'C140DEG':C140DEG,'C150DEG':C150DEG,'C160DEG':C160DEG,'C170DEG':C170DEG,\
'C180DEG':C180DEG,'C190DEG':C190DEG,\
'C210DEG':C210DEG,'C220DEG':C220DEG,'C230DEG':C230DEG,'C240DEG':C240DEG,\
'C250DEG':C250DEG,'C260DEG':C260DEG,'C270DEG':C270DEG,'C280DEG':C280DEG,\
'C290DEG':C290DEG,\
'C320DEG':C320DEG,'C330DEG':C330DEG,'C340DEG':C340DEG,\
'C350DEG':C350DEG,'C360DEG':C360DEG,'C370DEG':C370DEG,'C380DEG':C380DEG,\
'C390DEG':C390DEG,\
'C440DEG':C440DEG,'C450DEG':C450DEG,'C460DEG':C460DEG,'C470DEG':C470DEG,\
'C480DEG':C480DEG,'C490DEG':C490DEG,\
'C510DEG':C510DEG,'C520DEG':C520DEG,'C530DEG':C530DEG,'C540DEG':C540DEG,\
'C550DEG':C550DEG,'C560DEG':C560DEG,'C570DEG':C570DEG,'C580DEG':C580DEG}

Angles=[10,20,30,40,50,60,70,80,90]
charts=['C1','C2','C3','C4','C5']

#=============================Functions Definitions=======================
def Find(x,List_name):
    print('\n\n\n\nFunction Find(x,List_name) is called')
    Angle_Dict=List_name
    data=[]
    for i in range(len(Angle_Dict)):
        data.append(Angle_Dict[i][0])
    
    print('data in List is ',data)
    for index in range(1,len(data)):
        if(x<float(data[index])):
            break
    #x is between data[index] and data[index-1]
    if(index==1):
        tup=(data[index],data[index])
    else:
        tup=(data[index-1],data[index])
    return tup

    
def Find_XY(x,List_name):
    print('\n\n\n\nFunction Find_XY(x,List_name) is called')
    tup=Find(x,List_name)
    index=Find_index(x,tup)        
    
    
    data=[]
    data2=List_name
    x1=x2=y1=y2=0.0
    
    for terms in data2:
        if (tup[0] in terms):
            x1=terms[1]
            y1=terms[2]
        if(tup[1] in terms):
            x2=terms[1]
            y2=terms[2]
    print((x1,y1))
    print((x2,y2))
    
    step_size=(x2-x1)/100.0
    x=x1+step_size*index
    
    step_size=(y2-y1)/100.0
    y=y1+step_size*index    
    print('final answer is ',x,y)
    return (x,y)
    
def Find_index(x,tup):
    print('\n\n\n\nFunction Find_index(x,tup) is called')
    print("tuple received ",tup)
    print('x received',x)
    index=0
    initial=float(tup[0])
    final=float(tup[1])
    step_size=(final-initial)/100.0
    print('step size',step_size)
    for i in range(0,100):
        term=initial+i*step_size
        if(abs(x-term)<0.0000001):
            index=i
            break
    print('index is ',index)
    return index
    
    
def Point_Between_theta1_and_2(x,Angle,chart_number):
    print('\n\n\n\nFunction Point_Between_theta1_and_2(x,Angle,chart_number) is called')
    flag=0
    for index in range(0,len(Angles)):
        if (Angle<float(Angles[index])):
            flag=1
            break
    if(index==0):
        tup=(Angles[0],Angles[0])
    else:
        if(index==len(Angles)-1 and flag==0):
            tup=(Angles[len(Angles)-1],Angles[len(Angles)-1])
        else:
            tup=(Angles[index-1],Angles[index])
    
    index=Find_index(Angle,tup)
    dict_name=Make_Dict_Name(chart_number,tup[0])
    List=Dict_names[dict_name]
    tup1=Find_XY(x,List)
    print('tup1 received in caller',tup1)
    print('tup1 = ',tup1,' at ',tup[0],' degree')
    
    dict_name=Make_Dict_Name(chart_number,tup[1])
    List=Dict_names[dict_name]
    tup2=Find_XY(x,List)
    print('tup2 received in caller',tup2)
    
    print('tup2 = ',tup2,' at ',tup[1],' degree')
    
    step_size=(tup2[0]-tup1[0])/100.0
    x1=tup1[0]+step_size*index
    
    step_size=(tup2[1]-tup1[1])/100.0
    y1=tup1[1]+step_size*index
    print('the value for x and y for ',x,' at ',Angle,', from chart=',chart_number\
,'is =',(x1,y1))
    return (x1,y1)
    
def Make_Dict_Name(chart_number,angle):
    print('\n\n\n\nFunction Make_Dict_Name(chart_number,Angle) is called')
    print('Chart number=',chart_number,' angle=',angle)
    if chart_number==5 and angle>=80:
        Angle_Dict='C580DEG'
    else:
        Angle_Dict=charts[chart_number-1]+str(Angles[int(angle/10)-1])+'DEG'
    print("Dictionary Name : "+Angle_Dict)
    return Angle_Dict
#=================================================================================    

 