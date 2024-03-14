import pandas as pd 
file1 = "./test_speeches/predictions/Speech_1_Obama__AI.xlsx"
file2 = "./test_speeches/Speech_1_Obama_.xlsx"


df1 = pd.read_excel(file1,skiprows=1, index_col=0,header=None).iloc[:,:]

df1 = df1.fillna(0)

df1
import pandas as pd 
df2 = pd.read_excel(file2,skiprows=8,header=None).iloc[:,1:]
df2.index = df2.index.fillna(0)

df2 = df2.fillna(0)



# Check if shapes are the same
if df1.shape != df2.shape:
    print("Sheets have different shapes. They cannot be compared.")
else:
    differences = []

    # Compare cell values
    for i in range(df1.shape[0]):
        for j in range(df1.shape[1]):
            if df1.iloc[i, j] != df2.iloc[i, j]:
                differences.append((i+1, j+1, df1.iloc[i, j], df2.iloc[i, j]))

    if differences:
        diff_df = pd.DataFrame(differences, columns=['Row', 'Column', 'Value_Sheet1', 'Value_Sheet2'])

        diff_excel_path = 'differences.xlsx'
        diff_df.to_excel(diff_excel_path, index=False)
        print(f"Differences saved in '{diff_excel_path}'.")
    else:
        print("Sheets are identical. No differences found.")

