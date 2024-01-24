import pandas as pd
import json

def parse_saga_instance_file(json_bytes, output_main_csv_path='media/df/saga_instance_main.csv', output_steps_csv_path='media/df/saga_instance_steps.csv'):
    try:
        # Decode the bytes to a string and load as JSON
        json_data = json.loads(json_bytes.decode('utf-8'))

        # Normalize the main data, excluding the 'steps' list
        main_df = pd.json_normalize(json_data, sep="_", record_path=None)
        main_df.rename(columns={'_id_$oid': 'saga_instance_id', 'sagaId_$oid': 'saga_id'}, inplace=True)
        main_df['steps']=main_df.steps.apply(lambda row : [step['_id'] for step in row])
        main_df.to_csv(output_main_csv_path, index=False)
        print(f"Main DataFrame saved as {output_main_csv_path}")

        
        # Normalize the 'steps' data and link it with the 'saga_instance_id'
        steps_df = pd.json_normalize(json_data, sep="_", record_path=['steps'])
        steps_df['saga_instance_id'] = main_df['saga_instance_id']  # Linking with the main data
        steps_df.to_csv(output_steps_csv_path, index=False)
        print(f"Steps DataFrame saved as {output_steps_csv_path}")

    except Exception as e:
        print(f"Error: {str(e)}")


def load_saga_instance_dfs():
    saga_instance_path = 'media/df/saga_instance_main.csv'
    saga_instance_steps_path = 'media/df/saga_instance_steps.csv'

    try:
        # Load the saga instance DataFrame
        saga_instance_df = pd.read_csv(saga_instance_path)

        # Load the saga instance steps DataFrame
        saga_instance_steps_df = pd.read_csv(saga_instance_steps_path)

        return saga_instance_df, saga_instance_steps_df

    except FileNotFoundError as e:
        print(f"File not found: {str(e)}")
        return None, None
    except Exception as e:
        print(f"Error while loading the dataframes: {str(e)}")
        return None, None