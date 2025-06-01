import pandas as pd

def filter_columns_from_data_source(column_names: list, data_source: str) -> pd.DataFrame:
    # Filters and returns a DataFrame containing only the specified columns from the given data source.
    
    try:
        df=pd.read_csv(data_source)
        filtered_df=df[column_names]
        return filtered_df
    except FileNotFoundError:
        print(f"Error: File '{data_soruce}' not found")
    except KeyError as e:
        print(f"Error: One or more columns not found in the data source: {e}")
    except Exception as e:
        print(f"Error: unexpected error occurred: {e}")
