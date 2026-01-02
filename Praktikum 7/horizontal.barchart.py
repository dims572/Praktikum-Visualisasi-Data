import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Praktikum 7 Visualisasi Data")
st.subheader("Horizontal Bar Chart & Stacked Horizontal Bar Chart")

st.write("Kelompok: 24")
st.markdown("""
- DIMAS JULIAN (0110122067)
""")

# ======================
# DATASET
# ======================
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales_2023 = [350, 420, 300, 200]
sales_2024 = [300, 450, 320, 300]

y = np.arange(len(brands))
bar_width = 0.4

# ======================
# PILIH KATEGORI
# ======================
kategori = st.selectbox(
    "Pilih kategori visualisasi",
    ['Basic Chart', 'Kustomisasi Grafik', 'Multiple Chart']
)

# ======================
# BASIC CHART
# ======================
if kategori == "Basic Chart":
    st.subheader("Horizontal Bar Chart Sederhana")

    fig1, ax1 = plt.subplots()
    ax1.barh(y, sales_2023, color='skyblue')
    ax1.set_yticks(y)
    ax1.set_yticklabels(brands)
    ax1.set_title('Horizontal Bar Chart - 2023')
    ax1.set_xlabel('Jumlah Penjualan')
    ax1.set_ylabel('Merk')
    st.pyplot(fig1)

    st.subheader("Stacked Horizontal Bar Chart Sederhana")

    fig2, ax2 = plt.subplots()
    ax2.barh(y, sales_2023, color='skyblue', label='2023')
    ax2.barh(y, sales_2024, left=np.array(sales_2023),
             color='lightgreen', label='2024')
    ax2.set_yticks(y)
    ax2.set_yticklabels(brands)
    ax2.set_title('Stacked Horizontal Bar Chart')
    ax2.set_xlabel('Jumlah Penjualan')
    ax2.set_ylabel('Merk')
    ax2.legend()
    st.pyplot(fig2)

# ======================
# KUSTOMISASI
elif kategori == "Kustomisasi Grafik":
    st.subheader("Kustomisasi Horizontal Bar Chart")

    fig3, ax3 = plt.subplots()
    ax3.barh(y, sales_2023, color='skyblue', edgecolor='black')
    ax3.set_yticks(y)
    ax3.set_yticklabels(brands)
    ax3.set_title('Kustomisasi Horizontal Bar Chart - 2023')
    ax3.set_xlabel('Jumlah Penjualan')
    ax3.set_ylabel('Merk')
    ax3.grid(axis='x', linestyle='--', alpha=0.6)

    for i, v in enumerate(sales_2023):
        ax3.text(v + 5, i, str(v), va='center')

    st.pyplot(fig3)

    st.subheader("Kustomisasi Stacked Horizontal Bar Chart")

    fig4, ax4 = plt.subplots()
    ax4.barh(y, sales_2023, color='violet', edgecolor='black', label='2023')
    ax4.barh(y, sales_2024, left=np.array(sales_2023),
             color='coral', edgecolor='black', label='2024')
    ax4.set_yticks(y)
    ax4.set_yticklabels(brands)
    ax4.set_title('Kustomisasi Stacked Horizontal Bar Chart')
    ax4.set_xlabel('Sales')
    ax4.set_ylabel('Brands')
    ax4.grid(axis='x', linestyle='--', alpha=0.6)
    ax4.legend()
    st.pyplot(fig4)

# ======================
# MULTIPLE CHART
# ======================
else:
    st.subheader("Multiple Horizontal Bar Chart")

    fig5, ax5 = plt.subplots()
    ax5.barh(y - bar_width/2, sales_2023,
             height=bar_width, label='2023', color='violet')
    ax5.barh(y + bar_width/2, sales_2024,
             height=bar_width, label='2024', color='coral')
    ax5.set_yticks(y)
    ax5.set_yticklabels(brands)
    ax5.set_title('Multiple Horizontal Bar Chart')
    ax5.set_xlabel('Sales')
    ax5.set_ylabel('Brands')
    ax5.grid(axis='x', linestyle='--', alpha=0.6)
    ax5.legend()
    st.pyplot(fig5)

    st.subheader("Multiple Stacked Horizontal Bar Chart")

    fig6, ax6 = plt.subplots()
    ax6.barh(y, sales_2023, color='violet', label='2023')
    ax6.barh(y, sales_2024, left=np.array(sales_2023),
             color='coral', label='2024')
    ax6.set_yticks(y)
    ax6.set_yticklabels(brands)
    ax6.set_title('Multiple Stacked Horizontal Bar Chart')
    ax6.set_xlabel('Sales')
    ax6.set_ylabel('Brands')
    ax6.grid(axis='x', linestyle='--', alpha=0.6)
    ax6.legend()
    st.pyplot(fig6) 
