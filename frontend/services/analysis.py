
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

region_map = {'CT' : 'NorthEast', 'ME' : 'NorthEast', 'MA' : 'NorthEast', 'NH' : 'NorthEast', 'RI' : 'NorthEast', 'VT' : 'NorthEast', 'NJ' : 'NorthEast', 'NY' : 'NorthEast', 'PA' : 'NorthEast',
              
              'IL' : 'MidWest', 'IN' : 'MidWest', 'MI' : 'MidWest', 'OH' : 'MidWest', 'WI' : 'MidWest', 'IA' : 'MidWest', 'KS' : 'MidWest', 'MN': 'MidWest', 'MO' : 'MidWest', 'NE' : 'MidWest',
              'ND': 'MidWest', 'SD' : 'MidWest',
              
              'DE' : 'South', 'DC' : 'South', 'FL' : 'South', 'GA' : 'South', 'MD' : 'South', 'NC' : 'South', 'SC' : 'South', 'VA' : 'South', 'WV': 'South', 'AL' : 'South', 'KY' : 'South', 'MS' : 'South',
              'TN' : 'South', 'AR' : 'South', 'LA' : 'South', 'OK' : 'South', 'TX' : 'South',
              
              'AZ' : 'West', 'CO' : 'West', 'ID' : 'West', 'MT' : 'West', 'NV' : 'West', 'NM' : 'West', 'UT' : 'West', 'WY' : 'West', 'AK' : 'West', 'CA' : 'West', 'HI': 'West', 'OR' : 'West', 'WA' : 'West' }


success_20 = pd.read_csv('2020SuccessRates.csv')
profile_20 = pd.read_csv('2020Profiles.csv')
cycle_20 = pd.read_csv('2020ARTCycles.csv')

success_21 = pd.read_csv('2021SuccessRates.csv')
profile_21 = pd.read_csv('2021Profiles.csv')
cycle_21 = pd.read_csv('2021Cycles.csv')

success_22 = pd.read_csv('2022SuccessRates.csv')
profile_22 = pd.read_csv('2022Profiles.csv')
cycle_22 = pd.read_csv('2022Cycles.csv')


filtered_summary_success_20 = success_20[success_20['Data_Value_Footnote'].isna() | (success_20['Data_Value_Footnote'] == '')]
summary_success_20 = filtered_summary_success_20.groupby('LocationAbbr')['Data_Value_num'].mean().reset_index()
summary_success_20 = summary_success_20.sort_values(by='LocationAbbr').reset_index(drop = 'True')


filtered_summary_success_21 = success_21[success_21['Data_Value_Footnote'].isna() | (success_21['Data_Value_Footnote'] == '')]
summary_success_21 = filtered_summary_success_21.groupby('LocationAbbr')['Data_Value_num'].mean().reset_index()
summary_success_21 = summary_success_21.sort_values(by='LocationAbbr').reset_index(drop = 'True')


filtered_summary_success_22 = success_22[success_22['Data_Value_Footnote'].isna() | (success_22['Data_Value_Footnote'] == '')]
summary_success_22 = filtered_summary_success_22.groupby('LocationAbbr')['Data_Value_num'].mean().reset_index()
summary_success_22 = summary_success_22.sort_values(by='LocationAbbr').reset_index(drop = 'True')


counts_per_state_20 = filtered_summary_success_20.groupby('LocationAbbr')['Data_Value_num'].count().reset_index(name = 'Count')
counts_per_state_21 = filtered_summary_success_21.groupby('LocationAbbr')['Data_Value_num'].count().reset_index(name = 'Count')
counts_per_state_22 = filtered_summary_success_22.groupby('LocationAbbr')['Data_Value_num'].count().reset_index(name = 'Count')

states_over_10_20 = counts_per_state_20[counts_per_state_20['Count'] > 10]['LocationAbbr']
states_over_10_21 = counts_per_state_21[counts_per_state_21['Count'] > 10]['LocationAbbr']
states_over_10_22 = counts_per_state_22[counts_per_state_22['Count'] > 10]['LocationAbbr']


filtered_over_10_20 = summary_success_20[summary_success_20['LocationAbbr'].isin(states_over_10_20)].reset_index()
filtered_over_10_21 = summary_success_21[summary_success_21['LocationAbbr'].isin(states_over_10_21)].reset_index()
filtered_over_10_22 = summary_success_22[summary_success_22['LocationAbbr'].isin(states_over_10_22)].reset_index()

filtered_over_10_20['Region'] = filtered_over_10_20['LocationAbbr'].map(region_map)
filtered_over_10_21['Region'] = filtered_over_10_21['LocationAbbr'].map(region_map)
filtered_over_10_22['Region'] = filtered_over_10_22['LocationAbbr'].map(region_map)

summary_region_20 = filtered_over_10_20.groupby('Region')['Data_Value_num'].mean().reset_index()
summary_region_21 = filtered_over_10_21.groupby('Region')['Data_Value_num'].mean().reset_index()
summary_region_22 = filtered_over_10_22.groupby('Region')['Data_Value_num'].mean().reset_index()

summary_region_20["Year"] = 2020 
summary_region_21["Year"] = 2021
summary_region_22["Year"] = 2022

region_combined = pd.concat([summary_region_20, summary_region_21, summary_region_22], ignore_index = True)
summary_region_yr = region_combined.groupby(['Region', 'Year'])['Data_Value_num'].mean().reset_index()




#plt.figure(figsize=(10, 6))
#sns.lineplot(data = summary_region_yr, x = 'Year', y = 'Data_Value_num', hue = 'Region')
#plt.title('Mean ART Success Rate by Region (2020-2022)')
#plt.ylabel('Mean Success Rate')
#plt.xticks([2020, 2021, 2022])
#plt.legend(title = 'Region')
#plt.show()


#region_order = sorted(summary_region_20['Region'].unique())
#plt.figure(figsize=(18, 6))
#sns.barplot(data = summary_region_20, x = 'Region', y = 'Data_Value_num', order = region_order)
#plt.title('Distribution of success percentage by Region 2020')
#plt.xlabel('Region')
#plt.ylabel('Mean Success Percentage')
#plt.savefig('reg_suc_20.pdf', bbox_inches = 'tight')
#plt.show()
#plt.figure(figsize=(18, 6))
#sns.barplot(data = summary_region_21, x = 'Region', y = 'Data_Value_num', order = region_order)
#plt.title('Distribution of success percentage by Region 2021')
#plt.xlabel('Region')
#plt.ylabel('Mean Success Percentage')
#plt.savefig('reg_suc_21.pdf', bbox_inches = 'tight')
#plt.show()
#plt.figure(figsize=(18, 6))
#sns.barplot(data = summary_region_22, x = 'Region', y = 'Data_Value_num', order = region_order)
#plt.title('Distribution of success percentage by Region 2022')
#plt.xlabel('Region')
#plt.ylabel('Mean Success Percentage')
#plt.savefig('reg_suc_22.pdf', bbox_inches = 'tight')
#plt.show()


#region_order = sorted(summary_region_20['Region'].unique())
#plt.figure(figsize=(18, 6))
#sns.barplot(data = summary_region_20, x = 'Region', y = 'Data_Value_num', order = region_order)
#plt.title('Distribution of success percentage by Region 2020')
#plt.xlabel('Region')
#plt.ylabel('Mean Success Percentage')
#plt.savefig('reg_suc_20.pdf', bbox_inches = 'tight')
#plt.show()
#plt.figure(figsize=(18, 6))
#sns.barplot(data = summary_region_21, x = 'Region', y = 'Data_Value_num', order = region_order)
#plt.title('Distribution of success percentage by Region 2021')
#plt.xlabel('Region')
#plt.ylabel('Mean Success Percentage')
#plt.savefig('reg_suc_21.pdf', bbox_inches = 'tight')
#plt.show()
#plt.figure(figsize=(18, 6))
#sns.barplot(data = summary_region_22, x = 'Region', y = 'Data_Value_num', order = region_order)
#plt.title('Distribution of success percentage by Region 2022')
#plt.xlabel('Region')
#plt.ylabel('Mean Success Percentage')
#plt.savefig('reg_suc_22.pdf', bbox_inches = 'tight')
#plt.show()

#
#plt.figure(figsize=(18, 6))
#sns.barplot(data = filtered_over_10_20, x = 'LocationAbbr', y = 'Data_Value_num', color = 'skyblue')
#plt.title('Distribution of success percentage by State 2020')
#plt.xlabel('State Abbreviation')
#plt.ylabel('Mean Success Percentage')
#plt.savefig
#plt.show()

#plt.figure(figsize=(18, 6))
#sns.barplot(data = filtered_over_10_21, x = 'LocationAbbr', y = 'Data_Value_num', color = 'skyblue')
#plt.title('Distirbution of success percentage by State 2021')
#plt.xlabel('State Abbreviation')
#plt.ylabel('Mean Success Percentage')
#plt.show()

#plt.figure(figsize=(18, 6))
#sns.barplot(data = filtered_over_10_22, x = 'LocationAbbr', y = 'Data_Value_num', color = 'skyblue')
#plt.title('Distirbution of success percentage by State 2022')
#plt.xlabel('State Abbreviation')
#plt.ylabel('Mean Success Percentage')
#plt.show()


type_2020 = success_20['Type'].unique()

filtered_20_type = success_20[success_20['Data_Value_Footnote'].isna() | (success_20['Data_Value_Footnote'] == '')]
filtered_20_type = filtered_20_type.groupby(['Type'])['Data_Value_num'].mean().reset_index()
filtered_20_type['Year'] = 2020

filtered_21_type = success_21[success_21['Data_Value_Footnote'].isna() | (success_21['Data_Value_Footnote'] == '')]
filtered_21_type = filtered_21_type.groupby(['Type'])['Data_Value_num'].mean().reset_index()
filtered_21_type['Year'] = 2021


filtered_22_type = success_22[success_22['Data_Value_Footnote'].isna() | (success_22['Data_Value_Footnote'] == '')]
filtered_22_type = filtered_22_type.groupby(['Type'])['Data_Value_num'].mean().reset_index()
filtered_22_type['Year'] = 2022

summary_type = pd.concat([filtered_20_type, filtered_21_type, filtered_22_type], ignore_index= True)
summary_type = summary_type[summary_type['Data_Value_num'].notna()]


#print(type_2020)


#plt.figure(figsize = (10, 6))
#sns.barplot(data = summary_type, x = 'Year', y = 'Data_Value_num', hue ='Type')
#plt.title('Mean ART Success Rate by Type and Year')
#plt.ylabel('Mean Success Rate')
#plt.xlabel('Year')
#plt.legend(title = 'Type')
#plt.show()




fac_name = cycle_20.loc[cycle_20["ClinicId"] == 37, 'FacilityName'].values[0]
#print(fac_name)
fac_name_2 = success_20.loc[success_20["ClinicId"] == 37, 'FacilityName'].values[0]
#print(fac_name_2 == fac_name)

def clinics(df1, df2, id_col = 'ClinicId', name_col='FacilityName'):
    #merge
    merged = df1[[id_col, name_col]].merge(df2[[id_col, name_col]], on = id_col, suffixes = ('_df1', '_df2'), how = 'inner')
    mismatches = merged[merged[f'{name_col}_df1'] != merged[f'{name_col}_df2']]
    if mismatches.empty:
        print('All clinic IDS match')
    else:
        print('Mismatches')
        print(len(mismatches))
    return
#clinics(cycle_20, success_20)
#clinics(cycle_21, success_21)
#clinics(cycle_22, success_22)




excluded = ['What was the average number of transfers per intended egg retrieval?', 
            'What was the average number of intended egg retrievals per new patient?']           


success_20_QF = filtered_summary_success_20[~filtered_summary_success_20["Question"].isin(excluded)].copy()
success_20_QF['Expected # Cycles'] = 1/(success_20_QF['Data_Value_num']/100)

success_21_QF = filtered_summary_success_21[~filtered_summary_success_21["Question"].isin(excluded)].copy()
success_21_QF['Expected # Cycles'] = 1/(success_21_QF['Data_Value_num']/100)

success_22_QF = filtered_summary_success_22[~filtered_summary_success_22["Question"].isin(excluded)].copy()
success_22_QF['Expected # Cycles'] = 1/(success_22_QF['Data_Value_num']/100)

summary_success_all = pd.concat([success_20_QF, success_21_QF, success_22_QF], ignore_index=True)
summary_success_all = summary_success_all[summary_success_all['Data_Value_num'].notna()]
                                          


clean_20 = success_20_QF[
    success_20_QF['Expected # Cycles'].notna() &
    ~success_20_QF['Expected # Cycles'].isin([-np.inf, np.inf])
]
clean_21 = success_21_QF[
    success_21_QF['Expected # Cycles'].notna() &
    ~success_21_QF['Expected # Cycles'].isin([-np.inf, np.inf])]
clean_22 = success_22_QF[
    success_22_QF['Expected # Cycles'].notna() &
    ~success_22_QF['Expected # Cycles'].isin([-np.inf, np.inf])
]

clean_all = pd.concat([clean_20, clean_21, clean_22], ignore_index=True)




def expected_num_cycles(state, attribute, df = clean_all):
    print(state)
    print(attribute)
    state_df = df[df["LocationAbbr"] == state]

    attribute_df = state_df[state_df["Type"] == attribute]

    result = attribute_df["Expected # Cycles"].mean()

    description = "Placeholder description"

    return result, description