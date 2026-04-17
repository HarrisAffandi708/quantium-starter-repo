from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

task3= Dash()

df = pd.read_csv("pink_morsel_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

daily_sales = (
    df.groupby("Date", as_index=False)["Sales"]
    .sum()
    .sort_values("Date")
)

fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    markers=True,
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales",
    template="plotly_white"
)

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f8f9fa",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif",
    },
    children=[
        html.H1(
            "Soul Foods Sales Visualiser",
            style={
                "textAlign": "center",
                "marginBottom": "10px",
                "color": "#222",
            },
        ),
        html.Div(
            style={
                "maxWidth": "1100px",
                "margin": "0 auto",
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "12px",
            },
            children=[
                dcc.Graph(
                    id="sales-line-chart",
                    figure=fig
                )
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)