import io
import json
import pandas as pd
def parse_saga_file(json_file, output_csv_path='media/df/saga_file.csv'):
    """
    Generate a Pandas DataFrame from a JSON file and save it as a CSV.

    Args:
        json_file (str): The path to the JSON file.
        output_csv_path (str): The path to save the resulting CSV file.
    Returns:
        None
    """
    try:
        # Read JSON file into Pandas DataFrame
        print(type(json_file),flush=True)
        # Create a file-like object from bytes
        json_buffer = io.BytesIO(json_file)
        
        # Convert JSON to DataFrame
        df = pd.json_normalize(json_buffer)

        # Renaming columns for clarity
        df.rename(columns={'_id.$oid': 'id', 'createdAt.$date': 'createdAt', 'name': 'name'}, inplace=True)
        
        # Save DataFrame as CSV
        df.to_csv(output_csv_path, index=False)
        
        print(f"DataFrame saved as {output_csv_path}",flush=True)
        
    except Exception as e:
        print(f"Error: {str(e)}",flush=True)



def parse_saga_instance_file(json_bytes, output_csv_path='media/df/saga_instace_file.csv'):
    try:
        # Decode the bytes to a string and load as JSON
        json_data = json.loads(json_bytes.decode('utf-8'))

        main_df = pd.json_normalize(json_data , sep="_")
        main_df.to_csv(output_csv_path)
        print(f"DataFrame saved as {output_csv_path}")

    except Exception as e:
        print(f"Error: {str(e)}")