import numpy as np
import matplotlib.pyplot as plt

obj=[0.4,0.5,0.6,0.7]
data_256=[2.8193, 4.2433, 4.5427, 7.1953]
data_512=[3.2595, 4.0729, 4.9997, 6.4167]
data_1024=[3.0692, 3.7098, 5.8871, 6.6023]
data_2048=[3.5300, 4.2222, 5.2345, 6.8408]

plt.plot(obj, data_256,linewidth=1,marker='o',markersize=10,color='green',label='chi phi lookup turng binh voi 256 nodes')
plt.plot(obj, data_512,linewidth=1,marker='o',markersize=10,color='red',label='chi phi lookup trung binh voi 512 nodes')
plt.plot(obj, data_1024,linewidth=1,marker='o',markersize=10,color='blue',label='chi phi lookup trung binh voi 1024 nodes')
plt.plot(obj, data_2048,linewidth=1,marker='o',markersize=10,color='black',label='chi phi trung binh voi 2048 nodes')
plt.axis([0.2, 0.8, 0, 11])
plt.xlabel(" %node fault in chord ring")
plt.ylabel("chi phi trung binh trong qua trinh lookup")
plt.legend()
plt.show()
