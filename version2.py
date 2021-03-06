import statistics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import kurtosis
from scipy.stats import skew

# import dataframe
data = pd.read_csv("https://raw.githubusercontent.com/J-tin/CarryOn/master/data.csv")
print(data.columns)  # get column index获取列索引值
print(data.index)  # get range index获取行索引值
year_return = data[' value']
year = data['date']

# devide year_return into 13 groups according to the x-axis-scale

group1 = []
group2 = []
group3 = []
group4 = []
group5 = []
group6 = []
group7 = []
group8 = []
group9 = []
group10 = []
group11 = []
group12 = []
group13 = []

group_number = list(range(99))

for n in group_number:
    yr_return = data.at[n, ' value']

    if yr_return >= -60 and yr_return <= -50:
        year_name = data.at[n, 'date']
        group1.append(year_name)

    elif yr_return >= -50 and yr_return <= -40:
        year_name = data.at[n, 'date']
        group2.append(year_name)

    elif yr_return >= -40 and yr_return <= -30:
        year_name = data.at[n, 'date']
        group3.append(year_name)
    elif yr_return >= -30 and yr_return <= -20:
        year_name = data.at[n, 'date']
        group4.append(year_name)
    elif yr_return >= -20 and yr_return <= -10:
        year_name = data.at[n, 'date']
        group5.append(year_name)
    elif yr_return >= -10 and yr_return <= -0:
        year_name = data.at[n, 'date']
        group6.append(year_name)
    elif yr_return >= 0 and yr_return <= 10:
        year_name = data.at[n, 'date']
        group7.append(year_name)
    elif yr_return >= 10 and yr_return <= 20:
        year_name = data.at[n, 'date']
        group8.append(year_name)
    elif yr_return >= 20 and yr_return <= 30:
        year_name = data.at[n, 'date']
        group9.append(year_name)
    elif yr_return >= 30 and yr_return <= 40:
        year_name = data.at[n, 'date']
        group10.append(year_name)
    elif yr_return >= 40 and yr_return <= 50:
        year_name = data.at[n, 'date']
        group11.append(year_name)
    elif yr_return >= 50 and yr_return <= 60:
        year_name = data.at[n, 'date']
        group12.append(year_name)
    elif yr_return >= 60 and yr_return <= 70:
        year_name = data.at[n, 'date']
        group13.append(year_name)

# draw the plot

xbins = np.linspace(-60, 70, 14)
plt.xticks(xbins,
           ('-60%', '-50%', '-40%', '-30%', '-20%', '-10%', '0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%'))
ybins = np.linspace(1, 26, 26)
plt.yticks(ybins, ('1 (1.0%)', '2 (2.0%)', '3 (3.0%)', '4 (4.0%)', '5 (5.0%)', '6 (6.0%)', '7 (7.0%)',
                   '8 (8.0%)', '9 (9.0%)', '10 (10.0%)', '11 (11.0%)', '12 (12.0%)', '13 (13.0%)', '14 (14.0%)',
                   '15 (15.0%)', '16 (16.0%)', '17 (17.0%)', '18 (18.0%)', '19 (19.0%)', '20 (20.0%)', '21 (21.0%)',
                   '22 (22.0%)', '23 (23.0%)', '24 (24.0%)', '25 (25.0%)', '26 (26.0%)'))

plt.xlabel = ("Returns DJIA in %")
plt.ylabel = ('Number of Observations(Probability in %)')
plt.title('Dow Jones Industrial Average 1920 to 2019')

n, bins, patches = plt.hist(year_return, xbins, color='#0504aa', alpha=0.75)

# tag year labels

groups = [group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12, group13]

for i in range(len(groups)):
    for n, year in enumerate(groups[i]):
        plt.text(-60 + 10 * i, n, str(year), color='white')
        plt.text(-20,10,'2020',color='red')

plt.grid(True)

# add the stat summary textbox

#calculate
pos=len(list(filter(lambda x: (x >= 0), year_return)))
neg=len(list(filter(lambda x: (x < 0), year_return)))
mean= round(statistics.mean(year_return),1)
results_list = sorted(year_return)
mini=results_list[0]
quar25= round(np.quantile(year_return, .25),1)
quar50= round(np.quantile(year_return, .5),1)
quar75= round(np.quantile(year_return, .75),1)
maxm=results_list[-1]
sta_dev=round(np.std(year_return),1)
skewness=round(skew(year_return),1)
kurto=round(kurtosis(year_return),1)

ss=[pos,neg,mean,mini,quar25,quar50,quar75,maxm,sta_dev,skewness,kurto]

text = 'Time period:' + '1921-2019'\
       '\nIndex:' + 'DJIA'\
       '\nNumber of years:'+ '99' \
       '\nNumber of pos. years:'  + '69'\
       '\nNumber of neg. years:' + '30'\
       '\nMean:' + '81%' \
       '\nMinimum:' + '-52.7%'\
       '\n25%-Quartile:' + '-3.3%' \
       '\n50%-Quartile: 9.7%'\
       '\n75%-Quartile:20.5%' \
       '\nMaximum:69.3%'\
       '\nStandard dev:19.4%' \
       '\nSkewness:-21.0%'\
       '\nKurtosis:3.92'\


plt.text(-60, 15, str(text), size=5, bbox=dict(fc="none"), multialignment="left")

plt.show()
