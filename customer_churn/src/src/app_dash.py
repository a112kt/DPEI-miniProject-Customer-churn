import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import duckdb

# 📦 Connect to DuckDB
con = duckdb.connect("data/customer_churn_warehouse.duckdb")

# 📄 Load data from dbt models (analytics schema)
df = con.execute("SELECT * FROM analytics.fact_churn;").fetchdf()
con.close()

# 🧹 Basic cleaning
df['Contract'] = df['Contract'].fillna('Unknown')
df['InternetService'] = df['InternetService'].fillna('Unknown')

# 🎯 Calculations for KPIs
total_customers = len(df)
churn_rate = round(df['Churn_Flag'].mean() * 100, 2)
avg_monthly_charge = round(df['MonthlyCharges'].mean(), 2)

# 🎨 Initialize app
app = dash.Dash(__name__)
app.title = "Customer Churn Dashboard"

app.layout = html.Div([
    html.H1("📊 Customer Churn Analytics Dashboard", style={'textAlign': 'center'}),

    # KPIs
    html.Div([
        html.Div([
            html.H4("Total Customers"),
            html.H2(f"{total_customers}")
        ], className="card"),

        html.Div([
            html.H4("Overall Churn Rate (%)"),
            html.H2(f"{churn_rate}")
        ], className="card"),

        html.Div([
            html.H4("Average Monthly Charge ($)"),
            html.H2(f"{avg_monthly_charge}")
        ], className="card"),
    ], style={'display': 'flex', 'justifyContent': 'space-around'}),

    html.Hr(),

    # Filters
    html.Div([
        html.Label("Filter by Internet Service:"),
        dcc.Dropdown(
            id='service_filter',
            options=[{'label': s, 'value': s} for s in df['InternetService'].unique()],
            value='All',
            clearable=False
        ),
    ], style={'width': '40%', 'margin': '0 auto'}),

    html.Hr(),

    # Graphs
    html.Div([
        dcc.Graph(id='churn_by_contract'),
        dcc.Graph(id='churn_by_tenure'),
        dcc.Graph(id='churn_by_service')
    ])
])

# 🔄 Callbacks
@app.callback(
    [Output('churn_by_contract', 'figure'),
     Output('churn_by_tenure', 'figure'),
     Output('churn_by_service', 'figure')],
    Input('service_filter', 'value')
)
def update_graphs(service_filter):
    dff = df.copy()
    if service_filter != 'All':
        dff = dff[dff['InternetService'] == service_filter]

    fig1 = px.bar(
        dff.groupby('Contract', as_index=False)['Churn_Flag'].mean(),
        x='Contract', y='Churn_Flag', title='Churn Rate by Contract',
        color='Contract', text_auto='.2%'
    )

    fig2 = px.histogram(
        dff, x='tenure', color='Churn_Flag',
        nbins=30, barmode='overlay',
        title='Churn Distribution by Tenure'
    )

    fig3 = px.bar(
        dff.groupby('InternetService', as_index=False)['Churn_Flag'].mean(),
        x='InternetService', y='Churn_Flag',
        title='Churn Rate by Internet Service',
        color='InternetService', text_auto='.2%'
    )

    return fig1, fig2, fig3


if __name__ == '__main__':
    app.run(debug=True)

