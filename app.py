import pandas as pd
import streamlit as st
import plotly.express as px



def selectData(name,datafr):
	partial = datafr[name].max()
	selection = datafr.loc[datafr[name]==partial]
	return selection

data = pd.read_csv("RailwireBilling.csv")
userdata = pd.read_csv("userdata.csv")
userdata.set_index("Details",inplace=True)

st.set_page_config(page_title="Data Usage Dashboard",page_icon="https://cdn-icons-png.flaticon.com/512/1340/1340311.png",layout="wide")

st.title("Hello Varun,")

st.subheader("Railwire Data Usage Dashboard")
st.title("")

fs1,fs2,fs3 = st.columns(3,gap="medium")

fs1.write("## Username:")
uname = list(userdata.loc["Username"])
fs1.write("# "+str(uname[1]))

fs2.write("## Recharge Plan:")
fs2.write("# Rs. "+str(list(userdata.loc["Price"])[1]))

fs3.write("## Expires On:")
fs3.write("# "+str(list(userdata.loc["Expiry"])[1]))

st.title("")

sh = data.shape

data2 = data.drop([sh[0]-1])

df = data[["Upload[MB]","Download[MB]","Total[MB]"]].loc[sh[0]-1]
l1=[]
for i in df:
	l1.append(i)
l2=["Upload","Download","Total"]
df1 = pd.DataFrame({"Speed":l1,"Usage Indicator":l2})
fig = px.bar(df1,x="Speed",orientation="h",template="plotly_white",color="Usage Indicator",title="<b> Total Data Usage Visualisation </b>")
fig.update_layout(plot_bgcolor="rgba(0,0,0,0)",xaxis=dict(showgrid=False))
st.plotly_chart(fig)
ss1,ss2 = st.columns(2,gap="medium")

ss1.write("## Framed IP Address:")
ss1.write("# "+str(data["Framed IP"][0]))

ss2.write("## MAC Address:")
ss2.write("# "+str(data["MAC"][0]))

df2part = data[["Upload[MB]","Download[MB]","Total[MB]"]]
df2 = df2part.drop([sh[0]-1])

fig = px.bar(df2,x="Upload[MB]",orientation="h",template="plotly_white",title="<b> Upload Data Usage </b>",color="Upload[MB]")
fig.update_layout(plot_bgcolor="rgba(0,0,0,0)",xaxis=dict(showgrid=False))
st.plotly_chart(fig)

se0 = selectData("Upload[MB]",data2)
st.subheader("Highest Upload data usage on ")
ts1,ts2,ts3 = st.columns(3,gap="medium")
ts1.write("## Date:")

x1 = str(se0["Start Time"])
x1l = list(map(str,x1.split()))
ts1.write("# "+x1l[1])

ts2.write("## Session Period:")
ts2.write("# "+x1l[2])
ts3.write("## Upload Data Used:")
ts3.write("# "+str(df2["Upload[MB]"].max()))

fig1 = px.bar(df2,x="Download[MB]",orientation="h",template="plotly_white",title="<b> Download Data Usage</b>",color="Download[MB]")
fig1.update_layout(plot_bgcolor="rgba(0,0,0,0)",xaxis=dict(showgrid=False))
st.plotly_chart(fig1)


se1 = selectData("Download[MB]",data2)
st.subheader("Highest Download data usage on ")
fs1,fs2,fs3 = st.columns(3,gap="medium")
fs1.write("## Date:")

y1 = str(se1["Start Time"])
y1l = list(map(str,y1.split()))
fs1.write("# "+str(y1l[1]))

fs2.write("## Session Period:")
fs2.write("# "+y1l[2])
fs3.write("## Download Data Used:")
fs3.write("# "+str(df2["Download[MB]"].max()))

fig2 = px.bar(df2,x="Total[MB]",orientation="h",template="plotly_white",title="<b> Total [Download+Upload] Data Usage </b>",color="Total[MB]")
fig2.update_layout(plot_bgcolor="rgba(0,0,0,0)",xaxis=dict(showgrid=False))
st.plotly_chart(fig2)

se2 = selectData("Total[MB]",data2)
st.subheader("Highest Total data usage on ")
fis1,fis2,fis3 = st.columns(3,gap="medium")
fis1.write("## Date:")

z1 = str(se2["Start Time"])
z1l = list(map(str,y1.split()))
fis1.write("# "+str(z1l[1]))
fis2.write("## Session Period:")
fis2.write("# "+z1l[2])
fis3.write("## Total[Upload+Download] Data Used:")
fis3.write("# "+str(df2["Total[MB]"].max()))

hide = """<style>
	#MainMenu {visbility: hidden;}	
	footer {visibility: hidden;}
	header {visibility: hidden;}
	</style?"""

st.markdown(hide,unsafe_allow_html=True)
