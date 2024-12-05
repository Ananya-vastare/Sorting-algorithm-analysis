import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import *
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


# Set background color
set_background_color()
# Load the data from the Excel file
sample_data1 = pd.read_excel("Datatimings.xlsx")
sample_data2 = pd.read_excel("Datatimings1.xlsx")
# Extract the data for plotting from the first Excel file
x1 = [int(y) for y in sample_data1.InputSize]
t1_1 = [float(y) for y in sample_data1.Time_Taken_Bubble_Sort]
t2_1 = [float(y) for y in sample_data1.Time_Taken_Selection_Sort]

# Extract the data for plotting from the second Excel file
x2 = [int(y) for y in sample_data2.InputSize]
t1_2 = [float(y) for y in sample_data2.Time_Taken_Bubble_Sort]
t2_2 = [float(y) for y in sample_data2.Time_Taken_Selection_Sort]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
fig.suptitle("Graph for bubble sort and selection sort", fontsize=16)
ax1.plot(x1, t1_1, color="blue", label="Bubble Sort", marker="o")
ax1.plot(x1, t2_1, color="green", label="Selection Sort", marker="s")
ax1.set_xlabel("Input size")
ax1.set_ylabel("Time taken in seconds")
ax1.set_title("Optimized Code's Graph")
ax1.set_xticks(
    [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
)  # sets the x-axis range
ax1.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9])  # y-axis range
ax1.legend()
ax1.grid(True)

# Plot the data for the second subplot
ax2.plot(x2, t1_2, color="blue", label="Bubble Sort", marker="o")
ax2.plot(x2, t2_2, color="green", label="Selection Sort", marker="s")
ax2.set_xlabel("Input size")
ax2.set_ylabel("Time taken in seconds")
ax2.set_title("Non Optimized Code's Graph")
ax2.set_xticks([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
ax2.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9])
ax2.legend()
ax2.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
st.pyplot(fig)
