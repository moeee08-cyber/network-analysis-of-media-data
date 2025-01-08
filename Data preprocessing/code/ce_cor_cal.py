import pandas as pd
import numpy as np

def create_correlation_matrix(input_file):
    df = pd.read_excel(input_file)
    
    # Print first few rows to inspect data
    print("First few rows:")
    print(df.head())
    
    # Replace non-numeric values with 0
    df = df.apply(pd.to_numeric, errors='coerce').fillna(0)
    
    rows= ['Australia', 'Austria',
       'Belgium', 'Canada', 'China', 'Egypt', 'Ireland', 'Finland', 'France',
       'Ghana', 'Germany', 'Greece', 'Haiti', 'Hungary', 'Indonesia', 'India',
       'Iran', 'Italy', 'Iraq', 'Japan', 'Kenya', 'South Korea', 'Mexico',
       'Malaysia', 'Nigeria', 'Netherlands', 'New Zealand', 'Pakistan',
       'Poland', 'Philippines', 'Russia', 'Rwanda', 'Saudi Arabia',
       'South Africa', 'Singapore', 'Spain', 'Sweden', 'Thailand', 'Turkey',
       'United Kingdom', 'United States', 'Vietnam', 'Zambia']

    cols = ['economy', 'military&terrorism', 'borderissues', 'healthcare', 
                 'publicorder', 'civil_liberties', 'environment', 'education', 
                 'politics', 'poverty', 'disaster', 'religion', 'infrastructure', 
                 'media/internet']


    matrix = pd.DataFrame(0, index=rows, columns=cols)
    
    for idx in range(len(df)):
        row = df.iloc[idx]
        for i, country in enumerate(rows):    #
               country_val = row.iloc[i + 16]    # +15 because countries start at P (16th column)
               for j, issue in enumerate(cols):   # 14 issues
                    issue_val = row.iloc[j + 2]    # +1 because issues start at B (2nd column)
                
                    if country_val == 1 and issue_val == 1:
                       matrix.loc[country, issue] += 1
        if idx == 0 or idx == len(df):
            print(matrix)

                        
    return matrix


# Usage
matrix = create_correlation_matrix('/Users/wumengmeng/Desktop/project-MediaAgenda/two-mode/step1testcode/step2_code_data/exploratory analysis/canada_code0105.xlsx')
matrix.to_excel('canada_cecorrelation_matrix_0105.xlsx')