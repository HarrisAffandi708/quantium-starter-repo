from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("pink_morsel_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Region"] = df["Region"].str.lower().str.strip()

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f8",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif",
    },
    children=[
        html.Div(
            style={
                "maxWidth": "1100px",
                "margin": "0 auto",
                "backgroundColor": "white",
                "borderRadius": "16px",
                "padding": "30px",
                "boxShadow": "0 4px 14px rgba(0, 0, 0, 0.12)",
            },
            children=[
                html.H1(
                    "Soul Foods Pink Morsel Sales Visualiser",
                    style={
                        "textAlign": "center",
                        "color": "#1f3c88",
                        "marginBottom": "10px",
                    },
                ),
                html.P(
                    "Explore daily Pink Morsel sales overall or by region to compare performance before and after the 15 January 2021 price increase.",
                    style={
                        "textAlign": "center",
                        "color": "#555",
                        "fontSize": "18px",
                        "marginBottom": "30px",
                    },
                ),
                html.Div(
                    style={
                        "marginBottom": "25px",
                        "padding": "15px",
                        "backgroundColor": "#eef3ff",
                        "borderRadius": "12px",
                    },
                    children=[
                        html.Label(
                            "Filter by Region:",
                            style={
                                "fontWeight": "bold",
                                "fontSize": "16px",
                                "color": "#222",
                                "display": "block",
                                "marginBottom": "10px",
                            },
                        ),
                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                            ],
                            value="all",
                            inline=True,
                            labelStyle={
                                "marginRight": "20px",
                                "fontSize": "15px",
                                "color": "#333",
                            },
                            inputStyle={"marginRight": "6px"},
                        ),
                    ],
                ),
                dcc.Graph(id="sales-line-chart"),
            ],
        )
    ],
)

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["Region"] == selected_region]

    daily_sales = (
        filtered_df.groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Date")
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=daily_sales["Date"],
            y=daily_sales["Sales"],
            mode="lines+markers",
            name="Sales"
        )
    )

    fig.add_vline(
        x=pd.Timestamp("2021-01-15"),
        line_width=2,
        line_dash="dash"
    )

    chart_title = (
        "Pink Morsel Sales Over Time (All Regions)"
        if selected_region == "all"
        else f"Pink Morsel Sales Over Time ({selected_region.title()} Region)"
    )

    fig.update_layout(
        title=chart_title,
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white",
        title_x=0.5,
        paper_bgcolor="white",
        plot_bgcolor="white",
        annotations=[
            dict(
                x=pd.Timestamp("2021-01-15"),
                y=1,
                xref="x",
                yref="paper",
                text="Price increase: 15 Jan 2021",
                showarrow=False,
                xanchor="left",
                yanchor="bottom"
            )
        ]
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)