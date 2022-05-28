import streamlit as st
import streamlit.components.v1 as components
import random
st.set_page_config(page_title="可编辑脑图", layout="wide")
p = open("naotu.html", encoding="utf-8")
components.html(p.read(), height=1000, width=1800, scrolling=True)
choose = st.sidebar.selectbox("是否要进行截图保存", ("是", "否"))
if choose == "是":
  import PIL.ImageGrab
  import time
  time.sleep(3)
  scr = PIL.ImageGrab.grab()
  scr.save("screen.png")
else:
  pass
