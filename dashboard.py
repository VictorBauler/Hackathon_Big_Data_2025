import marimo

__generated_with = "0.8.3"
app = marimo.App(width="medium")


@app.cell
def __(cols_drop, go, mo, plot_df):
    import plotly.io as pio
    pio.renderers.default = 'notebook'

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=plot_df['week_date'],
        y=plot_df['quantidade'],
        mode='lines+markers',  # Can be 'lines', 'markers', or both
        name='Quantidade de vendas'       # This text appears in the legend
    ))

    # 5. Add the second line (trace)
    fig.add_trace(go.Scatter(
        x=plot_df['week_date'],
        y=plot_df[cols_drop.value],
        mode='lines+markers',
        name=cols_drop.value
    ))

    # 6. Update the layout to add titles and clean up the appearance
    fig.update_layout(
        title='Product Sales Over Time',
        xaxis_title='Date',
        yaxis_title='Value',
        plot_bgcolor='white',
        legend_title_text='Product'
    )
    #fig.add_trace(go.line(plot_df,x='week_date',y=
    #                    mode='markers', name='markers'))

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

    mo.ui.plotly(fig)
    return fig, pio


@app.cell
def __(mo, plot_df):
    cols = plot_df.columns

    cols_drop = mo.ui.dropdown(
        options=cols, value="gross_profit", label="Variável"
    )

    plot_df.sort_values(by="week_date", inplace=True);

    cols_drop
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
    import plotly.graph_objects as go
    return go, mo, pd, plt, px


if __name__ == "__main__":
    app.run()
