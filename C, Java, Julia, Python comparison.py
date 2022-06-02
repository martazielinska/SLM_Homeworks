import pandas as pd
from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

data=StringIO("""problem,language,time,size
n-body,C,2.13,1633
mandelbrot,C,1.3,1135
spectral norm,C,0.41,1197
fannkuch-redux,C,7.58,910
fasta,C,0.78,1463
k-nucleotide,C,3.96,1506
binary-trees,C,1.58,809
reverse-complement,C,0.41,1965
pidigits,C,0.56,1090
regex-redux,C,0.8,1397
n-body,Java,6.77,1489
mandelbrot,Java,4.1,796
spectral norm,Java,1.55,756
fannkuch-redux,Java,10.48,1282
fasta,Java,1.2,2543
k-nucleotide,Java,4.83,1812
binary-trees,Java,2.51,835
reverse-complement,Java,1.57,2183
pidigits,Java,0.79,764
regex-redux,Java,5.34,929
n-body,Python,541.34,1196
mandelbrot,Python,177.35,688
spectral norm,Python,112.97,407
fannkuch-redux,Python,341.45,950
fasta,Python,36.9,1947
k-nucleotide,Python,46.31,1967
binary-trees,Python,44.7,660
reverse-complement,Python,6.62,814
pidigits,Python,1.16,567
regex-redux,Python,1.34,1403
n-body,Julia,4.21,1111
mandelbrot,Julia,1.42,619
spectral norm,Julia,1.11,429
fannkuch-redux,Julia,7.83,1067
fasta,Julia,1.13,1082
k-nucleotide,Julia,4.94,951
binary-trees,Julia,7.28,634
reverse-complement,Julia,1.44,522
pidigits,Julia,0.97,506
regex-redux,Julia,1.74,759""")

df = pd.read_csv(data, header=0)
df1=df[df['language']=='C']
dfju=df[df['language']=='Julia']
dfp=df[df['language']=='Python']
dfja=df[df['language']=='Java']

dfp=dfp.rename(columns={"time": "Python_time", "size": "Python_size"})
dfp=dfp.drop(columns='language')

dfju=dfju.rename(columns={"time": "Julia_time", "size": "Julia_size"})
dfju=dfju.drop(columns='language')
print(dfju)
dfja=dfja.rename(columns={"time": "Java_time", "size": "Java_size"})
dfja=dfja.drop(columns='language')

df1=df1.rename(columns={"time": "C_time", "size": "C_size"})
df1=df1.drop(columns='language')

dfnew =pd.merge(df1, dfp, on="problem")
dfnew=pd.merge(dfnew, dfju, on = "problem")
dfnew=pd.merge(dfnew, dfja, on = "problem")

dfnew['Python_time']=dfnew['Python_time']/dfnew['C_time']
dfnew['Python_size']=dfnew['Python_size']/dfnew['C_size']
dfnew['Julia_time']=dfnew['Julia_time']/dfnew['C_time']
dfnew['Julia_size']=dfnew['Julia_size']/dfnew['C_size']
dfnew['Java_time']=dfnew['Java_time']/dfnew['C_time']
dfnew['Java_size']=dfnew['Java_size']/dfnew['C_size']
dfnew['C_time']=1
dfnew['C_size']=1

print(dfnew)



plt.subplot(1, 2, 1)
plt.scatter(dfnew['problem'],dfnew['Python_size'],color='blue', marker= '*', s=200,label='Python')
plt.scatter(dfnew['problem'],dfnew['Julia_size'],color= 'red', marker='.',  s=200,label='Julia')
plt.scatter(dfnew['problem'],dfnew['Java_size'],color= 'green', marker='v', s=200,label='Java')
plt.plot(dfnew['problem'],dfnew['C_size'],color= 'gold', label='C')
plt.xticks(rotation = 45)
plt.ylabel('Size')
plt.legend(loc='best')

plt.subplot(1, 2, 2)
plt.scatter(dfnew['problem'],dfnew['Python_time'],color='blue', marker= '*', s=200,label='Python')
plt.scatter(dfnew['problem'],dfnew['Julia_time'],color= 'red', marker='.', s=200,label='Julia')
plt.scatter(dfnew['problem'],dfnew['Java_time'],color= 'green', marker='v', s=200,label='Java')
plt.plot(dfnew['problem'],dfnew['C_time'],color= 'gold', label='C')
plt.yscale('symlog')
plt.xticks(rotation = 45)
plt.ylabel('Time')
plt.legend(loc='best')
plt.show()





