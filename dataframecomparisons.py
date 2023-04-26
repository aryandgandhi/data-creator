
import pandas as pd
import pyodbc
import sys
import pandas as pd
import time
import random 

def magnitude_difference(old_df, new_df):
    # filter out non-numeric columns
    numeric_cols = old_df.select_dtypes(include=['number']).columns
    
    # compute the difference in magnitude between the old and new dataframes
    diff_df = pd.DataFrame(index=numeric_cols, columns=['max_diff', 'mean_diff', 'std_diff'])
    for col in numeric_cols:
        old_col = old_df[col]
        new_col = new_df[col]
        max_diff = (new_col - old_col).abs().max()
        mean_diff = (new_col - old_col).abs().mean()
        std_diff = (new_col - old_col).abs().std()
        diff_df.loc[col] = [max_diff, mean_diff, std_diff]

    return diff_df




def paq_change(old_df, new_df):
    # filter out non-numeric columns
    
    # compute the difference in magnitude between the old and new dataframes

    final_df = pd.DataFrame()
    
    final_df["Magnitude Change"] = abs((new_df["ORDER_QTY"] - old_df["ORDER_QTY"])).sort_values()
    #can choose which one you want to sort
    final_df["Percent Change"] = abs(((new_df["ORDER_QTY"] - old_df["ORDER_QTY"]) / old_df["ORDER_QTY"]))
    final_df["PART_NUMBER"] = old_df["PART_NUMBER"] 

    return final_df






# define a function to calculate the sensitivity report
def sensitivity_report(before_df, after_df):
    report = {}
    for column in before_df.columns:
        before_set = set(before_df[column])
        after_set = set(after_df[column])
        added = after_set - before_set
        removed = before_set - after_set
        report[column] = {'added': added, 'removed': removed}
    return report

# calculate the sensitivity report
report = sensitivity_report(original_dataframe, test_df)







