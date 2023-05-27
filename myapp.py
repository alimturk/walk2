import numpy as np
import pandas as pd
import streamlit as st

# Sayfa Ayarları
st.set_page_config(
    page_title="Walk Counter",
    page_icon="https://r.resimlink.com/CTZ_A.jpg",
    
)

# Başlık Ekleme
st.title("Walking Project")

# Markdown Oluşturma
st.markdown("Bu projede bize gönderdiğiniz g kuvveti değerleri ile sizin adım sayınızı hesaplayacağız.")
st.markdown("https://r.resimlink.com/va1lCL7TI_.gif)")




uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  dataframe = pd.read_csv(uploaded_file)
  st.write(dataframe)

  walklist=[]
  walklist_counter=0
  walk_list_mean=0
  walk_list_sum=0
  for i in range(41759):
    if(walklist_counter==130):
      walk_list_mean=walk_list_sum/130
      walklist.append(walk_list_mean)
      walk_list_sum=0
      walklist_counter=0
    walk_list_sum=walk_list_sum+(dataframe.iloc[i,1])
    walklist_counter=walklist_counter+1
  range_walk=len(walklist)
  counter_plus=0
  counter_sum=0
  for i in range(range_walk):
    if counter_plus==0:
      if walklist[i]>-0.56:
       counter_plus=1
    if counter_plus==1:
     if walklist[i]<-0.56:
       counter_sum=counter_sum+1
       counter_plus=0
  st.info("Toplam adım sayınız aşağıda verilmiştir.")
  st.write(counter_sum)