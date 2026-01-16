# import
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# header
st.title("Praktikum 06 Visualisasi Data")
st.write("Kelompok 24")
st.markdown("""
- Dimas Julian - 0110122067
""")

# dataset gender per store
stores = ['Store A', 'Store B', 'Store C']
male = [150, 200, 180]
female = [120, 230, 170]

# dataset transaksi penjualan
product_a = [200, 250, 300]
product_b = [150, 300, 200]

# dataset quarter
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]

# 1 Grafik Stacked Vertical Bar Chart
st.subheader("1. Stacked Vertical Bar Chart")
fig, ax = plt.subplots()
x = np.arange(len(stores))

ax.bar(x, male, label='Male', color='blue')
ax.bar(x, female, bottom=male, label='Female', color='pink')

ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)

# 2 Stacked Vertical Bar Chart dengan Matplotlib
st.subheader("2. Stacked Vertical Bar Chart (Produk)")
fig, ax = plt.subplots()
x = np.arange(len(stores))

ax.bar(x, product_a, label='Product A', color='blue')
ax.bar(x, product_b, bottom=product_a, label='Product B', color='green')

ax.set_title('Sales Transaction by Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Total Sales')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)

# 3 Kustomisasi Stacked Vertical Bar Chart
st.subheader("3. Custom Stacked Vertical Bar Chart")
fig, ax = plt.subplots()
x = np.arange(len(stores))

ax.bar(x, product_a, label='Product A', color='blue')
ax.bar(x, product_b, bottom=product_a, label='Product B', color='green')

# label text
for i in range(len(x)):
    plt.text(x[i], product_a[i]/2, str(product_a[i]), ha='center', color='white')
    plt.text(x[i], product_a[i] + product_b[i]/2, str(product_b[i]), ha='center', color='black')

ax.set_title('Customized Sales Chart')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)

# 4 Multiple Stacked Vertical Bar Chart (Quarter)
st.subheader("4. Multiple Stacked Vertical Bar Chart")
fig, ax = plt.subplots()

width = 0.4
x = np.arange(len(stores))

# Quarter 1
ax.bar(x - width/2, q1_male, width=width, label='Q1 Male', color='lightblue')
ax.bar(x - width/2, q1_female, width=width, bottom=q1_male, label='Q1 Female', color='pink')

# Quarter 2
ax.bar(x + width/2, q2_male, width=width, label='Q2 Male', color='blue')
ax.bar(x + width/2, q2_female, width=width, bottom=q2_male, label='Q2 Female', color='red')

ax.set_title('Population by Gender & Store (Multiple Quarters)')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)
