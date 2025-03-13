import plotly.express as px
from preswald import connect, get_df, plotly, table, text, slider, checkbox, selectbox, separator, alert, query
import pandas as pd
import numpy as np

# Report Title
text(
    "# Diabetes Analysis Dashboard \n This report provides analysis of diabetes data from the Pima Indians Diabetes Database, which contains diagnostic measurements for females at least 21 years old of Pima Indian heritage."
)

# Load the CSV
connect()
df = get_df("diabetes_csv")

# Data Overview
text(
    "## Dataset Overview \n This dataset consists of several medical predictors and one target variable, Outcome. Predictors include the number of pregnancies, BMI, insulin level, age, and more."
)

text("### Sample Data Records")
table(df, limit=10)

# Basic Statistics
text("### Summary Statistics")
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
stats_df = df[numeric_columns].describe().reset_index()
stats_df.columns = ['Statistic'] + list(stats_df.columns[1:])
table(stats_df)

# Visualizations
text(
    "## Feature Distributions \n The following visualizations show the distribution of key features and their relationship with diabetes outcome."
)

# Glucose Distribution by Outcome
text(
    "### Glucose Distribution by Diabetes Outcome \n Glucose levels tend to be higher in patients with diabetes (Outcome=1)."
)
fig1 = px.histogram(
    df, 
    x="Glucose", 
    color="Outcome", 
    barmode="overlay",
    title="Glucose Level Distribution by Diabetes Outcome",
    labels={"Outcome": "Diabetes Status"},
    color_discrete_map={"0": "skyblue", "1": "indianred"}
)
fig1.update_layout(template="plotly_white")
plotly(fig1)

# BMI Distribution by Outcome
text(
    "### BMI Distribution by Diabetes Outcome \n Higher BMI values are associated with higher diabetes risk."
)
fig2 = px.histogram(
    df, 
    x="BMI", 
    color="Outcome", 
    barmode="overlay",
    title="BMI Distribution by Diabetes Outcome",
    labels={"Outcome": "Diabetes Status"},
    color_discrete_map={"0": "skyblue", "1": "indianred"}
)
fig2.update_layout(template="plotly_white")
plotly(fig2)

# Age Distribution by Outcome
text(
    "### Age Distribution by Diabetes Outcome \n We can see how age correlates with diabetes diagnosis."
)
fig3 = px.histogram(
    df, 
    x="Age", 
    color="Outcome", 
    barmode="overlay",
    title="Age Distribution by Diabetes Outcome",
    labels={"Outcome": "Diabetes Status"},
    color_discrete_map={"0": "skyblue", "1": "indianred"}
)
fig3.update_layout(template="plotly_white")
plotly(fig3)

# Interactive Scatter Plot
text(
    "## Interactive Feature Relationship Analysis"
)
text(
    "This interactive tool allows you to explore relationships between any two features in the dataset and analyze how they relate to diabetes outcomes."
)

feature_list = [col for col in numeric_columns if col != "Outcome"]

separator()

alert(
    "### Select Features to Compare",
    "Use the dropdown menus below to select which features you want to analyze in the scatter plot.",
)

# CHeckbox from preswald
x_feature = selectbox("X-axis feature:", feature_list, default=feature_list[1])
y_feature = selectbox("Y-axis feature:", feature_list, default=feature_list[5])
show_trend = checkbox("Show regression trendline", default=True)

# Slider to filter data
text("### Filter Data")
text("Use this slider to filter data points based on the selected X-axis feature value:")
threshold = slider(f"{x_feature} threshold", min_val=int(df[x_feature].min()), max_val=int(df[x_feature].max()), default=int(df[x_feature].min()))
text(f"Showing only data points where {x_feature} > {threshold}")

filtered_df = df[df[x_feature] > threshold]

separator()

text(" Scatter Plot Results")
text(f"Showing the relationship between **{x_feature}** and **{y_feature}** (filtered data). Points are colored by diabetes outcome (blue = no diabetes, red = diabetes).")

fig4 = px.scatter(
    filtered_df,  # Using filtered data
    x=x_feature,
    y=y_feature,
    color="Outcome",
    title=f"{y_feature} vs {x_feature} by Diabetes Outcome (Filtered)",
    labels={"Outcome": "Diabetes Status"},
    color_discrete_map={"0": "skyblue", "1": "indianred"},
    trendline="ols" if show_trend else None
)
fig4.update_layout(template="plotly_white")
plotly(fig4)

text("### SQL Query Example")
sql = f"SELECT * FROM diabetes_csv WHERE {x_feature} > {threshold} LIMIT 10"
sql_filtered_df = query(sql, "diabetes_csv")
text("Results from SQL query:")
table(sql_filtered_df, title="SQL Query Results")

# Add analysis text based on the correlation
correlation = df[x_feature].corr(df[y_feature])
correlation_with_outcome_x = df[x_feature].corr(df['Outcome'])
correlation_with_outcome_y = df[y_feature].corr(df['Outcome'])

text(f"**Analysis:**")
text(f"- Correlation between {x_feature} and {y_feature}: **{correlation:.2f}**")
text(f"- Correlation of {x_feature} with diabetes: **{correlation_with_outcome_x:.2f}**")
text(f"- Correlation of {y_feature} with diabetes: **{correlation_with_outcome_y:.2f}**")

separator()

# Correlation Matrix
text(
    "## Feature Correlation Matrix \n This heatmap shows the correlation between different features in the dataset."
)
corr = df.corr()
fig5 = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="RdBu_r",
    title="Feature Correlation Matrix"
)
fig5.update_layout(template="plotly_white")
plotly(fig5)

# Outcome Distribution
text(
    "## Diabetes Outcome Distribution \n This pie chart shows the proportion of positive and negative diabetes diagnoses in the dataset."
)
outcome_counts = df['Outcome'].value_counts().reset_index()
outcome_counts.columns = ['Outcome', 'Count']
outcome_counts['Outcome'] = outcome_counts['Outcome'].map({0: 'No Diabetes', 1: 'Diabetes'})

fig6 = px.pie(
    outcome_counts,
    values='Count',
    names='Outcome',
    title="Diabetes Outcome Distribution",
    color_discrete_sequence=["skyblue", "indianred"]
)
fig6.update_layout(template="plotly_white")
plotly(fig6)

text(
    "## Feature Impact on Diabetes Risk \n This bar chart shows how individual features correlate with diabetes outcome."
)
# Calculate correlation with outcome for each feature
feature_importance = []
for col in df.columns:
    if col != 'Outcome':
        corr_val = df[col].corr(df['Outcome'])
        feature_importance.append({'Feature': col, 'Correlation': corr_val})

feature_imp_df = pd.DataFrame(feature_importance)
feature_imp_df = feature_imp_df.sort_values('Correlation', ascending=False)

fig7 = px.bar(
    feature_imp_df,
    x='Feature',
    y='Correlation',
    title="Feature Correlation with Diabetes Outcome",
    labels={"Correlation": "Correlation with Outcome"},
    color='Correlation',
    color_continuous_scale="RdBu_r"
)
fig7.update_layout(template="plotly_white")
plotly(fig7)

# Conclusion
text(
    "## Conclusion \n This analysis shows how various health metrics correlate with diabetes diagnoses. Glucose level, BMI, Age, and family history (DiabetesPedigreeFunction) appear to be significant indicators. Interactive tools in this dashboard can help in exploring deeper relationships between these factors."
)
