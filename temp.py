
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from PIL import Image


plt.style.use('default')


st.set_page_config(page_title='Seasonal EPL Football stats from 1993-94 to 2017-18',
                   page_icon='10+ Free Baby+Cute+Bunny+Cartoon,+Cute+ & Easter Images.jpg',
                   layout="wide")


eda=pd.read_excel('EPL_Set.xlsx')
eda1=pd.read_excel('EPL_Set.xlsx',sheet_name='Sheet1')
eda.fillna(0,inplace=True)



row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3 = st.beta_columns(
    (.1, 2, 1.5, 1, .1)
    )


row1_1.title('Seasonal EPL Football stats')


with row1_2:
    st.write('')
    row1_2.subheader(
    'A Web App by [Hanuma shashank](https://www.linkedin.com/in/hanuma-shashank-5b244a1a2/)')
   
    
row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3 = st.beta_columns(
    (.1, 1.6, .1, 1.6, .1)
    )


with row2_1:
    st.write('')
    selected_team=st.selectbox('Select team name', eda1['TotalTeam'])
    
    
with row2_2:
    selected_season=st.selectbox('Select season name', eda.Season.unique())
    
 
            
row1_space1, row1_1, row1_space3, row1_3 = st.beta_columns(
    (.15,2, 1.5, 0.5)
    )



with row1_1:
    st.subheader('Team Logo')
    img = Image.open(str(selected_team)+'.png')
    st.image(img, width=200)


with row1_space3:
    
    df_new=eda[((eda['HomeTeam']==selected_team)|(eda['AwayTeam']==selected_team)) & (eda['Season']==selected_season)]
    
    with row1_3:
        option=st.selectbox('Choose your option', ['HomeTeam','AwayTeam'])
    
    if(option=='HomeTeam'):
        
        df_new1=df_new[df_new['HomeTeam']==selected_team]

        df_win=df_new1[(df_new1['FTR']=='H')]
        total_wins=df_win.shape[0]
        df_draw=df_new1[(df_new1['FTR']=='D')]
        total_draws=df_draw.shape[0]
        total_looses=df_new1.shape[0]-(df_win.shape[0]+df_draw.shape[0])
        
        data=[total_wins,total_draws,total_looses]
        plot_labels=['WIN','DRAW','LOOSE']
        
        #st.subheader("Seasonal Team Stats")
        fig = px.pie(values=data,names=plot_labels,title="Seasonal Team Stats")
        st.plotly_chart(fig,use_container_width=True)
        
    else:
        
        df_new1=df_new[df_new['AwayTeam']==selected_team]
        
        df_win=df_new1[(df_new1['FTR']=='A')]
        total_wins=df_win.shape[0]
        df_draw=df_new1[(df_new1['FTR']=='D')]
        total_draws=df_draw.shape[0]
        total_looses=df_new1.shape[0]-(df_win.shape[0]+df_draw.shape[0])
        
        data=[total_wins,total_draws,total_looses]
        plot_labels=['WIN','DRAW','LOOSE']
        
        #st.subheader("Seasonal Team Stats")
        fig = px.pie(values=data,names=plot_labels,title="Seasonal Team Stats")
        st.plotly_chart(fig,use_container_width=True)
    
             

row3_space1, row3_1, row3_space1,r,row3_2,row3_space2 = st.beta_columns(
    (.25,1.25,0.5,0.09, 1.25,0.5)
    )

    
with row3_1:
    
    with row3_space1:
        
        options=st.selectbox('Choose your option', ['Home','Away'])

    if(options=='Home'):
        
        df_new2=df_new[df_new['HomeTeam']==selected_team]
        
        goals=df_new2['FTHG'].sum()
        conceded=df_new2['FTAG'].sum()
        
        data=[goals,conceded]
        plot_labels=['GOAL!!','CONCEDE']
        
        #st.subheader("Team Goal Details")
        fig = px.pie(values=data,names=plot_labels,title="Team Goal Details")
        st.plotly_chart(fig,use_container_width=True)
        
    else:
        
        df_new2=df_new[df_new['AwayTeam']==selected_team]

        goals=df_new2['FTAG'].sum()
        conceded=df_new2['FTHG'].sum()
        
        data=[goals,conceded]
        plot_labels=['GOAL!!','CONCEDE']
        
        #st.subheader("Team Goal Details")
        fig = px.pie(values=data,names=plot_labels,title="Team Goal Details")
        st.plotly_chart(fig,use_container_width=True)
    
    
with row3_2:
    
    with row3_space2:
        
        options=st.selectbox('Choose your option', ['H','A'])
        
    if(options=='H'):
        
        df_new3=df_new[df_new['HomeTeam']==selected_team]
        
        df_scored=df_new3[(df_new3['FTHG']>=0)]
        goals=df_scored.shape[0]
        df_concede=df_new3[(df_new3['FTAG']>=0)]
        conceded=df_concede.shape[0]
        
        data=[goals,conceded]
        plot_labels=['GOAL!! Greater than 0','CONCEDES Greater than 0']
        
        #st.subheader("Team Goal Details")
        fig = px.pie(values=data,names=plot_labels,title="Team Goal Details")
        st.plotly_chart(fig,use_container_width=True)
    
    else:
        
        df_new3=df_new[df_new['AwayTeam']==selected_team]
        
        df_scored=df_new3[(df_new3['FTAG']>=0)]
        goals=df_scored.shape[0]
        df_concede=df_new3[(df_new3['FTHG']>=0)]
        conceded=df_concede.shape[0]
        
        data=[goals,conceded]
        plot_labels=['GOAL!! Greater than 0','CONCEDES Greater than 0']
        
        #st.subheader("Team Goal Details")
        fig = px.pie(values=data,names=plot_labels,title="Team Goal Details")
        st.plotly_chart(fig,use_container_width=True)
    

row4_space1, row4_1, row4_2, row4_space2 = st.beta_columns(
    (0.35,1.5,0.25,0.25)
    )


with row4_1:
    
    with row4_2:
        
        options=st.selectbox('Choose your option',['HomeTop','HomeBottom','AwayTop','AwayBottom'])
        
    if(options=='HomeTop'):
        
        st.subheader("Top and least five scorings of a team")
        df_new4=df_new[df_new['HomeTeam']==selected_team]
        df_new4.sort_values(by='FTHG',ascending=False,inplace=True)
        df_new4.iloc[:5]
    
    elif(options=='HomeBottom'):
        
        st.subheader("Top and least five scorings of a team")
        df_new4=df_new[df_new['HomeTeam']==selected_team]
        df_new4.sort_values(by='FTHG',ascending=True,inplace=True)
        df_new4.iloc[:5]
        
    elif(options=='AwayTop'):
        
        st.subheader("Top and least five scorings of a team")
        df_new4=df_new[df_new['AwayTeam']==selected_team]
        df_new4.sort_values(by='FTAG',ascending=True,inplace=True)
        df_new4.iloc[:5]
        
    else:
        
        st.subheader("Top and least five scorings of a team")
        df_new4=df_new[df_new['AwayTeam']==selected_team]
        df_new4.sort_values(by='FTAG',ascending=True,inplace=True)
        df_new4.iloc[:5]






