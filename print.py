import streamlit as st
import random as r

st.header("𝑬𝒗𝒆𝒏 𝒊𝒇 𝒚𝒐𝒖 𝒄𝒂𝒏 𝒈𝒆𝒕 𝒐𝒏𝒆 𝒕𝒂𝒔𝒌 𝒅𝒐𝒏𝒆, 𝒕𝒉𝒂𝒕'𝒔 𝒕𝒉𝒆 𝒘𝒊𝒏 𝒎𝒚 𝒈𝒖𝒚!❤️")
st.subheader("𝙒𝙝𝙖𝙩 𝙖𝙧𝙚 𝙮𝙤𝙪 𝙬𝙖𝙞𝙩𝙞𝙣𝙜 𝙛𝙤𝙧?")
dip = st.text_input("Enter your name!")
if dip:
    st.success(f"Welcome {dip}")

messages = [
    f"Nice job! You crushed it {dip}! 💪",
    f"One down, many more victories to come {dip}! 🚀",
    f"Boom! Task annihilated {dip}! 🔥",
    f"You're on fire today {dip}! 🔥🔥🔥",
    f"Well done, warrior {dip}! 🛡️",
    f"That’s how legends do it {dip}! 🏆",
    f"Task? More like snack {dip}! 😎",
    f"You're unstoppable {dip}! ⚡"
]

num_tasks = st.number_input("How many tasks do you want to enter?", min_value=1, max_value=20, step=1)
tasks = []

for i in range(num_tasks):
    task = st.text_input(f"Task {i + 1}", key=f"task_{i}")
    if task:
        tasks.append(task)

if tasks:
    st.subheader("✅ Your Tasks:")
    for i, t in enumerate(tasks):
        done = st.checkbox(f"{t}", key=f"done_{i}")
        if done:
            message = r.choice(messages)
            st.success(message)