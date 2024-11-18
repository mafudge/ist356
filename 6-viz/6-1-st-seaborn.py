import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.title('Seaborn Visualizations Example')
st.caption('This is a simple example of how to use Seaborn to create visualizations. Seaborn allows you to pre-aggregate data, and provides more control over the look and feel of the charts.')

df  = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/delimited/fudge_companies.csv')
st.dataframe(df)

st.write('## Bar Plots')
st.caption("Seaborn does aggregates with an estimator")
bar_y = st.selectbox('Select y', ["Ordered", "Returned", "Sold"], key="bar_y")
if bar_y:
    fig1, ax1 = plt.subplots()
    fig1.suptitle(f"Total {bar_y} by Month")
    sns.barplot(data=df, x="Month", y=bar_y, estimator="sum", hue="Month", ax=ax1)
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    fig2.suptitle(f"Average {bar_y} by Month")
    sns.barplot(data=df, x="Month", y=bar_y, estimator="mean", errorbar=None, hue="Month", ax=ax2)
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    fig3.suptitle(f"Total {bar_y} by Month breakdowns by department")
    sns.barplot(data=df, x="Month", y=bar_y, estimator="sum", errorbar=None, hue="Dept", ax=ax3)
    st.pyplot(fig3)


st.write('## Line Plots')
st.caption("Lines plot the same as bars")
line_y = st.selectbox('Select y', ["Ordered", "Returned", "Sold"], key="line_y")
if line_y:
    fig1, ax1 = plt.subplots()
    fig1.suptitle(f"Total {bar_y} by Month")
    sns.lineplot(data=df, x="Month", y=line_y, estimator="sum", ax=ax1)
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    fig2.suptitle(f"Average {bar_y} by Month")
    sns.lineplot(data=df, x="Month", y=line_y, estimator="mean", errorbar=None, ax=ax2)
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    fig3.suptitle(f"Total {bar_y} by Month breakdowns by department")
    sns.lineplot(data=df, x="Month", y=line_y, estimator="sum", hue="Dept", ax=ax3)
    st.pyplot(fig3)


st.write('## Scatter / lm plots Plots')
st.caption("Scatter / lmplots Plots are for comparisons of 2 numerical values they do not aggregate your data") 
scat_x = st.selectbox('Select x', ["Ordered", "Returned", "Sold"], key="scat_x")
scat_y = st.selectbox('Select y', ["Ordered", "Returned", "Sold"], key="scat_y")
if scat_x and scat_y:
    fig1, ax1 = plt.subplots()
    fig1.suptitle(f"{scat_x} vs {scat_y}")
    sns.scatterplot(data=df, x=scat_x, y=scat_y, ax=ax1)
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    fig2.suptitle(f"{scat_x} vs {scat_y} by Store")
    sns.scatterplot(data=df, x=scat_x, y=scat_y, hue="Store", ax=ax2)
    st.pyplot(fig2)

    # lmplot is its own figure
    fig3 = sns.lmplot(data=df, x=scat_x, y=scat_y)
    st.pyplot(fig3)

    fig4 = sns.lmplot(data=df, x=scat_x, y=scat_y, hue="Store")
    st.pyplot(fig4)


st.write('## Histograms')
st.caption("Histograms are great for distributions across one numerical dimension")
hist_x = st.selectbox('Select x', ["Ordered", "Returned", "Sold"], key="hist_x")
if hist_x:
    fig1, ax1 = plt.subplots()
    fig1.suptitle(f"{hist_x} Histogram")
    sns.histplot(data=df, x=hist_x, ax=ax1)
    st.pyplot(fig1)

    fig1a, ax1a = plt.subplots()
    fig1a.suptitle(f"{hist_x} Histogram with Kernel Density Estimate")
    sns.histplot(data=df, x=hist_x, ax=ax1a, kde=True)
    st.pyplot(fig1a)

    fig2, ax2 = plt.subplots()
    fig2.suptitle(f"{hist_x} by Store")
    sns.histplot(data=df, x=hist_x, hue="Store", ax=ax2)
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    fig3.suptitle(f"{hist_x} by Store (dodged side by side)")
    sns.histplot(data=df, x=hist_x, hue="Store", multiple="dodge", ax=ax3)
    st.pyplot(fig3)
