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
    df_line = df.copy()

    df_line.reset_index(inplace=True)
    df_line.rename(columns={'date': 'Date', 'value':'Page Views'}, inplace=True)

    fig, ax = plt.subplots(figsize=(16, 4))

    df_line.plot(x='Date', y='Page Views', kind='line', 
        #kwargs
        ax=ax,
        title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
        ylabel='Page Views',
        legend=False,
        color='red'
    )
    #plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['Years'] = df_bar.index.year

    df_bar['Months'] = df_bar.index.month_name()
    df_bar['Month_num'] = df_bar.index.month

    df_bar = df_bar.groupby(['Years', 'Months', 'Month_num'])['value'].mean().reset_index(name='Average Page Views')

    df_bar = df_bar.sort_values(by=['Years', 'Month_num'])

    ordered_month_names = df_bar.sort_values(by=['Month_num'])['Months'].unique()


    # Draw bar plot
    bar_plot = sns.barplot(data=df_bar, x='Years', y='Average Page Views',
        hue='Months', hue_order=ordered_month_names)

    fig = bar_plot.fig

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
    df_box['Month_num'] = [d.month for d in df_box.date]

    fig, ax = plt.subplots(1,2,figsize=(20, 8))

    sns.boxplot(data=df_box.sort_values(by=['year']),
        ax=ax[0], x='year', y='value', hue='year', legend=False
        ,palette=sns.color_palette("tab10")
    )

    sns.boxplot(data=df_box.sort_values(by=['Month_num']),
        ax=ax[1], x='month', y='value', hue='month', legend=False, 
        # hue_order=ordered_month_names2
    )

    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
