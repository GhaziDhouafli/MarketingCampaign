
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading our model
model= pickle.load(open('C:/Users/ASUS/Desktop/project/model.sav','rb'))

#sidebar for navigation
with st.sidebar:
    selected=option_menu('Check Customer is group',
                         ['Click Here'],
                         icons=['person'],
                         default_index=0)

# Parkinson's Prediction Page
if (selected == "Click Here"):
    
    # page title
    st.title("Fill in the customer is data")
    
    col1, col2, col3, col4 = st.columns(4)  
    
    with col1:
        text1 = st.text_input('QUANTITYORDERED')
        
    with col1:
        text2 = st.text_input('PRICEEACH')
        
    with col1:
        text3 = st.text_input('ORDERLINENUMBER')
        
    with col2:
        text4 = st.text_input('SALES')
        
    with col2:
        text5 = st.text_input('MONTH_ID')
        
    with col2:
        text6 = st.text_input('YEAR_ID')
        
    with col3:
        text7 = st.text_input('MSRP')
        
    with col3:
        text8 = st.text_input('PRODUCTCODE')
        
    with col1:
        country = st.radio(
            "pick the country:",
            ('Australia', 'Austria', 'Belgium',
             'Canada', 'Denmark', 'Finland', 'France', 'Germany', 'Ireland', 'Italy',
             'Japan', 'Norway', 'Philippines', 'Singapore', 'Spain', 'Sweden',
             'Switzerland', 'UK', 'USA'))
        
    with col2:
        product = st.radio(
            "pick the product:",
            ('Classic Cars', 'Motorcycles', 'Planes',
             'Ships', 'Trains', 'Trucks and Buses', 'Vintage Cars'))
         
    with col3:
         size = st.radio(
             "pick the size:",
             ('Large','Medium', 'Small'))    
         
         
    L=[]
    for i in range(9,38):
        L.append(0)
    
    countries={9:'Australia', 10:'Austria', 11:'Belgium',12:'Canada', 13:'Denmark', 14:'Finland', 15:'France', 16:'Germany', 17:'Ireland', 18:'Italy',
               19:'Japan', 20:'Norway', 21:'Philippines', 22:'Singapore', 23:'Spain', 24:'Sweden',25:'Switzerland', 26:'UK', 27:'USA'}

    
    products={28:'Classic Cars', 29:'Motorcycles', 30:'Planes',31:'Ships', 32:'Trains', 33:'Trucks and Buses', 34:'Vintage Cars'}
    
    sizes={35:'Large',36:'Medium', 37:'Small'}
    
    
    ch=country
    for i in countries.values():
        if (i==ch):
            n=(list(countries.keys())[list(countries.values()).index(i)])
            n=n-9
            L[n]=1
            break
    ch=product
    for i in products.values():
        if (i==ch):
            n=(list(products.keys())[list(products.values()).index(i)])
            n=n-9
            L[n]=1 
            break
    ch=size
    for i in sizes.values():
        if (i==ch):
            n=(list(sizes.keys())[list(sizes.values()).index(i)])
            n=n-9
            L[n]=1 
            break
# code for Prediction
    customer_group = ''
    
    # creating a button for Prediction    
    if st.button("Customer is Result"):
        L1=[text1,text2,text3,text4,text5,text6,text7,text8]
        for i in L:
            L1.append(i)
        customer_group_prediction = model.predict([L1]) 
        st.success('The Customer group is',customer_group_prediction)                         
        
        #if (parkinsons_prediction[0] == 1):
          #parkinsons_diagnosis = "The person has Parkinson's disease"
        #else:
          #parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    #st.success(parkinsons_diagnosis)