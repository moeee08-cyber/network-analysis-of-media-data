import pandas as pd
import numpy as np

def create_correlation_matrix(input_file):
    df = pd.read_excel(input_file)
    
    # Print first few rows to inspect data
    print("First few rows:")
    print(df.head())
    
    # Replace non-numeric values with 0
    df = df.apply(pd.to_numeric, errors='coerce').fillna(0)
    
    countries = ['Australia', 'Austria',
       'Belgium', 'Canada', 'China', 'Egypt', 'Ireland', 'Finland', 'France',
       'Ghana', 'Germany', 'Greece', 'Haiti', 'Hungary', 'Indonesia', 'India',
       'Iran', 'Italy', 'Iraq', 'Japan', 'Kenya', 'South Korea', 'Mexico',
       'Malaysia', 'Nigeria', 'Netherlands', 'New Zealand', 'Pakistan',
       'Poland', 'Philippines', 'Russia', 'Rwanda', 'Saudi Arabia',
       'South Africa', 'Singapore', 'Spain', 'Sweden', 'Thailand', 'Turkey',
       'United Kingdom', 'United States', 'Vietnam', 'Zambia']


    matrix = pd.DataFrame(0, index=countries, columns=countries)
    
    for idx in range(len(df)):
        row = df.iloc[idx]
        for i, cat1 in enumerate(countries):
            for j, cat2 in enumerate(countries):
                if row.iloc[i+16] == 1 and row.iloc[j+16] == 1:
                    matrix.loc[cat1, cat2] += 1
        if idx == 0 or idx == len(df):
            print(matrix)

                        
    return matrix


# Usage
matrix = create_correlation_matrix('/Users/wumengmeng/Desktop/project-MediaAgenda/two-mode/step1testcode/step2_code_data/exploratory analysis/canada_code0105.xlsx')
matrix.to_excel('canada_ccorrelation_matrix_0105.xlsx')
