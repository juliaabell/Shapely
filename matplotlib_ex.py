#matlab part


import matplotlib.pyplot as plt
%matplotlib inline

x=[0,1,0,1]
y=[0,0,1,1]

##scatter plot
plt.scatter(x,y, s=30, c='red')
plt.show()

##line segment
plt.plot(x,y)
plt.show()

##subplot
plt.figure()

plt.subplot(1,2,1)
plt.scatter(x,y,s=30,c='red')

plt.subplot(1,2,2)
plt.plot(x,y);

plt.show
