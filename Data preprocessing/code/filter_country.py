import os
import csv
import pandas as pd

news_sources = [
    "cbc.ca",
    "nationalpost.com",
    "theglobeandmail.com",
    "vancouversun.com",
    "torontosun.com",
    "montrealgazette.com",
    "cp24.com",
    "castanet.net",
    "globalnews.ca",
    "winnipegfreepress.com"
]

def process_csv_files(input_folder, output_file):
    """
    Process CSV files to extract and filter website information.
    
    Args:
        input_folder (str): Path to folder containing input CSV files
        output_file (str): Path to the output CSV file
    """
    # List to store all matching website entries
    all_matches = []
    
    # Process each CSV file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_folder, filename)
            
            try:
                # Try different encodings
                encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
                df = None
                
                for encoding in encodings:
                    try:
                        df = pd.read_csv(file_path, 
                                       delimiter='\t', 
                                       header=None,
                                       encoding=encoding,
                                       on_bad_lines='skip')  # Skip problematic lines
                        break  # If successful, break the encoding loop
                    except UnicodeDecodeError:
                        continue
                
                if df is None:
                    print(f"Could not read {filename} with any of the attempted encodings")
                    continue
                
                # Check the website column (4th column, index 3)
                website_column = 3
                
                # Filter rows where website contains foxnews.com or usatoday.com
                for i in news_sources:
                    filtered_df = df[df[website_column].str.contains(i, na=False)]
                    
                    # If there are matching entries, add them to the list
                    if not filtered_df.empty:
                        all_matches.append(filtered_df)
                        print(f"Found {len(filtered_df)} matching entries in {filename}")
                    
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
    
    # Combine all matches into a single file
    if all_matches:
        try:
            combined_df = pd.concat(all_matches, ignore_index=True)
            
            # Ensure the output directory exists
            output_dir = os.path.dirname(output_file)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # Save without header
            combined_df.to_csv(output_file, 
                             index=False, 
                             header=False, 
                             encoding='utf-8',
                             errors='replace')
            print(f"Results saved to: {output_file}")
            print(f"Total matching entries: {len(combined_df)}")
        except Exception as e:
            print(f"Error saving results: {str(e)}")
    else:
        print("No matching entries found in any of the CSV files.")


# Example usage
if __name__ == "__main__":
    input_folder = "/Users/wumengmeng/Desktop/project-MediaAgenda/two-mode/step1testcode"  # input folder path
    output_folder = "/Users/wumengmeng/Desktop/project-MediaAgenda/two-mode/canada_all_filtered1.csv"  # output folder path
    process_csv_files(input_folder, output_folder)