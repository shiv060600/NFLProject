import numpy as np 
import streamlit as st
from  scipy.stats import norm

def blackscholes(r,S,K,T,sigma):
    d1 = ((np.log(S/K)) + (r + (sigma**2)/2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - (sigma*np.sqrt(T))
    call_Price = (S * norm.cdf(d1,0,1)) - (K*np.exp(-r * T) * norm.cdf(d2,0,1)) 
    put_Price = (K * np.exp(-r * T) * norm.cdf(-d2,0,1)) - (S * norm.cdf(-d1, 0 ,1))
    return [call_Price,put_Price]

st.title("Option Pricing -  Shiv Bhutani")

#define variables 

with st.sidebar:
    r = st.text_input("Risk-Free Interest Rate", 0.1)
    S = st.text_input("Current Stock Price",30)
    K = st.text_input("Strike Price",40)
    T = st.text_input("Time Remaining until Option Expiration (days)", 240)
    sigma = st.text_input("Volatility as Percentage" ,0.3 )
r = float(r)   
S = float(S)
K = float(K)
T = float(int(T)/365)
sigma = float(sigma) 
prices = blackscholes(r,S,K,T,sigma)
col1 , col2 = st.columns(2)
with col1:
    call_Texts = [" Call Price:", str([prices[0]])]
    st.text_input("Call Price is: ", str(prices[0]))
with col2:
    st.text_input("Call Price is: ", str(prices[1]))







