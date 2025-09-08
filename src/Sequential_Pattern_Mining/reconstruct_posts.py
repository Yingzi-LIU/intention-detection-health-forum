import pandas as pd
import json
import sys

def reconstruct_from_ids(df, id_ranges):
    """
    Accurately reconstructs posts from the DataFrame based on the provided ID ranges.
    
    Args:
        df (pd.DataFrame): The DataFrame containing sentences and labels.
        id_ranges (list): A list of strings with the start and end IDs of posts, e.g., ['3-19', '20-24'].
        
    Returns:
        list: A list of dictionaries, where each dictionary represents a reconstructed post.
    """
    reconstructed_data = []
    
    # Ensure the ID column is of integer type for easy lookup
    if 'ID' in df.columns:
        df['ID'] = pd.to_numeric(df['ID'], errors='coerce').fillna(0).astype(int)
    
    # Get all column names from the DataFrame, excluding 'ID' and 'Sentences'
    label_columns = [col for col in df.columns if col not in ['ID', 'Sentences']]
    
    for i, id_range_str in enumerate(id_ranges):
        # Fix for non-standard dash characters like en-dash (–)
        id_range_str = id_range_str.replace('–', '-')

        post_data = {
            "post_id": i + 1,
            "sentences": []
        }
        
        # Parse the ID range string, e.g., '3-19'
        if '-' in id_range_str:
            start_id, end_id = map(int, id_range_str.split('-'))
        else:
            # Handle posts with a single sentence, e.g., '49'
            start_id = end_id = int(id_range_str)
            
        # Accurately select sentences from the DataFrame based on the ID range
        # Use the ID column for filtering, avoiding reliance on row index
        sentences_for_post = df[(df['ID'] >= start_id) & (df['ID'] <= end_id)]

        for _, row in sentences_for_post.iterrows():
            sentence_data = {
                "text": row['Sentences']
            }
            # Dynamically add all other columns as key-value pairs
            for col in label_columns:
                sentence_data[col] = row[col]
                
            post_data["sentences"].append(sentence_data)
        
        # Only posts containing sentences are added to the result
        if post_data["sentences"]:
            reconstructed_data.append(post_data)

    return reconstructed_data

def save_reconstructed_data(data, file_path):
    """
    Saves the reconstructed data to a JSON file.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ Data successfully saved to {file_path}")

def check_missing_ids(df, id_ranges):
    """
    Checks for and prints any IDs from the DataFrame that are not in the ID ranges.
    
    Args:
        df (pd.DataFrame): The DataFrame containing the sentences.
        id_ranges (list): The list of ID ranges used for reconstruction.
    """
    all_ids_in_df = set(df['ID'].unique())
    all_ids_in_ranges = set()

    for id_range_str in id_ranges:
        id_range_str = id_range_str.replace('–', '-')
        if '-' in id_range_str:
            start_id, end_id = map(int, id_range_str.split('-'))
            all_ids_in_ranges.update(range(start_id, end_id + 1))
        else:
            all_ids_in_ranges.add(int(id_range_str))
            
    missing_ids = sorted(list(all_ids_in_df - all_ids_in_ranges))
    
    if missing_ids:
        print("\n⚠️  Warning: The following IDs were not included in the ID_RANGES list:")
        print(missing_ids)
        print(f"Total missing IDs: {len(missing_ids)}")
    else:
        print("\n✅ All IDs from the CSV file are included in the ID_RANGES list.")


if __name__ == '__main__':
    # The ID list you provided
    ID_RANGES = [
        '3-19', '20-24', '25-27', '28-30', '31-39', '40-48', '49', '50-55',
        '57-64', '65-68', '69-70', '71-77', '78-80', '81-89', '90-98', '99-106',
        '107-109', '110-115', '116-117', '118-119', '120-122', '123-133',
        '134-139', '140-142', '143-147', '148-162', '163-169', '170-178',
        '179-188', '189-201', '202-216', '217-224', '225-238', '239-242', '243',
        '244', '245-254', '255-258', '259-265', '266-278', '279-284', '285-286',
        '287-289', '290-292', '293-296', '297-300', '301-307', '308-310',
        '311-317', '318-324', '325-327', '328-335', '336-349', '350-354',
        '355-357', '358-360', '361-363', '364-367', '368-372', '373-374', '375',
        '376-385', '386', '387-390', '391-392', '393-394', '395-400', '401-402',
        '403-405', '406-411', '412-430', '431-439', '440-450', '451-457',
        '458-461', '462-482', '483-486', '487-489', '490-498', '499-509',
        '510-516', '517-528', '529', '530-531', '532-536', '537-545', '546-549',
        '550-553', '554-558', '560-561', '562-563', '564-566', '567-573',
        '574-576', '577-579', '580-585', '586-587', '588-595', '596-613',
        '614-617', '618-620', '621-627', '628-630', '631-643', '644-647',
        '648-656', '657', '658-664', '665-667', '668-678', '680-682', '683-686',
        '688-694', '695-697', '698-699', '700-708', '709-716', '717–719',
        '720-724', '725-730', '731', '732-734', '735', '737-756', '757-758',
        '759-760', '762-763', '764-769', '770-783', '784-789', '790-791',
        '792-806', '810-817', '819-827', '828-833', '834-839', '840-843',
        '845-852', '853-857', '859-863', '865-869', '871-876', '877-881',
        '883-892', '893-897', '899-902', '903-906', '908-909', '910-913',
        '915-919', '920-925', '927-931', '932-936', '938-944', '945-950',
        '952-960', '961-965', '967-975', '977-984', '986-994', '995-1000'
    ]
    
    # Define file paths
    CSV_FILE_PATH = 'data/projet_annotation_sante_final_M1.csv'
    OUTPUT_FILE_PATH = 'data/reconstructed_posts_final.json'

    # Load the CSV file, specifying that 'NA' should be treated as a missing value
    try:
        labeled_sentences_df = pd.read_csv(CSV_FILE_PATH, na_values=['NA'])
    except FileNotFoundError:
        print(f"Error: The file {CSV_FILE_PATH} was not found.")
        sys.exit()

    # Replace NaN values with the string 'NA' to match the desired output
    labeled_sentences_df.fillna('NA', inplace=True)

    # Reconstruct the data
    reconstructed_data = reconstruct_from_ids(labeled_sentences_df, ID_RANGES)
    
    # Check for missing IDs and print them
    check_missing_ids(labeled_sentences_df, ID_RANGES)

    # Save the reconstructed data
    save_reconstructed_data(reconstructed_data, OUTPUT_FILE_PATH)
