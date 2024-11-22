import streamlit as st 
st.title("thevenins theorom")
def output(vth,rth,rl):
    il=vth(rth+rl)
    pl=il*il*rl
    return il,pl

col1,col2=st.columns(2)
with col1:
    vth=st.number_input("vth(volt)",value=10)
    rth=st.number_input("rth(ohms)",value=10)
    rl=st.number_input("rl(ohms)",value=10)
    compute=st.button("compute")


with col2:
    with st.container(border=True):
        if compute:
            il,pl=output(vth,rth,rl)
            st.write(f"load current={il:.2f}A")
            st.write(f"load current={pl:.2f}watt")
