import random
from unicodedata import name
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
count =[]
diceresult = []
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)
    count.append(i)
import statistics as st
mean=st.mean(diceresult)
median=st.median(diceresult)
mode=st.mode(diceresult)
sd=st.stdev(diceresult)
print(mean)
print(median)
print(mode)
sd1start,sd1end=mean-sd,mean+sd
sd2start,sd2end=mean-(2*sd),mean+(2*sd)
sd3start,sd3end=mean-(3*sd),mean+(3*sd)
fig=ff.create_distplot([diceresult],["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.17],mode="lines",name="sd1"))
fig.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.17],mode="lines",name="sd1"))
fig.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.17],mode="lines",name="sd2"))
fig.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.17],mode="lines",name="sd2"))
fig.show()
listsd1=[result for result in diceresult if result > sd1start and result < sd1end]
print("{}% of data lies sd1".format(len(listsd1)*100.0/len(diceresult)))
listsd2=[result for result in diceresult if result > sd2start and result < sd2end]
print("{}% of data lies sd2".format(len(listsd2)*100.0/len(diceresult)))
listsd3=[result for result in diceresult if result > sd3start and result < sd3end]
print("{}% of data lies sd3".format(len(listsd3)*100.0/len(diceresult)))
