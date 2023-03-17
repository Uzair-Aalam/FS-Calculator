from numpy import deg2rad
from snip1 import *
from math import tan
from openpyxl import Workbook
from openpyxl.chart import LineChart,Reference
from openpyxl.chart.trendline import Trendline
columnHead={'SCondition':'Slope Condition(over all slope conditions)','SAngle':'Slope Angle',\
'FAngle':'Friction Angle','Height':'Height','Density':'Density','Cohesion':'Cohesion'}

markerSymbol=['triangle','circle','star','diamond','plus','dash',]
markerColor=['FF0000','00FF00','0000FF','FF00FF','00FFFF','FF00FF']

def analyse(dict1,dict2):

    coeffDict={}
    coeffDict1={}
    parameterlist=[]
    filelist=[]
    ChartNo=0
    wb=Workbook()
    sheet=wb.active
    columnNo=65
    sheetcol=chr(columnNo)
    for item in dict2:
        if(dict2[item]!=0):
            coeffDict1[item]=(float(dict2[item])-float(dict1[item]))/100.0
            parameterlist.append(item)
        else:
            coeffDict1[item]=0.0
            
    
    print(coeffDict)
    print(parameterlist)
    
    FS_min=10.0
    FS_max=0.0
    for i in range(1,102):
        sheet[sheetcol+str(i+1)]=float(i-1.0)
        
    if(dict1['SCondition']==0):
        ChartNo=1
    else:
        ChartNo=dict1['SCondition']
    
    for item in parameterlist:
        columnNo+=1
        sheetcol=chr(columnNo)
        
        if(item!='SCondition'):
            for term in coeffDict1:
                if(term!=item):
                    coeffDict[term]=0
                else:
                    coeffDict[term]=coeffDict1[term]
            
            sheet[sheetcol+str(1)]=str(columnHead[item])
            filelist.append(str(item))
            
            for i in range(0,101):
                c=float(dict1['Cohesion'])+i*coeffDict['Cohesion']
                
                d=float(dict1['Density'])+i*coeffDict['Density']
                h=float(dict1['Height'])+i*coeffDict['Height']
                phi=deg2rad(float(dict1['FAngle'])+i*coeffDict['FAngle'])
                DlessRatio=c/(d*h*tan(phi))
                
                print(DlessRatio)
                print((round(DlessRatio,2)))
                DlessRatio=round(DlessRatio,3)
                slopeangle=float(dict1['SAngle'])+i*coeffDict['SAngle']
                    
                ResultTuple=Point_Between_theta1_and_2(DlessRatio,slopeangle,ChartNo)
                
                x_value=round(ResultTuple[0],3)
                FSx=c/(d*h*x_value)
                                
                y_value=round(ResultTuple[1],3)
                FSy=tan(phi)/y_value
                                
                FS=round((FSx+FSy)/2.0,3)
                
                if(FS>FS_max):
                    FS_max=FS
                if(FS<FS_min):
                    FS_min=FS
                
                percentChange=100.0*i/100.0                
                
                sheet[sheetcol+str(i+2)]=FS       
            
        else:
            sheet[sheetcol+str(1)]=str(columnHead[item])
            filelist.append(str(item))            
            for ChartNo in range(1,6):
                c=float(dict1['Cohesion'])              
                d=float(dict1['Density'])
                h=float(dict1['Height'])
                phi=deg2rad(float(dict1['FAngle']))
                DlessRatio=c/(d*h*tan(phi))
                DlessRatio=round(DlessRatio,3)
                
                slopeangle=float(dict1['SAngle'])
                
                ResultTuple=Point_Between_theta1_and_2(DlessRatio,slopeangle,ChartNo)
                
                x_value=round(ResultTuple[0],3)
                FSx=c/(d*h*x_value)
                                
                y_value=round(ResultTuple[1],3)
                FSy=tan(phi)/y_value
                                
                FS=round((FSx+FSy)/2.0,3)
                print(FS)
                
                if(FS>FS_max):
                    FS_max=FS
                if(FS<FS_min):
                    FS_min=FS
                sheet[sheetcol+str(ChartNo+1)]=FS
    
    
    OutputChart=LineChart()
    OutputChart.title='Variation of Factor of Safety'
    OutputChart.x_axis.title='Percent Change in Parameters'
    OutputChart.y_axis.title='Factor of Safety'
    #OutputChart.style=1
    data=Reference(sheet,min_col=2,min_row=1,max_col=columnNo,max_row=102)
    OutputChart.add_data(data,titles_from_data=True)
    OutputChart.x_axis.scaling.min=0    
    OutputChart.x_axis.scaling.max=100
    OutputChart.y_axis.scaling.min=FS_min-0.5
    OutputChart.y_axis.scaling.max=FS_max+0.5
    
    for i in range(0,columnNo-65):
        style=OutputChart.series[i]
        style2=OutputChart.series[i]
        style2.trendline=Trendline(trendlineType='linear')
        print('value of i is'+str(i))
        style.marker.symbol=markerSymbol[i]
        style.marker.graphicalProperties.solidFill=markerColor[i]
        style.marker.graphicalProperties.line.solidFill=markerColor[i]
        style.graphicalProperties.line.noFill=True
    sheet.add_chart(OutputChart,'J2')
    wb.save('AnalysisData.xlsx')
    return filelist
    

    