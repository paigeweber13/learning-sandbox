# before running, make sure you have python3 installed and make sure you have
# run `pip3 install lxml html5lib BeautifulSoup4 pandas numpy matplotlib`

import matplotlib.pyplot as plt
import pandas


### constants

# tables had to be manually downloaded to allow for table to be populated after
# page load 

# cs go html sourced from https://prosettings.net/cs-go-pro-settings-gear-list/
cs_go_html_filename = 'cs.html'

# r6 siege html sourced from 
# https://prosettings.net/rainbow-6-pro-settings-gear-list/
r6_siege_html_filename = 'r6.html'


### Functions

def load_tables():
    with open(cs_go_html_filename, 'r') as f:
        cs_html = f.read()
    with open(r6_siege_html_filename, 'r') as f:
        r6_html = f.read()

    cs_dfs = pandas.read_html(cs_html)
    r6_dfs = pandas.read_html(r6_html)

    return (cs_dfs[0], r6_dfs[0])

def create_frequency_chart(pd_series, max_to_show=0, plt_title='', 
        plt_xlabel='', plt_ylabel=''):
    counts = pd_series.value_counts()

    if max_to_show > 0:
        counts = counts[0:max_to_show]

    counts = counts.sort_values()
    x = counts.keys()
    y = counts.values
    plt.figure(figsize=(10, 7))
    plt.subplots_adjust(left=0.3)
    plt.title(plt_title)
    plt.ylabel(plt_ylabel)
    plt.xlabel(plt_xlabel)
    plt.barh(x, y)

def main():
    cs_df, r6_df = load_tables()
    create_frequency_chart(cs_df['Mouse'], 20, 
        'CS: GO Professional Mouse Choices', 'Number of Users', 'Mouse')
    create_frequency_chart(r6_df['Mouse'], 20, 
        'R6: Siege Professional Mouse Choices', 'Number of Users', 'Mouse')
    plt.show()

if __name__ == '__main__':
    main()

