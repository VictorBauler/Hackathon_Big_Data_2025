import marimo

__generated_with = "0.8.3"
app = marimo.App(width="medium")


@app.cell
def __(cols_drop, plot_df, px):


    fig = px.line(
        plot_df,                                  # The DataFrame to use
        x='week_date',                       # Column for the x-axis
        y=cols_drop.value,                  # Column for the y-axis
        title=f'{cols_drop.value} over Time',      # The title of the chart
        markers=True,                        # Show markers for each data point
        labels={                             # Customize axis labels
            "week_date": "Date",
            cols_drop.value: "Value"
        }
    )

    # Customize the plot's appearance for a cleaner look
    fig.update_layout(
        plot_bgcolor='white',
        font=dict(family="Arial, sans-serif", size=12, color="black")
    )
    return fig,


@app.cell
def __(mo, plot_df):
    cols = plot_df.columns

    cols_drop = mo.ui.dropdown(
        options=cols, value="gross_profit", label="Variável"
    )

    cols_drop

    plot_df.sort_values(by="week_date");
    return cols, cols_drop


@app.cell
def __(filtered_df, prod_drop):
    plot_df = filtered_df[filtered_df.produto == prod_drop.value]
    return plot_df,


@app.cell
def __(filtered_df, mo):
    produto_list = filtered_df.produto.value_counts().index.tolist()

    prod_drop = mo.ui.dropdown(
        options=produto_list, value=produto_list[0], label="Produto id"
    )

    prod_drop

    return prod_drop, produto_list


@app.cell
def __(df, pdv_drop):
    filtered_df = df[df.pdv == pdv_drop.value]

    return filtered_df,


@app.cell
def __(pdv_drop):
    pdv_drop
    return


@app.cell
def __(df):
    pdv_list = df.pdv.value_counts().index.tolist()
    return pdv_list,


@app.cell
def __(mo, pdv_list):
    pdv_drop = mo.ui.dropdown(
        options=pdv_list[0:20], value=pdv_list[0], label="PDV id"
    )
    return pdv_drop,


@app.cell
def __(df, pd):
    # Create a week_date column with format "week/month/year" extracting it from columns semana,mes and ano
    day_mapping = {1: 1, 2: 8, 3: 15, 4: 22, 5: 29}
    # 3. Create a 'day' column from the 'semana' column
    df['day'] = df['semana'].map(day_mapping).copy(
    )
    df['week_date'] = pd.to_datetime(df[['ano', 'mes', 'day']].rename(columns={'ano': 'year', 'mes': 'month'}))
    # Optional: Drop the intermediate 'day' column if you don't need it
    df.drop(columns=['day'], inplace=True)
    return day_mapping,


@app.cell
def __(pd):
    df = pd.read_parquet("/data/challenges/hackathon_bigdata_2025/processed_data/transacoes_merged.parquet")
    return df,


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    import plotly.express as px
    return mo, pd, plt, px


if __name__ == "__main__":
    app.run()
