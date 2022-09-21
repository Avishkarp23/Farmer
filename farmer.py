from fuzzywuzzy import fuzz
import pandas as pd

class farmer:

   def __init__(self,name,father,village):
     self.name=name
     self.father=father
     self.village=village
     self.m_name=""
     self.m_father=""

   def display(self):

    a=[self.name,self.father,self.village]
    return(a)



   def display2(self):
    b=[self.name,self.father,self.village,self.m_name,self.m_father]
    return (b)

df=pd.read_csv("farmer.csv")
b=df.to_numpy()
#creating objects
list1=[]
for i in b:
    a=farmer(i[0],i[1],i[2])
    list1.append(a)



#check duplicates
for i in range(len(list1)-1):

   if(fuzz.WRatio(list1[i].name,list1[i+1].name)>84):
      list1[i+1].m_name=list1[i].name
   if (fuzz.WRatio(list1[i].father, list1[i + 1].father) > 84):
    list1[i + 1].m_father = list1[i].father

#print results
Inpl=[]
Outl=[]
print("Input file:")
for i in list1:
  inp=i.display()
  Inpl.append(inp)
inp_df=pd.DataFrame(Inpl)
print(inp_df)

print("output file:")
for i in list1:
 out=i.display2()
 Outl.append(out)
out_df=pd.DataFrame(Outl)
print(out_df)







