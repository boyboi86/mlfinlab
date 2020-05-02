"""
Various useful functions
"""

import pandas as pd
import numpy as np

def crop_data_frame_in_batches(df: pd.DataFrame, chunksize: int):
    # pylint: disable=invalid-name
    """
    Splits df into chunks of chunksize

    :param df: (pd.DataFrame) Dataframe to split
    :param chunksize: (int) Number of rows in chunk
    :return: (list) Chunks (pd.DataFrames)
    """
    generator_object = []
    for _, chunk in df.groupby(np.arange(len(df)) // chunksize):
        generator_object.append(chunk)
    return generator_object

def reversion_spd():
    """
    find average speed of reversion
    ln(2)/x = y
    
    where 
    x = benchmark used
    y = years requried for reversion to take place
    """
    #https://www.hindawi.com/journals/jps/2016/5191583/
    #https://www.quantstart.com/articles/Basics-of-Statistical-Mean-Reversion-Testing/
    #average time required by vertical barriers to hit 70% profitable rate
    #work backwards to get hald life required
    #find correlation matrix for lenght of vertical barrier vs profitablility