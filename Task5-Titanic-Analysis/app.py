import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Titanic Dashboard", layout="wide")

st.markdown("""
<style>
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #3b0764 0%, #7e22ce 50%, #a855f7 100%);
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 4px 12px rgba(168, 85, 247, 0.3);
}
div[data-testid="stMetricLabel"] { color: #e9d5ff; }
div[data-testid="stMetricValue"] { color: #ffffff; }

/* Selected pill buttons -> purple theme */
button[data-variant="pills"][data-selected="true"] {
    background-color: #7e22ce 75% !important;
    border-color: #7e22ce !important;
    color: #ffffff !important;
    }

/* Make the filter column (last column of the first horizontal block) stick while scrolling */
div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="stColumn"]:last-of-type {
    position: sticky;
    top: 1rem;
    align-self: flex-start;
}
</style>
""", unsafe_allow_html=True)

PURPLE_SCALE = ["#c084fc", "#a855f7", "#9333ea", "#7e22ce", "#581c87"]

# TITLE ----------------------------------
st.title("Titanic Passenger Analysis Dashboard")

#Load the cleaned dataset, cached so it's not re-read every interaction
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_titanic.csv")
    return df

df = load_data()

# st.subheader("Data Preview")
# st.dataframe(df.head(10))

# Data note
st.warning(
    "**Data Note:** The 'Survived' column matches 'Sex' with 100% overlap in this dataset "
    "(all women survived, no men did). Survived-based findings should be interpreted with caution."
)

AGEGROUP_ORDER = ["Child","Teen", "Adult", "Senior"]

main_col, filter_col = st.columns([3, 1])

#FILTERS ----------------------------------
with filter_col:
    st.subheader("Filters")

    filter_config = {
        'Pclass': ('Passenger Class',None),
        'Sex': ('Sex',None),
        'Embarked': ('Embarked', None),
        'AgeGroup': ('Age Group',AGEGROUP_ORDER),
    }

    
    selections = {}
    for col_name, (label,fixed_order) in filter_config.items():
        available = df[col_name].dropna().unique().tolist()
        options = [v for v in fixed_order if v in available] if fixed_order else sorted(available)
        selections[col_name] = st.pills(
            label, options= options, selection_mode= "multi", default= options
        )

mask = pd.Series(True, index=df.index)
for col_name, selected_values in selections.items():
    mask &= df[col_name].isin(selected_values)

df_filtered = df[mask]

 # Overview KPI section ----------------------------------
with main_col:
    st.subheader("Overview")

    if len(df_filtered)>0:
        kpis ={
            "Total Passengers": len(df_filtered),
            "Average Age": round(df_filtered['Age'].mean(), 1),
            "Median Fare": f"${round(df_filtered['Fare'].median(), 1)}",
            "Avg Family Size": round(df_filtered['FamilySize'].mean(),2),
        }
        cols = st.columns(len(kpis))
        for col, (label, value) in zip(cols, kpis.items()):
            col.metric(label, value)


        # DEMOGRAPHICS ----------------------------------
        st.subheader("Whi Was on Board?")

        template = "plotly_dark"

        row1= st.columns(3)
        with row1[0]:
            # Donut chart: Sex distribution
            counts= df_filtered['Sex'].value_counts().reset_index()
            counts.columns= ['Sex', 'Count']
            fig = px.pie(counts, names='Sex', values='Count', hole=0.5,
                        title="Sex Distribution", color_discrete_sequence = PURPLE_SCALE,
                        template = template)
            st.plotly_chart(fig, use_container_width=True)
        
        with row1[1]:
             # Funnel chart: Passenger class (1st -> 2nd -> 3rd is a natural ranked order)
            counts = df_filtered['Pclass'].value_counts().sort_index().reset_index()
            counts.columns = ['Pclass', 'Count']
            counts['Pclass'] = counts['Pclass'].map({1: '1st Class', 2: '2nd Class', 3: '3rd Class'})
            fig = px.funnel(counts, x='Count', y='Pclass', title="Passenger Class Distribution",
                             color_discrete_sequence=["#a855f7"], template=template)
            st.plotly_chart(fig, use_container_width=True)

        with row1[2]:
            # Stacked bar: Embarked x Pclass -> was passenger class mix different by port?
            counts = df_filtered.groupby(['Embarked', 'Pclass']).size().reset_index(name='Count')
            counts['Pclass'] = counts['Pclass'].map({1: '1st Class', 2: '2nd Class', 3: '3rd Class'})
            fig = px.bar(counts, x='Embarked', y='Count', color='Pclass', barmode='stack',
                         title="Passenger Class Mix by Port", color_discrete_sequence=PURPLE_SCALE,
                         template=template)
            st.plotly_chart(fig, use_container_width=True)
             
        row2 = st.columns(3)

        with row2[0]:
            # Histogram: Age distribution (continuous variable)
            fig = px.histogram(df_filtered, x='Age', nbins=30, title="Age Distribution",
                                color_discrete_sequence=["#a855f7"], template=template)

            fig.update_traces(
                marker_line_color="#3b0764",  
                marker_line_width=1.2,)
            st.plotly_chart(fig, use_container_width=True)

        with row2[1]:
            # Box plot: Fare spread by passenger class
            fig = px.box(df_filtered, x='Pclass', y='Fare', title="Fare Spread by Class",
                         color='Pclass', color_discrete_sequence=PURPLE_SCALE, template=template)
            st.plotly_chart(fig, use_container_width=True)

        with row2[2]:
          # Area chart: Family size distribution
            counts = df_filtered['FamilySize'].value_counts().sort_index().reset_index()
            counts.columns = ['FamilySize', 'Count']
            fig = px.area(counts, x='FamilySize', y='Count', title="Family Size Distribution",
                           color_discrete_sequence=["#a855f7"], template=template)
            st.plotly_chart(fig, use_container_width=True)

        # SURVIVED BREAKDOWN (CAVEATED) ----------------------------------
        st.subheader("Survived Breakdown")
      

        row3 = st.columns(2)

        with row3[0]:
            # Overlaid histogram: Age distribution split by Survived
            plot_df = df_filtered.copy()
            plot_df['Survived'] = plot_df['Survived'].map({0: 'Did not survive', 1: 'Survived'})
            fig = px.histogram(plot_df, x='Age', color='Survived', barmode='overlay', opacity=0.7,
                                nbins=30, title="Age Distribution by Survival",
                                color_discrete_sequence=["#581c87", "#c084fc"], template=template)
            st.plotly_chart(fig, use_container_width=True)

        with row3[1]:
            # Grouped bar: Survival rate by Pclass, split by Alone vs With Family
            grouped = (df_filtered.groupby(['Pclass', 'IsAlone'])['Survived'].mean() * 100).round(1).reset_index()
            grouped['IsAlone'] = grouped['IsAlone'].map({0: 'With Family', 1: 'Alone'})
            fig = px.bar(grouped, x='Pclass', y='Survived', color='IsAlone', barmode='group',
                         title="Survival Rate by Class and Travel Status",
                         color_discrete_sequence=["#a855f7", "#581c87"], template=template)
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No passengers match the selected filters.")





