import pandas as pd

def filter_columns_from_data_source(column_names: list, data_source: str) -> pd.DataFrame:
    ''' 
    This function returns a data frame containing only the column_names from the data_source which is located in the current workspace.
    In case the data source is not found prints out an Error file not found
    In case a column name is not contained in the data soruce it prints an error message that the corresponding columns  is not found
    In case of any other error it prints out the error.
    
    Input: 
        column_names : list of column names
        data_source: : file name
        
    Output: 
        Data frame containing only the columns column_names from the data_source
    '''
    
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
