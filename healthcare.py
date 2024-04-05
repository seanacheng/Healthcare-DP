import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('h236.csv')

# print(df.info()) 

selected_columns = ['DIABDXY1_M18', 'CANCERY1', 'RACETHX']
correlation_matrix = df[selected_columns].corr()
# Get unique categories
unique_categories = df['RACETHX'].unique()

# Numbers of pairs of bars you want
N = 4

# Data on X-axis
filtered_df = df[(df['DIABDXY1_M18'] == 1)]
hispanic_diab = len(filtered_df.loc[df['RACETHX'] == 1, 'DIABDXY1_M18'])
white_diab = len(filtered_df.loc[df['RACETHX'] == 2, 'DIABDXY1_M18'])
black_diab = len(filtered_df.loc[df['RACETHX'] == 3, 'DIABDXY1_M18'])
asian_diab = len(filtered_df.loc[df['RACETHX'] == 4, 'DIABDXY1_M18'])
filtered_df = df[(df['CANCERY1'] == 1)]
hispanic_canc = len(filtered_df.loc[df['RACETHX'] == 1, 'CANCERY1'])
white_canc = len(filtered_df.loc[df['RACETHX'] == 2, 'CANCERY1'])
black_canc = len(filtered_df.loc[df['RACETHX'] == 3, 'CANCERY1'])
asian_canc = len(filtered_df.loc[df['RACETHX'] == 4, 'CANCERY1'])

# Specify the values of blue bars (height)
blue_bar = (hispanic_diab, white_diab, black_diab, asian_diab)
# Specify the values of orange bars (height)
orange_bar = (hispanic_canc, white_canc, black_canc, asian_canc)

# Position of bars on x-axis
ind = np.arange(N)

# Figure size
plt.figure(figsize=(10,10))
plt.subplot(211)

# Width of a bar 
width = 0.3       

# Plotting
plt.bar(ind, blue_bar, width, label='Diabetes diagnosis')
plt.bar(ind + width, orange_bar, width, label='Cancer diagnosis')
for i, value in enumerate(blue_bar):
    plt.text(i, value + 0.5, str(value), ha='center', va='bottom')
for i, value in enumerate(orange_bar):
    plt.text(i + width, value + 0.5, str(value), ha='center', va='bottom')

plt.xlabel('Race')
plt.ylabel('Population')
plt.title('Diagnosis\' by race')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width / 2, ('Hispanic', 'White', 'Black', 'Asian'))

# Finding the best position for legends and putting it
plt.legend(loc='best')


# Specify the values of blue bars (height)
noisy_blue_bar = (round(np.random.laplace(loc=hispanic_diab, scale=1)), round(np.random.laplace(loc=white_diab, scale=1)), round(np.random.laplace(loc=black_diab, scale=1)), round(np.random.laplace(loc=asian_diab, scale=1)))
# Specify the values of orange bars (height)
noisy_orange_bar = (round(np.random.laplace(loc=hispanic_canc, scale=1)), round(np.random.laplace(loc=white_canc, scale=1)), round(np.random.laplace(loc=black_canc, scale=1)), round(np.random.laplace(loc=asian_canc, scale=1)))

plt.subplot(212)   

# Plotting
plt.bar(ind, noisy_blue_bar, width, label='Diabetes diagnosis')
plt.bar(ind + width, noisy_orange_bar, width, label='Cancer diagnosis')
for i, value in enumerate(noisy_blue_bar):
    plt.text(i, value + 0.5, str(value), ha='center', va='bottom')
for i, value in enumerate(noisy_orange_bar):
    plt.text(i + width, value + 0.5, str(value), ha='center', va='bottom')

plt.xlabel('Race')
plt.ylabel('Population')
plt.title('Diagnosis\' by race with DP (ε = 1)')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width / 2, ('Hispanic', 'White', 'Black', 'Asian'))

# Finding the best position for legends and putting it
plt.legend(loc='best')

plt.subplots_adjust(hspace=0.3)
# plt.show()


filtered_df = df[(df['AFRDCA2'] == 1)]
hispanic_med = len(filtered_df.loc[df['RACETHX'] == 1, 'AFRDCA2'])
white_med = len(filtered_df.loc[df['RACETHX'] == 2, 'AFRDCA2'])
black_med = len(filtered_df.loc[df['RACETHX'] == 3, 'AFRDCA2'])
asian_med = len(filtered_df.loc[df['RACETHX'] == 4, 'AFRDCA2'])
filtered_df = df[(df['AFRDDN2'] == 1)]
hispanic_den = len(filtered_df.loc[df['RACETHX'] == 1, 'AFRDDN2'])
white_den = len(filtered_df.loc[df['RACETHX'] == 2, 'AFRDDN2'])
black_den = len(filtered_df.loc[df['RACETHX'] == 3, 'AFRDDN2'])
asian_den = len(filtered_df.loc[df['RACETHX'] == 4, 'AFRDDN2'])
filtered_df = df[(df['AFRDPM2'] == 1)]
hispanic_pmed = len(filtered_df.loc[df['RACETHX'] == 1, 'AFRDPM2'])
white_pmed = len(filtered_df.loc[df['RACETHX'] == 2, 'AFRDPM2'])
black_pmed = len(filtered_df.loc[df['RACETHX'] == 3, 'AFRDPM2'])
asian_pmed = len(filtered_df.loc[df['RACETHX'] == 4, 'AFRDPM2'])

# Specify the values of blue bars (height)
blue_bar = (hispanic_med, white_med, black_med, asian_med)
# Specify the values of orange bars (height)
orange_bar = (hispanic_den, white_den, black_den, asian_den)
# Specify the values of green bars (height)
green_bar = (hispanic_pmed, white_pmed, black_pmed, asian_pmed)

# Position of bars on x-axis
ind = np.arange(N)

# Figure size
plt.figure(figsize=(10,10))
plt.subplot(211)

# Width of a bar 
width = 0.3       

# Plotting
plt.bar(ind, blue_bar, width, label='Could not afford medical care')
plt.bar(ind + width, orange_bar, width, label='Could not afford dental care')
plt.bar(ind + (width * 2), green_bar, width, label='Could not afford prescription care')
for i, value in enumerate(blue_bar):
    plt.text(i, value + 0.5, str(value), ha='center', va='bottom')
for i, value in enumerate(orange_bar):
    plt.text(i + width, value + 0.5, str(value), ha='center', va='bottom')
for i, value in enumerate(green_bar):
    plt.text(i + (width * 2), value + 0.5, str(value), ha='center', va='bottom')

plt.xlabel('Race')
plt.ylabel('Population')
plt.title('Health care affordability by race')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width, ('Hispanic', 'White', 'Black', 'Asian'))

# Finding the best position for legends and putting it
plt.legend(loc='best')


# Specify the values of blue bars (height)
noisy_blue_bar = (round(np.random.laplace(loc=hispanic_med, scale=2)), round(np.random.laplace(loc=white_med, scale=2)), round(np.random.laplace(loc=black_med, scale=2)), round(np.random.laplace(loc=asian_med, scale=2)))
# Specify the values of orange bars (height)
noisy_orange_bar = (round(np.random.laplace(loc=hispanic_den, scale=2)), round(np.random.laplace(loc=white_den, scale=2)), round(np.random.laplace(loc=black_den, scale=2)), round(np.random.laplace(loc=asian_den, scale=2)))
# Specify the values of green bars (height)
noisy_green_bar = (round(np.random.laplace(loc=hispanic_pmed, scale=2)), round(np.random.laplace(loc=white_pmed, scale=2)), round(np.random.laplace(loc=black_pmed, scale=2)), round(np.random.laplace(loc=asian_pmed, scale=2)))

plt.subplot(212)   

# Plotting
plt.bar(ind, noisy_blue_bar, width, label='Could not afford medical care')
plt.bar(ind + width, noisy_orange_bar, width, label='Could not afford dental care')
plt.bar(ind + (width * 2), noisy_green_bar, width, label='Could not afford prescription care')
for i, value in enumerate(noisy_blue_bar):
    plt.text(i, value + 0.5, str(value), ha='center', va='bottom')
for i, value in enumerate(noisy_orange_bar):
    plt.text(i + width, value + 0.5, str(value), ha='center', va='bottom')
for i, value in enumerate(noisy_green_bar):
    plt.text(i + (width * 2), value + 0.5, str(value), ha='center', va='bottom')

plt.xlabel('Race')
plt.ylabel('Population')
plt.title('Health care affordability by race with DP (ε = 0.5)')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width, ('Hispanic', 'White', 'Black', 'Asian'))

# Finding the best position for legends and putting it
plt.legend(loc='best')

plt.subplots_adjust(hspace=0.3)
# plt.show()

# Data on X-axis
filtered_df = df[(df['UNINSY1'] == 1)]
american_unins_y1 = len(filtered_df.loc[df['BORNUSA'] == 1, 'UNINSY1'])
nonamerican_unins_y1 = len(filtered_df.loc[df['BORNUSA'] == 2, 'UNINSY1'])
filtered_df = df[(df['UNINSY2'] == 1)]
american_unins_y2 = len(filtered_df.loc[df['BORNUSA'] == 1, 'UNINSY2'])
nonamerican_unins_y2 = len(filtered_df.loc[df['BORNUSA'] == 2, 'UNINSY2'])
filtered_df = df[(df['UNINSY3'] == 1)]
american_unins_y3 = len(filtered_df.loc[df['BORNUSA'] == 1, 'UNINSY3'])
nonamerican_unins_y3 = len(filtered_df.loc[df['BORNUSA'] == 2, 'UNINSY3'])
filtered_df = df[(df['UNINSY4'] == 1)]
american_unins_y4 = len(filtered_df.loc[df['BORNUSA'] == 1, 'UNINSY4'])
nonamerican_unins_y4 = len(filtered_df.loc[df['BORNUSA'] == 2, 'UNINSY4'])

# Specify the values of blue bars (height)
blue_bar = (american_unins_y1, american_unins_y2, american_unins_y3, american_unins_y4)
# Specify the values of orange bars (height)
orange_bar = (nonamerican_unins_y1, nonamerican_unins_y2, nonamerican_unins_y3, nonamerican_unins_y4)

# Position of bars on x-axis
ind = np.arange(N)

# Figure size
plt.figure(figsize=(10,10))
plt.subplot(211)

# Width of a bar 
width = 0.3       

# Plotting
plt.bar(ind, blue_bar, width, label='Born in US')
plt.bar(ind + width, orange_bar, width, label='Born outside US')
for i, value in enumerate(blue_bar):
    plt.text(i, value + 0.5, str(value), ha='center', va='bottom')
for i, value in enumerate(orange_bar):
    plt.text(i + width, value + 0.5, str(value), ha='center', va='bottom')

plt.xlabel('Years')
plt.ylabel('Population')
plt.title('Uninsured by country of birth')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width / 2, ('2018', '2019', '2020', '2021'))

# Finding the best position for legends and putting it
plt.legend(loc='best')


# Specify the values of blue bars (height)
noisy_blue_bar = (round(np.random.laplace(loc=american_unins_y1, scale=1)), round(np.random.laplace(loc=american_unins_y2, scale=1)), round(np.random.laplace(loc=american_unins_y3, scale=1)), round(np.random.laplace(loc=american_unins_y4, scale=1)))
# Specify the values of orange bars (height)
noisy_orange_bar = (round(np.random.laplace(loc=nonamerican_unins_y1, scale=1)), round(np.random.laplace(loc=nonamerican_unins_y2, scale=1)), round(np.random.laplace(loc=nonamerican_unins_y3, scale=1)), round(np.random.laplace(loc=nonamerican_unins_y4, scale=1)))

plt.subplot(212)   

# Plotting
plt.bar(ind, noisy_blue_bar, width, label='Born in US')
plt.bar(ind + width, noisy_orange_bar, width, label='Born outside US')
for i, value in enumerate(noisy_blue_bar):
    plt.text(i, value + 0.5, str(value), ha='center', va='bottom')
for i, value in enumerate(noisy_orange_bar):
    plt.text(i + width, value + 0.5, str(value), ha='center', va='bottom')


plt.xlabel('Years')
plt.ylabel('Population')
plt.title('Uninsured by country of birth with DP (ε = 1)')

# xticks()
# First argument - A list of positions at which ticks should be placed
# Second argument -  A list of labels to place at the given locations
plt.xticks(ind + width / 2, ('2018', '2019', '2020', '2021'))

# Finding the best position for legends and putting it
plt.legend(loc='best')

plt.subplots_adjust(hspace=0.3)
plt.show()