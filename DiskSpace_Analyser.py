import os
import shutil
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

def get_size(start_path):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    if total_size>0:
        return total_size
    else:
        return os.path.getsize(start_path)

def show_FileName_and_Size(link):
    for files in os.listdir(link):
        path=link+'\\'+files
        size=get_size(path)
        arr.append(size/(1024*1024))

def show_percentage(link):
    total=sum(arr)
    for i in arr:
        perc.append((i/total)*100)

def display_stats(link):
    show_FileName_and_Size(link)
    show_percentage(link)
    labels = os.listdir(link)
    print('Total space occupied by directory(in MB) :',sum(arr))
    df=pd.DataFrame({'Perc(%)':perc,'Size(in MB) ':arr,'File':labels})
    df1=df.sort_values(by=['Perc(%)'],ascending=False)
    print(df1)
    
    for i in range(0,len(arr)-1):
        for j in range (i+1,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                temp1=labels[i]
                labels[i]=labels[j]
                labels[j]=temp1
        
    y_pos = np.arange(len(labels))
    plt.barh(y_pos,arr, align='center', alpha=0.5,color='red')
    plt.yticks(y_pos,labels)
    plt.xlabel('Disk space used in MB')
    plt.ylabel('File Name')
    plt.title('Directory Space Usage Analysis')
    plt.show()

dirpath=input('enter the path of directory')
dirpath.replace(':\\',':\\\\')
if os.path.exists(dirpath) is False:
    print('incorrect directory path')
else:
    path=dirpath
    arr=[]
    perc=[]
    display_stats(path)
    for i in range(1,1000):
        op=input('enter your choice:1-child,2-parent,3-delete a subdirectory within the current directory,4-delete a file within the current directory,5-exit:')
        if op=='1':
            ch=input('enter the folder name:')

            if os.path.exists(path+'\\'+ch) is False:
                print('Incorrect folder name')
            else:
                path=path+'\\'+ch
                arr=[]
                perc=[]
                display_stats(path)
        elif op=='2':
            path=path[:path.rfind('\\')]
            arr=[]
            perc=[]
            display_stats(path)
        elif op=='3':
            subdir_name=input('enter the name of subdirectory to be deleted:')
            if os.path.exists(path+'\\'+subdir_name) is False:
                print('incorrect subdirectory name')
            else:
                shutil.rmtree(path+'\\'+subdir_name)
                arr=[]
                perc=[]
                display_stats(path)
        elif op=='4':
            file_name=input('enter the name of file to be deleted:')
            if os.path.exists(path+'\\'+file_name) is False:
                print('incorrect file name')
            else:
                os.remove(path+'\\'+file_name)
                arr=[]
                perc=[]
                display_stats(path)
        elif op=='5':
            break
        else:
            print('wrong choice entered')
