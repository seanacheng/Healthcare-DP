import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from healthcarePlots import *

df = pd.read_csv('h236.csv')

runtime_list = []
same_runtime_list = []

variance = (2 / (.75**2))

# Query 1
start_time = time.time()
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
            
actual_values = (hispanic_diab, white_diab, black_diab, asian_diab, hispanic_canc, white_canc, black_canc, asian_canc)
noisy_values = (round(np.random.laplace(loc=hispanic_diab, scale=variance)),
                round(np.random.laplace(loc=white_diab, scale=variance)), 
                round(np.random.laplace(loc=black_diab, scale=variance)), 
                round(np.random.laplace(loc=asian_diab, scale=variance)), 
                round(np.random.laplace(loc=hispanic_canc, scale=variance)), 
                round(np.random.laplace(loc=white_canc, scale=variance)), 
                round(np.random.laplace(loc=black_canc, scale=variance)), 
                round(np.random.laplace(loc=asian_canc, scale=variance)))
    
end_time = time.time()
true_runtime = end_time - start_time
time.sleep(2-true_runtime)
same_runtime = time.time() - start_time
runtime_list.append(true_runtime)
same_runtime_list.append(same_runtime)
print("Query 1 count: " + str(sum(actual_values)))

# Query 2
start_time = time.time()
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
            
actual_values = (hispanic_med, white_med, black_med, asian_med, hispanic_den, white_den, black_den, asian_den, hispanic_pmed, white_pmed, black_pmed, asian_pmed)
noisy_values = (round(np.random.laplace(loc=hispanic_med, scale=variance)), 
                round(np.random.laplace(loc=white_med, scale=variance)), 
                round(np.random.laplace(loc=black_med, scale=variance)), 
                round(np.random.laplace(loc=asian_med, scale=variance)),
                round(np.random.laplace(loc=hispanic_den, scale=variance)), 
                round(np.random.laplace(loc=white_den, scale=variance)), 
                round(np.random.laplace(loc=black_den, scale=variance)), 
                round(np.random.laplace(loc=asian_den, scale=variance)),
                round(np.random.laplace(loc=hispanic_pmed, scale=variance)), 
                round(np.random.laplace(loc=white_pmed, scale=variance)), 
                round(np.random.laplace(loc=black_pmed, scale=variance)), 
                round(np.random.laplace(loc=asian_pmed, scale=variance)))

end_time = time.time()
true_runtime = end_time - start_time
time.sleep(2-true_runtime)
same_runtime = time.time() - start_time
runtime_list.append(true_runtime)
same_runtime_list.append(same_runtime)
print("Query 2 count: " + str(sum(actual_values)))

# Query 3
start_time = time.time()
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

actual_values = (hispanic_hlthcr, white_hlthcr, black_hlthcr, asian_hlthcr, 
                hispanic_police, white_police, black_police, asian_police,
                hispanic_jbsrch, white_jbsrch, black_jbsrch, asian_jbsrch,
                hispanic_work, white_work, black_work, asian_work)
noisy_values = (round(np.random.laplace(loc=hispanic_hlthcr, scale=variance)), 
                round(np.random.laplace(loc=white_hlthcr, scale=variance)), 
                round(np.random.laplace(loc=black_hlthcr, scale=variance)), 
                round(np.random.laplace(loc=asian_hlthcr, scale=variance)),
                round(np.random.laplace(loc=hispanic_police, scale=variance)), 
                round(np.random.laplace(loc=white_police, scale=variance)), 
                round(np.random.laplace(loc=black_police, scale=variance)), 
                round(np.random.laplace(loc=asian_police, scale=variance)),
                round(np.random.laplace(loc=hispanic_jbsrch, scale=variance)), 
                round(np.random.laplace(loc=white_jbsrch, scale=variance)), 
                round(np.random.laplace(loc=black_jbsrch, scale=variance)), 
                round(np.random.laplace(loc=asian_jbsrch, scale=variance)),
                round(np.random.laplace(loc=hispanic_work, scale=variance)), 
                round(np.random.laplace(loc=white_work, scale=variance)), 
                round(np.random.laplace(loc=black_work, scale=variance)), 
                round(np.random.laplace(loc=asian_work, scale=variance)))
    
end_time = time.time()
true_runtime = end_time - start_time
time.sleep(2-true_runtime)
same_runtime = time.time() - start_time
runtime_list.append(true_runtime)
same_runtime_list.append(same_runtime)
print("Query 3 count: " + str(sum(actual_values)))

# Query 4
start_time = time.time()

filtered_df = df[(df['UNINSY1'] == 1)]
usaborn_english_unins = len(filtered_df.loc[(df['BORNUSA'] == 1) & (df['OTHLGSPK'] == 2), 'UNINSY1'])
usaborn_nonenglish_unins = len(filtered_df.loc[(df['BORNUSA'] == 1) & (df['OTHLGSPK'] == 1), 'UNINSY1'])
nonusaborn_english_unins = len(filtered_df.loc[(df['BORNUSA'] == 2) & (df['OTHLGSPK'] == 2), 'UNINSY1'])
nonusaborn_nonenglish_unins = len(filtered_df.loc[(df['BORNUSA'] == 2) & df['OTHLGSPK'] == 1, 'UNINSY1'])

actual_values = (usaborn_english_unins, usaborn_nonenglish_unins, nonusaborn_english_unins, nonusaborn_nonenglish_unins)
noisy_values = (round(np.random.laplace(loc=usaborn_english_unins, scale=variance)), round(np.random.laplace(loc=usaborn_nonenglish_unins, scale=variance)), round(np.random.laplace(loc=nonusaborn_english_unins, scale=variance)), round(np.random.laplace(loc=nonusaborn_nonenglish_unins, scale=variance)))

end_time = time.time()
true_runtime = end_time - start_time
time.sleep(2-true_runtime)
same_runtime = time.time() - start_time
runtime_list.append(true_runtime)
same_runtime_list.append(same_runtime)
print("Query 4 count: " + str(sum(actual_values)))

# Query 5
start_time = time.time()

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

actual_values = (male_single_priv, female_single_priv, male_married_priv, female_married_priv,
                male_single_publ, female_single_publ, male_married_publ, female_married_publ)
noisy_values = (round(np.random.laplace(loc=male_single_priv, scale=variance)), 
                round(np.random.laplace(loc=female_single_priv, scale=variance)), 
                round(np.random.laplace(loc=male_married_priv, scale=variance)), 
                round(np.random.laplace(loc=female_married_priv, scale=variance)),
                round(np.random.laplace(loc=male_single_publ, scale=variance)), 
                round(np.random.laplace(loc=female_single_publ, scale=variance)), 
                round(np.random.laplace(loc=male_married_publ, scale=variance)), 
                round(np.random.laplace(loc=female_married_publ, scale=variance)))

end_time = time.time()
true_runtime = end_time - start_time
time.sleep(2-true_runtime)
same_runtime = time.time() - start_time
runtime_list.append(true_runtime)
same_runtime_list.append(same_runtime)
print("Query 5 count: " + str(sum(actual_values)))

plt.scatter(np.arange(5), runtime_list, color='red', label='true value')
plt.scatter(np.arange(5), same_runtime_list, color='blue', label='leakage prevention value')

plt.xticks(np.arange(5), ('Query 1', 'Query 2', 'Query 3', 'Query 4', 'Query 5'))
plt.ylabel('Runtime')
plt.title('Timing attack prevention')
plt.legend()
plt.show()
