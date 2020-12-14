import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
data=df["temp"].tolist()
#population_mean = statistics.mean(data)
#sd=statistics.stdev(data)

#print("mean is:-",population_mean)
#print("standard deviation:-",sd)
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean=statistics.mean(mean_list)
    print("mean of sampling disterbution",mean)

setup()

population_mean = statistics.mean(data)
print("mean is:-",population_mean)

def sd():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)

    sd=statistics.stdev(mean_list)
    print("standard deviation of sampling disterbution",sd)

sd()