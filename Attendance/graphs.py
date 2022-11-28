from django.db.models import Count
from django.core.mail import send_mail
import datetime
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd
import numpy as np


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, formate='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x,y,a,b):
    plt.switch_backend("AGG")
    plt.title("Per day subject attended",fontsize = 16)    
    plt.plot(x,y,label="week1")
    plt.plot(a,b,label="week2")
    plt.xlabel("Week day ",fontsize = 14)
    plt.ylabel("Lecture attended per week",fontsize = 14)
    plt.legend()    
    graph = get_graph()
    return graph
    
def get_pie(x):
    plt.switch_backend("AGG")
    plt.title("Week wise present absent",fontsize = 20)
    colors = ["green","red"]
    labels="Present","Absent"
    plt.pie([x,15-x],explode=(0, 0.1), labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90,textprops={'fontsize': 16},colors=colors)
    graph = get_graph()
    return graph

def get_bar(x,y,a,b1):
    b = []
    for (i,k) in zip(a,b1):
        for j in x:
            if(j == i):
                b.append(k)
                break
    
    plt.figure(figsize=(100,100))
    plt.switch_backend("AGG")  
    
    X_axis1 = np.arange(len(x))
    plot = plt.bar(X_axis1 - 0.2, y, 0.4, label = 'Week1')
    plt.xticks(X_axis1, x, rotation=45)    
    
    X_axis2 = np.arange(len(a))
    plt.bar(X_axis2 + 0.2, b, 0.4, label = 'Week2')
        
    plt.title("Attendance of last week in %",fontsize = 16)
    plt.xlabel("Subjects",fontsize = 14)
    plt.ylabel("Percentage(%) of attendance",fontsize = 14)
    plt.legend()
    plt.tight_layout()
    graph = get_graph()
    return graph