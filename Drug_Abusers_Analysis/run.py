
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
import matplotlib.pyplot as plt
import pickle

#from model_methods import predict
# classes = {0:'setosa',1:'versicolor',2:'virginica'}
# class_labels = list(classes.values())
st.title("Drug Abusers Analysis")
st.markdown('**Objective** : Given details about the recently used period of drug.')
#st.markdown('The model can predict if it belongs to the following three Categories : **setosa, versicolor, virginica** ')
def predict_class(arg):
    #data = list(map(float,[sepal_length,sepal_width,petal_length, petal_width,gender]))
    # data = list(map(float,[age,gender,education,nscore,escore,oscore,ascore,cscore,impulsive,ss]))
    if arg[0]>=18 or arg[0]<24:
        age=-0.95197
    elif arg[0]>=25 or arg[0]<34:
        age=-0.07854
    elif arg[0]>=35 or arg[0]<44:
        age=-0.49788
    elif arg[0]>=45 or arg[0]<54:
        age=1.09449
    elif arg[0]>=55 or arg[0]<64:
        age=1.82213
    else:
        age=2.59171
    
    if arg[1]=="female":
        gender=0.48246
    else:
        gender=-0.48246

    if arg[2]=="Left school before 16 years":
        education=-2.43591
    elif arg[2]=="Left school at 16 years":
        education=-1.73790
    elif arg[2]=="Left school at 17 years":
        education=-1.43719
    elif arg[2]=="Left school at 18 years":
        education=-1.22751
    elif arg[2]=="Some College or university but no Certificate or degree":
        education=-0.61113
    elif arg[2]=="Professional Certificate/diploma":
        education=-0.05921
    elif arg[2]=="University Degree":
        education=0.045468
    elif arg[2]=="Masters Degree":
        education=1.16365
    else:
        education=1.98437


    if arg[3]==1:
        nscore=-0.92104
    elif arg[3]==2:
        nscore=-0.67825
    elif arg[3]==3:
        nscore=-0.46725
    elif arg[3]==4:
        nscore=-0.04257
    else:
        nscore=1.02119  
    
    if arg[4]==1:
        escore=0.47617
    elif arg[4]==2:
        escore=0.63779
    elif arg[4]==3:
        escore=0.00332
    elif arg[4]==4:
        escore=-0.15487
    else:
        escore=-0.43999     

    if arg[5]==1:
        oscore=1.65653
    elif arg[5]==2:
        oscore=0.58331
    elif arg[5]==3:
        oscore=-1.11902
    elif arg[5]==4:
        oscore=-0.17779
    else:
        oscore=0.14143 

    if arg[6]==1:
        ascore=1.11406
    elif arg[6]==2:
        ascore=0.76096
    elif arg[6]==3:
        ascore=0.59042
    elif arg[6]==4:
        ascore=0.28783
    else:
        ascore=-1.772 

    if arg[7]==1:
        cscore=-0.00665
    elif arg[7]==2:
        cscore=0.25953
    elif arg[7]==3:
        cscore=0.41594
    elif arg[7]==4:
        cscore=-0.00665
    else:
        cscore=-1.0145

    if arg[8]==1:
        impulsive=-0.21712
    elif arg[8]==2:
        impulsive=-0.71126
    elif arg[8]==3:
        impulsive=0.7583
    elif arg[8]==4:
        impulsive=1.29221
    else:
        impulsive=0.52975

    if arg[9]==1:
        ss=-0.21712
    elif arg[9]==2:
        ss=-0.71126
    elif arg[9]==3:
        ss=0.7583
    elif arg[9]==4:
        ss=1.29221
    else:
        ss=0.52975

    if arg[10]=='Alcohol':
        # model='Alcohol'
        file = open("Alcohol",'rb')
        model = pickle.load(file)
    elif arg[10]=='Amphet':
        # model='Amphet'
        file = open("Amphet",'rb')
        model = pickle.load(file)
    elif arg[10]=='Amyl':
       # model='Amyl'
        file = open("Amyl",'rb')
        model = pickle.load(file)
    elif arg[10]=='Benzos':
       # model='Benzos'
        file = open("Benzos",'rb')
        model = pickle.load(file)
    elif arg[10]=='Caff':
       # model='Caff'
        file = open("Caff",'rb')
        model = pickle.load(file)
    elif arg[10]=='Cannabis':
       # model='Cannabis'
        file = open("Cannabis",'rb')
        model = pickle.load(file)
    elif arg[10]=='Choc':
        #model='Choc'
        file = open("Choc",'rb')
        model = pickle.load(file)
    elif arg[10]=='Coke':
        #model='Coke'
        file = open("Coke",'rb')
        model = pickle.load(file)
    elif arg[10]=='Crack':
        #model='Crack'
        file = open("Crack",'rb')
        model = pickle.load(file)
    elif arg[10]=='Ecstasy':
        #model='Ecstasy'
        file = open("Ecstasy",'rb')
        model = pickle.load(file)
    elif arg[10]=='Heroin':
        #model='Heroin'
        file = open("Heroin",'rb')
        model = pickle.load(file)
    elif arg[10]=='Ketamine':
        #model='Ketamine'
        file = open("Ketamine",'rb')
        model = pickle.load(file)
    elif arg[10]=='Legalh':
        #model='Legalh'
        file = open("Legalh",'rb')
        model = pickle.load(file)
    elif arg[10]=='LSD':
        #model='LSD'
        file = open("LSD",'rb')
        model = pickle.load(file)
    elif arg[10]=='Meth':
        #model='Meth'
        file = open("Meth",'rb')
        model = pickle.load(file)
    elif arg[10]=='Mushrooms':
        #model='Mushrooms'
        file = open("Mushrooms",'rb')
        model = pickle.load(file)
    elif arg[10]=='Nicotine':
        #model='Nicotine'
        file = open("Nicotine",'rb')
        model = pickle.load(file)
    elif arg[10]=='Semer':
        #model='Semer'
        file = open("Semer",'rb')
        model = pickle.load(file)
    else:
        # model='VSA'
        file = open("VSA",'rb')
        model = pickle.load(file)
    # st.write('You selected:', (age,gender,education,nscore,cscore,escore,oscore,ascore,impulsive,ss,model))
    arr=[age,gender,education,nscore,cscore,escore,oscore,ascore,impulsive,ss]
    a =[[arr[i] for i in range(len(arr))]]
    xtest = pd.DataFrame(a)
    predict=model.predict(xtest)
    # st.write(pred[0])
    if(predict[0]==0):
        st.write("Never Used")
    elif(predict[0]==1):
        st.write("Used in last year")
    elif(predict[0]==2):
        st.write("Used in last 6 months")
    elif(predict[0]==3):
        st.write("Used within last 2 months")
    elif(predict[0]==4):
        st.write("Used in last month")
    elif(predict[0]==5):
        st.write("Used in last week")
    else:
        st.write("Used in last day")



    # result, probs = predict(data)
    # st.write("The predicted class is ",result)
    # probs = [np.round(x,6) for x in probs]
    # ax = sns.barplot(probs ,class_labels, palette="winter", orient='h')
    # ax.set_yticklabels(class_labels,rotation=0)
    # plt.title("Probabilities of the Data belonging to each class")
    # for index, value in enumerate(probs):
    #     plt.text(value, index,str(value))
    # st.pyplot()


st.sidebar.markdown("**Please enter the details of the persons**")
# sepal_length = st.text_input('Enter sepal_length', '')
# sepal_width = st.text_input('Enter sepal_width', '')
# petal_length = st.text_input('Enter petal_length', '')
# petal_width = st.text_input('Enter petal_width', '')

age = st.sidebar.number_input('Age',min_value=18,max_value=100)
gender = st.sidebar.selectbox('Gender:',('Female', 'Male'))

education = st.sidebar.selectbox('Education:',('Left school before 16 years',
 'Left school at 16 years','Left school at 17 years',
 'Left school at 18 years','Some College or university but no Certificate or degree',
'Professional Certificate/diploma','University Degree',
'Masters Degree','Doctorate Degree'))
nscore = st.sidebar.slider('Nscore:',1,5)
escore = st.sidebar.slider('Escore:',1,5)
oscore = st.sidebar.slider('Oscore:',1,5)
ascore = st.sidebar.slider('Ascore:',1,5)
cscore = st.sidebar.slider('Cscore:',1,5)
impulsive = st.sidebar.slider('Impulsive:',1,5)
ss = st.sidebar.slider('SS:',1,5)
model=st.selectbox('Select Model',('Alcohol','Amphet','Amyl','Benzos','Caff','Cannabis',
'Choc','Coke','Crack','Ecstasy','Heroin','Ketamine','Legalh','LSD','Meth','Mushrooms',
'Nicotine','Semer','VSA'))

#st.write('You selected:', gender)
# st.write('You selected:', ())
if st.button("PREDICT"):
    predict_class([age,gender,education,nscore,cscore,escore,oscore,ascore,impulsive,ss,model])