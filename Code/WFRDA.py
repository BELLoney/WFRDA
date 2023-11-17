## A weighted fuzzy rough density-based anomaly (WFRDA) algorithm
## Please refer to the following papers:
## Anomaly detection based on weighted fuzzy-rough density, Information Sciences, 2023
## Uploaded by Yuan Zhong on July 24, 2021. E-mail:yuanzhong2799@foxmail.com.
import numpy as np
from scipy.io import loadmat
from sklearn.preprocessing import MinMaxScaler

def WFRDA(data,sigma):
    ##input:
    # Data is data matrix without decisions, where rows for samples and columns for attributes.
    # Numeric attribute data is normalized to [0, 1].
    # sigma is an adjustable parameter.
    ## output
    # Weighted fuzzy rough density-based anomaly score (AS).

    n,m=data.shape
    delta=np.zeros(m) #Initialize the radius
    for k in range(m):
        if all(data[:,k]<=1+1e-6):
            delta[k]=sigma #Find the radius of the numeric feature

    E=np.zeros(m) #complement entropy
    FADens=np.zeros((n,m))
    for k in range(m):
        x=data[:,k]
        rm=np.zeros((n,n))
        for i in range(n):
            for j in range(i+1):
                rm[i,j]=wfrda_kersim(x[i],x[j],delta[k]) #Compute relation matrice
                rm[j,i]=rm[i,j]
        rm_temp=rm
        E[k]=-np.sum((1/n)*np.log2(np.sum(rm,1)/n)) #Compute fuzzy entropy
        FADens[:,k]=np.sum(rm_temp,1)/n
    # print(FADens)

    W=E/np.sum(E)
    # print(W)
    AS=np.zeros(n)
    for i in range(n):
        AS[i]=np.sum((1-FADens[i,:])*W)
    return AS

def wfrda_kersim(a,x,e):
    if (e==0):
        if (a==x):
            kersim=1
        else:
            kersim=0
    else:
        kersim=max(min((x-a+e)/e,(a-x+e)/e),0)
    return kersim

if __name__ == "__main__":
    load_data = loadmat('Example_WFRDA.mat')
    trandata = load_data['Example']
    scaler = MinMaxScaler()
    trandata[:, 1:] = scaler.fit_transform(trandata[:, 1:])

    sigma = 0.5
    out_scores = WFRDA(trandata, sigma)
    print(out_scores)
