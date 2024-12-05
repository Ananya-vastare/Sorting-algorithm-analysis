import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def set_background_color():
    st.markdown(
        """
        <style>
        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg,#2ecc71,#ffffff);
            height: 100vh;
            background-attachment: fixed;
        }
        header, footer {
            visibility: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


set_background_color()
data = pd.read_excel("Worstcases.xlsx")
x1 = [int(x) for x in data.Input_Size]
t1 = [int(x) for x in data.Time_taken_Bubble_sort]
t2 = [int(x) for x in data.Time_taken_Selection_sort]
t3 = [int(x) for x in data.Time_taken_Insertion_sort]
fig, ax = plt.subplots(figsize=(10, 6))
fig.suptitle("Traditional sorting algorithm's graph", fontsize=16)
ax.plot(x1, t1, color="blue", marker="o", label="Bubble sort")
ax.plot(x1, t2, color="purple", marker="*", label="Selection sort")
ax.plot(x1, t3, color="green", marker=".", label="Insertion sort")
ax.set_xlabel("Input Size")
ax.set_ylabel("Time taken (seconds)")
ax.set_title("Sorting Algorithms Performance")
ax.legend()  # labels are placed in the graph
ax.grid(True)
# Display plot in Streamlit
st.pyplot(fig)
