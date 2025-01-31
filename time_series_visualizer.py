import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True, index_col=0)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) 
    & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    df2 = df.copy()

    df2['Years'] = df2.index.year

    df2['Months'] = df2.index.month_name()
    df2['Month_num'] = df2.index.month

    df2 = df2.groupby(['Years', 'Months', 'Month_num'])['value'].mean().reset_index(name='Average Page Views')

    df2 = df2.sort_values(by=['Years', 'Month_num'])

    ordered_month_names = df2.sort_values(by=['Month_num'])['Months'].unique()

    bar_plot = sns.barplot(data=df2, x='Years', y='Average Page Views',
        hue='Months', hue_order=ordered_month_names)

    fig = bar_plot.fig
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
