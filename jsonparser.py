import json
import random
import numpy as np
import tensorflow as tf
from tensorflow import keras

def returnColorNumer(color):
    if(color=="Negru"):
        return 1
    if(color=="Maro"):
        return 2
    if(color=="Galben"):
        return 3
    if(color=="Gri"):
        return 4
    if(color=="Alb"):
        return 5
    if(color=="Rosu"):
        return 6 
    if(color=="Verde"):
        return 7   

def returnNumeProd(produs):
    if(produs=="Jacheta"):
        return 1
    if(produs=="Rochie"):
        return 2
    if(produs=="Camasa"):
        return 3
    if(produs=="Tricou"):
        return 4
    if(produs=="Vesta"):
        return 5
    if(produs=="Pantaloni"):
        return 6
    if(produs=="Pantofi"):
        return 7

def main():
    random.seed()
    with open('data.json') as f:
        data=f.read()
    dicts=json.loads(data)
    dicts=list(dicts)
    matrice=[]
    count_total=0
    for dict in dicts:
       for key in dict:
            if(str(key)=="count"):
                count_total+=int(dict[key])
    count=0
    for dict in dicts:
        produs=[]
        # for key in dict:
        if(dict['name']):
            nume=returnNumeProd(str(dict['name']).split()[0])
            color=returnColorNumer(str(dict['name']).split()[1])
        if(dict['count']):
            count=int(dict['count'])
        size=random.randint(1,5)
        pret=random.uniform(0.0,5000.0)
        eco=random.randint(1,10)
        produs.append(nume)
        produs.append(color)
        produs.append(size)
        produs.append(eco)
        produs.append(pret)
        print(produs)
        # for item in produs:
        #     if(type(item)!=str):
        #         item*=(count/count_total)
        # matrice.append(produs)
        for i in range(len(produs)):
            if(type(produs[i])!=str):
                produs[i]*=(count/count_total)
        matrice.append(produs)
    print("lungime:")
    print(len(produs))                
    mat=np.asarray(matrice)
    matrice=np.asmatrix(mat)
    print(matrice)
    print(matrice.shape[0])
    summ=0
    #print(matrice[0][0][0])
    for j in range(matrice.shape[0]):
        summ += matrice[j][0]
    print(summ)
    print(summ/matrice.shape[0])
    site_arr = summ
    site_arr = site_arr * 0.6
    bought1 = np.array([[2, 7, 4, 8, 4398.90]])
    bought2 = np.array([[4, 2, 3, 5, 2500]])
    lst = [2, 4]
    list1 = [1, 2, 3, 4, 5, 6, 7]
    
    #arr_fin = (bought1 + bought2) * 0.4 + site_arr
    arr_fin = site_arr * 10 / 6;
    print("array:")
    print(arr_fin)
    random.seed()
    produs = random.choice(list(filter(lambda ele: ele not in lst, list1)))
    f = open("demofile.json", "w")
    # f.write("Clothing prediction:\n")
    print("clothing prediction:")
    print(produs)
    dc = {}
    if(produs==1):
        dc['nume'] = 'Jacheta'
        # f.write("Jacheta\n")
    if(produs==2):
        dc['nume'] = 'Rochie'
        # f.write("Rochie\n")
    if(produs==3):
        dc['nume'] = 'Camasa'
        # f.write("Camasa\n")
    if(produs==4):
        dc['nume'] = 'Tricou'
        # f.write("Tricou\n")
    if(produs==5):
        dc['nume'] = 'Vesta'
        # f.write("Vesta\n")
    if(produs==6):
        dc['nume'] = 'Pantaloni'
        # f.write("Pantaloni\n")
    if(produs==7):
        dc['nume'] = 'Pantofi'
        # f.write("Pantofi\n")
    model = keras.models.load_model("size.model")
    prediction = model.predict(arr_fin)
    print("size prediction:")
    print(np.argmax(prediction))
    # f.write("Size prediction:\n")
    # f.write(str(np.argmax(prediction))+'\n')
    dc['marime'] = str(np.argmax(prediction))

    model = keras.models.load_model("colour.model")
    color = model.predict(arr_fin)
    color = np.argmax(color)
    print("colour prediction:")
    # f.write("Colour prediction:\n")
    if(color==1):
        dc['culoare'] = 'Negru'
        # f.write("Neagra\n")
    if(color==2):
        dc['culoare'] = 'Maro'
        # f.write("Maro\n")
    if(color==3):
        dc['culoare'] = 'Galben'
        # f.write("Galben\n")
    if(color==4):
        dc['culoare'] = 'Gri'
        # f.write("Gri\n")
    if(color==5):
        dc['culoare'] = 'Alb' 
        # f.write("Alba\n")
    if(color==6):
        dc['culoare'] = 'Rosu'
        # f.write("Rosu\n")
    if(color==7):
        dc['culoare'] = 'Verde'
        # f.write("Verde\n")  
    #print(np.argmax(color))

    model = keras.models.load_model("price.model")
    prediction = model.predict(arr_fin)
    print("price range prediction:")
    # f.write("Price range prediction:\n")
    fin_price = np.argmax(prediction) * 1000
    print(str(fin_price - 1000) + " -- " + str(fin_price))
    dc['pret'] = str(fin_price - 1000) + " -- " + str(fin_price)
    print(dc)
    js = json.dumps(dc)
    f.write(js)
    # f.write(str(fin_price - 1000) + " -- " + str(fin_price) + '\n')
    f.close()



if __name__ =="__main__":
    main()
