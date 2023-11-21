import pandas as pd

for i in range(1, 19):
    filename = f"revised_4_{i}.xlsx"
    print(filename)
# List of Excel file names
file_names = [filename]  # Update with your file names

# Dictionary to store data frames for each sheet name
combined_data = {}

# Iterate through each file
for file_name in file_names:
    xls = pd.ExcelFile(file_name)
    sheet_names = xls.sheet_names

    # Iterate through each sheet
    for sheet_name in sheet_names:
        if sheet_name in combined_data:
            # Append to existing dataframe
            combined_data[sheet_name] = pd.concat([combined_data[sheet_name], xls.parse(sheet_name, skiprows=3)], ignore_index=True)
        else:
            # Create new dataframe
            combined_data[sheet_name] = xls.parse(sheet_name)

# Save the combined data to a new Excel file
with pd.ExcelWriter('combined_file.xlsx') as writer:
    for sheet_name, df in combined_data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
