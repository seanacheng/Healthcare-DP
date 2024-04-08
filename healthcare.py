import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('h236.csv')

# print(df.info()) 


def get_diagnosis_by_race():
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

    # Numbers of pairs of bars you want
    N = 4
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
    plt.show()

def get_affordability_by_race():
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

    # Numbers of pairs of bars you want
    N = 4
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
    plt.show()

def get_discrimination_by_race():
    filtered_df = df[(df['SDDSCRMDR7'] == 1)]
    hispanic_hlthcr = len(filtered_df.loc[df['RACETHX'] == 1, 'SDDSCRMDR7'])
    white_hlthcr = len(filtered_df.loc[df['RACETHX'] == 2, 'SDDSCRMDR7'])
    black_hlthcr = len(filtered_df.loc[df['RACETHX'] == 3, 'SDDSCRMDR7'])
    asian_hlthcr = len(filtered_df.loc[df['RACETHX'] == 4, 'SDDSCRMDR7'])
    filtered_df = df[(df['SDDSCRMPOL7'] == 1)]
    hispanic_police = len(filtered_df.loc[df['RACETHX'] == 1, 'SDDSCRMPOL7'])
    white_police = len(filtered_df.loc[df['RACETHX'] == 2, 'SDDSCRMPOL7'])
    black_police = len(filtered_df.loc[df['RACETHX'] == 3, 'SDDSCRMPOL7'])
    asian_police = len(filtered_df.loc[df['RACETHX'] == 4, 'SDDSCRMPOL7'])
    filtered_df = df[(df['SDDSCRMJOB7'] == 1)]
    hispanic_jbsrch = len(filtered_df.loc[df['RACETHX'] == 1, 'SDDSCRMJOB7'])
    white_jbsrch = len(filtered_df.loc[df['RACETHX'] == 2, 'SDDSCRMJOB7'])
    black_jbsrch = len(filtered_df.loc[df['RACETHX'] == 3, 'SDDSCRMJOB7'])
    asian_jbsrch = len(filtered_df.loc[df['RACETHX'] == 4, 'SDDSCRMJOB7'])
    filtered_df = df[(df['SDDSCRMWRK7'] == 1)]
    hispanic_work = len(filtered_df.loc[df['RACETHX'] == 1, 'SDDSCRMWRK7'])
    white_work = len(filtered_df.loc[df['RACETHX'] == 2, 'SDDSCRMWRK7'])
    black_work = len(filtered_df.loc[df['RACETHX'] == 3, 'SDDSCRMWRK7'])
    asian_work = len(filtered_df.loc[df['RACETHX'] == 4, 'SDDSCRMWRK7'])

    # Specify the values of blue bars (height)
    blue_bar = (hispanic_hlthcr, white_hlthcr, black_hlthcr, asian_hlthcr)
    # Specify the values of orange bars (height)
    orange_bar = (hispanic_police, white_police, black_police, asian_police)
    # Specify the values of green bars (height)
    green_bar = (hispanic_jbsrch, white_jbsrch, black_jbsrch, asian_jbsrch)
    # Specify the values of green bars (height)
    red_bar = (hispanic_work, white_work, black_work, asian_work)

    # Numbers of pairs of bars you want
    N = 4
    # Position of bars on x-axis
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(10,10))
    plt.subplot(211)

    # Width of a bar 
    width = 0.2

    # Plotting
    plt.bar(ind, blue_bar, width, label='Discrimination in healthcare')
    plt.bar(ind + width, orange_bar, width, label='Discrimination by police')
    plt.bar(ind + (width * 2), green_bar, width, label='Discrimination in job applications')
    plt.bar(ind + (width * 3), red_bar, width, label='Discrimination at work')
    for i, value in enumerate(blue_bar):
        plt.text(i, value + 0.5, str(value), ha='center', va='bottom')
    for i, value in enumerate(orange_bar):
        plt.text(i + width, value + 0.5, str(value), ha='center', va='bottom')
    for i, value in enumerate(green_bar):
        plt.text(i + (width * 2), value + 0.5, str(value), ha='center', va='bottom')
    for i, value in enumerate(red_bar):
        plt.text(i + (width * 3), value + 0.5, str(value), ha='center', va='bottom')

    plt.xlabel('Race')
    plt.ylabel('Population')
    plt.title('Discrimination by race')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + (width * 3) / 2, ('Hispanic', 'White', 'Black', 'Asian'))

    # Finding the best position for legends and putting it
    plt.legend(loc='best')


    # Specify the values of blue bars (height)
    noisy_blue_bar = (round(np.random.laplace(loc=hispanic_hlthcr, scale=1)), round(np.random.laplace(loc=white_hlthcr, scale=1)), round(np.random.laplace(loc=black_hlthcr, scale=1)), round(np.random.laplace(loc=asian_hlthcr, scale=1)))
    # Specify the values of orange bars (height)
    noisy_orange_bar = (round(np.random.laplace(loc=hispanic_police, scale=1)), round(np.random.laplace(loc=white_police, scale=1)), round(np.random.laplace(loc=black_police, scale=1)), round(np.random.laplace(loc=asian_police, scale=1)))
    # Specify the values of green bars (height)
    noisy_green_bar = (round(np.random.laplace(loc=hispanic_jbsrch, scale=1)), round(np.random.laplace(loc=white_jbsrch, scale=1)), round(np.random.laplace(loc=black_jbsrch, scale=1)), round(np.random.laplace(loc=asian_jbsrch, scale=1)))
    # Specify the values of purple bars (height)
    noisy_red_bar = (round(np.random.laplace(loc=hispanic_work, scale=1)), round(np.random.laplace(loc=white_work, scale=1)), round(np.random.laplace(loc=black_work, scale=1)), round(np.random.laplace(loc=asian_work, scale=1)))
    
    plt.subplot(212)   

    # Plotting
    plt.bar(ind, noisy_blue_bar, width, label='Discrimination in healthcare')
    plt.bar(ind + width, noisy_orange_bar, width, label='Discrimination by police')
    plt.bar(ind + (width * 2), noisy_green_bar, width, label='Discrimination in job applications')
    plt.bar(ind + (width * 3), noisy_red_bar, width, label='Discrimination at work')
    for i, value in enumerate(noisy_blue_bar):
        plt.text(i, value + 0.5, str(value), ha='center', va='bottom')
    for i, value in enumerate(noisy_orange_bar):
        plt.text(i + width, value + 0.5, str(value), ha='center', va='bottom')
    for i, value in enumerate(noisy_green_bar):
        plt.text(i + (width * 2), value + 0.5, str(value), ha='center', va='bottom')
    for i, value in enumerate(noisy_red_bar):
        plt.text(i + (width * 3), value + 0.5, str(value), ha='center', va='bottom')

    plt.xlabel('Race')
    plt.ylabel('Population')
    plt.title('Discrimination by race with DP (ε = 1)')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + (width * 3) / 2, ('Hispanic', 'White', 'Black', 'Asian'))

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    plt.subplots_adjust(hspace=0.3)
    plt.show()

def get_uninsured():
    filtered_df = df[(df['UNINSY1'] == 1)]
    usaborn_english_unins = len(filtered_df.loc[(df['BORNUSA'] == 1) & (df['OTHLGSPK'] == 2), 'UNINSY1'])
    usaborn_nonenglish_unins = len(filtered_df.loc[(df['BORNUSA'] == 1) & (df['OTHLGSPK'] == 1), 'UNINSY1'])
    nonusaborn_english_unins = len(filtered_df.loc[(df['BORNUSA'] == 2) & (df['OTHLGSPK'] == 2), 'UNINSY1'])
    nonusaborn_nonenglish_unins = len(filtered_df.loc[(df['BORNUSA'] == 2) & df['OTHLGSPK'] == 1, 'UNINSY1'])

    # Specify the values of blue bars (height)
    blue_bar = (usaborn_english_unins, usaborn_nonenglish_unins, nonusaborn_english_unins, nonusaborn_nonenglish_unins)

    # Position of bars on x-axis
    N = 4
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(10,10))
    plt.subplot(211)

    # Width of a bar 
    width = 0.3       

    # Plotting
    plt.bar(ind, blue_bar, width)
    for i, value in enumerate(blue_bar):
        plt.text(i, value + 0.5, str(value), ha='center', va='bottom')

    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.title('Uninsured by USA born and English spoken at home')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind, ('USA & English', 'USA & not English', 'non USA & English', 'non USA & not English'))

    # Finding the best position for legends and putting it
    # plt.legend(loc='best')


    # Specify the values of blue bars (height)
    noisy_blue_bar = (round(np.random.laplace(loc=usaborn_english_unins, scale=2)), round(np.random.laplace(loc=usaborn_nonenglish_unins, scale=2)), round(np.random.laplace(loc=nonusaborn_english_unins, scale=2)), round(np.random.laplace(loc=nonusaborn_nonenglish_unins, scale=2)))

    plt.subplot(212)   

    # Plotting
    plt.bar(ind, noisy_blue_bar, width)
    for i, value in enumerate(noisy_blue_bar):
        plt.text(i, value + 0.5, str(value), ha='center', va='bottom')


    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.title('Uninsured by USA born and English spoken at home with DP (ε = .5)')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind, ('USA & English', 'USA & not English', 'non USA & English', 'non USA & not English'))

    # Finding the best position for legends and putting it
    # plt.legend(loc='best')

    plt.subplots_adjust(hspace=0.3)
    plt.show()

def get_insurance_type():
    filtered_df = df[(df['INSCOVY1'] == 1)]
    male_single_priv = len(filtered_df.loc[(df['SEX'] == 1) & (df['SPOUINY1'] == 1), 'INSCOVY1'])
    female_single_priv = len(filtered_df.loc[(df['SEX'] == 2) & (df['SPOUINY1'] == 1), 'INSCOVY1'])
    male_married_priv = len(filtered_df.loc[(df['SEX'] == 1) & (df['SPOUINY1'] == 2), 'INSCOVY1'])
    female_married_priv = len(filtered_df.loc[(df['SEX'] == 2) & (df['SPOUINY1'] == 2), 'INSCOVY1'])
    filtered_df = df[(df['INSCOVY1'] == 2)]
    male_single_publ = len(filtered_df.loc[(df['SEX'] == 1) & (df['SPOUINY1'] == 1), 'INSCOVY1'])
    female_single_publ = len(filtered_df.loc[(df['SEX'] == 2) & df['SPOUINY1'] == 1, 'INSCOVY1'])
    male_married_publ = len(filtered_df.loc[(df['SEX'] == 1) & (df['SPOUINY1'] == 2), 'INSCOVY1'])
    female_married_publ = len(filtered_df.loc[(df['SEX'] == 2) & (df['SPOUINY1'] == 2), 'INSCOVY1'])

    # Specify the values of blue bars (height)
    blue_bar = (male_single_priv, female_single_priv, male_married_priv, female_married_priv)
    orange_bar = (male_single_publ, female_single_publ, male_married_publ, female_married_publ)

    # Position of bars on x-axis
    N = 4
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(10,10))
    plt.subplot(211)

    # Width of a bar 
    width = 0.3       

    # Plotting
    plt.bar(ind, blue_bar, width, label='private insurance')
    plt.bar(ind + width, orange_bar, width, label='public insurance')
    for i, value in enumerate(blue_bar):
        plt.text(i, value + 0.5, str(value), ha='center', va='bottom')
    for i, value in enumerate(orange_bar):
        plt.text(i + width, value + 0.5, str(value), ha='center', va='bottom')

    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.title('Insurance type by gender and marital status')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('single male', 'single female', 'married male', 'married female'))

    # Finding the best position for legends and putting it
    plt.legend(loc='best')


    # Specify the values of blue bars (height)
    noisy_blue_bar = (round(np.random.laplace(loc=male_single_priv, scale=1)), round(np.random.laplace(loc=female_single_priv, scale=1)), round(np.random.laplace(loc=male_married_priv, scale=1)), round(np.random.laplace(loc=female_married_priv, scale=1)))
    # Specify the values of orange bars (height)
    noisy_orange_bar = (round(np.random.laplace(loc=male_single_publ, scale=1)), round(np.random.laplace(loc=female_single_publ, scale=1)), round(np.random.laplace(loc=male_married_publ, scale=1)), round(np.random.laplace(loc=female_married_publ, scale=1)))

    plt.subplot(212)   

    # Plotting
    plt.bar(ind, noisy_blue_bar, width, label='private insurance')
    plt.bar(ind + width, noisy_orange_bar, width, label='public insurance')
    for i, value in enumerate(noisy_blue_bar):
        plt.text(i, value + 0.5, str(value), ha='center', va='bottom')
    for i, value in enumerate(noisy_orange_bar):
        plt.text(i + width, value + 0.5, str(value), ha='center', va='bottom')


    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.title('Insurance type by gender and marital status with DP (ε = 1)')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('single male', 'single female', 'married male', 'married female'))

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    plt.subplots_adjust(hspace=0.3)
    plt.show()

if __name__ == "__main__":
    get_diagnosis_by_race()
    get_affordability_by_race()
    get_discrimination_by_race()
    get_uninsured()
    get_insurance_type()
