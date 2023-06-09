# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:21:07 2022

@author: 59195
"""
import numpy as np
import pivot as pt
#変数の初期化
i=0
#1式ごとに入力
print("入力例：3x(1)+4x(2)=5 → 3 4 5")
while True:
    #1行入力し空白区切りで分割しリスト化
    str=input(f"input({i+1}):").split()
    if i == 0:
        #初回ループのみ初期化
        n=len(str)-1
        data=[[]]*n
    #floatに変換
    data[i]=[float(x) for x in str]
    i+=1
    if i>=n :
        break

#計算はnumpyのほうが得意なので拡張性も考えnumpyにする
data=np.array(data)
c=pt.part_pivot(data,n)
x=np.array([1.]*n)
#-------------------
#以降使わないので一応メモリ解放
del str
del data
#計算
for k in range(n):
    for i in range(n):
        if i==k:
            continue
        temp=c[i,k]/c[k,k]
        for j in range(k,n+1):
            c[i,j]-=c[k,j]*temp
    print(c)
    print("")
    
for i in range(n):
    x[i]=c[i,n]/c[i,i]
    #表示
    print(f"x({i+1}):{round(x[i],3)}")
    

            