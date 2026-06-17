import pandas as pd

from model_loader import prediction_features

def prepare_input_data(origin, dest, airline, month, day_of_week, distance, crs_dep_time):
    input_df = pd.DataFrame(
        columns=prediction_features
    )

    input_df.loc[0] = 0
    input_df.at[0, 'month'] = month
    input_df.at[0, 'day_of_week'] = day_of_week
    input_df.at[0, 'distance'] = distance
    input_df.at[0, 'crs_dep_time'] = crs_dep_time

    origin_column = f'origin_{origin}'
    dest_column = f'dest_{dest}'
    carrier_column = f'op_unique_carrier_{airline}'

    if origin_column not in input_df.columns:
        raise ValueError(f"Unknwon origin airport: {origin}")

    if dest_column not in input_df.columns:
        raise ValueError(f"Unknwon destination airport: {dest}")

    if carrier_column not in input_df.columns:
        raise ValueError(f"Unknwon airline: {airline}")
    
    input_df.at[0, origin_column] = 1
    input_df.at[0, dest_column] = 1
    input_df.at[0, carrier_column] = 1

    return input_df

