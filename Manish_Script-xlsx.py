import os
import pandas as pd

# Define the paths to the input and output folders
input_folder = r'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Input Python'
output_folder = r'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Output'

# Use the os.listdir() function to get a list of files in the input folder with the extension '.xlsx'
files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]

# Loop through each file in the input folder
for file in files:
    # Read the current file into a DataFrame using read_excel function
    filepath = os.path.join(input_folder, file)
    T = pd.read_excel(filepath)
    
    # Split the data into separate dataframes
    dfs = []
    for i in range(0, len(T), 10):
        dfs.append(T.iloc[i:i+10])
    # Concatenate the dataframes and reset the index
    T = pd.concat(dfs, ignore_index=True)
    # Flip the rows of the table from row to row
    T.iloc[150:280, :] = T.iloc[150:280, :].iloc[::-1]
    T.iloc[430:560, :] = T.iloc[430:560, :].iloc[::-1]
    T.iloc[710:840, :] = T.iloc[710:840, :].iloc[::-1]
    T.iloc[990:1120, :] = T.iloc[990:1120, :].iloc[::-1]
    T.iloc[1270:1400, :] = T.iloc[1270:1400, :].iloc[::-1]
    T.iloc[1550:1680, :] = T.iloc[1550:1680, :].iloc[::-1]
    
    # Get the unique values in the 'PlateName' column using the unique function
    unique_plate_names = T['Plate Name'].unique()
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition
    for n in range(len(T)-1):
        if T.loc[n, 'Concentration'] == 1.111:
            T.loc[n, 'Concentration'] = 1.1111

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition
    for n in range(len(T)-1):
        if T.loc[n, 'Concentration'] == 3.333333333:
            T.loc[n, 'Concentration'] = 3.333

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition
    for n in range(len(T)-1):
        if (
            T.loc[n, 'Concentration'] == 10
            and (
                T.loc[n-9, 'Concentration'] == 0.000508053
                or T.loc[n-9, 'Concentration'] == 0.000508052634252908
                or T.loc[n-9, 'Concentration'] == 0.000508
                or T.loc[n-9, 'Concentration'] == 0.00050805
            )
            and (
                T.loc[n-1, 'Concentration'] == 3.333
                or T.loc[n-1, 'Concentration'] == 3.333333333
            )
            and not pd.isna(T.loc[n, 'Lum'])
            and not pd.isna(T.loc[n-1, 'Lum'])
        ):
            T.loc[n-9:n-1, 'Concentration'] = [
                0.000508053, 0.001524158, 0.004572474, 0.013717421,
                0.041152263, 0.1234679, 0.37037037, 1.111111111, 3.333333333
            ]
            T.loc[n, 'Concentration'] = 10

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition
    for n in range(len(T)-1):
        if (
            T.loc[n, 'Concentration'] == 30
            and T.loc[n-1, 'Concentration'] == 10
            and (
                T.loc[n-9, 'Concentration'] != 0.000508
                or T.loc[n-9, 'Concentration'] != 0.000508053
                and T.loc[n-9, 'Concentration'] != 0.000508052634252908
            )
            and not pd.isna(T.loc[n, 'Lum'])
            and not pd.isna(T.loc[n-1, 'Lum'])
        ):
            T.loc[n-9, 'Concentration'] = 0.00152401
            T.loc[n-8, 'Concentration'] = 0.00457201
            T.loc[n-7, 'Concentration'] = 0.01371701
            T.loc[n-6, 'Concentration'] = 0.04115201
            T.loc[n-5, 'Concentration'] = 0.1234601
            T.loc[n-4, 'Concentration'] = 0.3703701
            T.loc[n-3, 'Concentration'] = 1.111101
            T.loc[n-2, 'Concentration'] = 3.33301
            T.loc[n-1, 'Concentration'] = 10.01
            T.loc[n, 'Concentration'] = 30

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition
    for n in range(len(T)-1):
        if (
            T.loc[n, 'Concentration'] == 1
            and T.loc[n-1, 'Concentration'] == 0.333333333
            and (
                T.loc[n-9, 'Concentration'] == 0.0000508053
                or T.loc[n-9, 'Concentration'] == 0.0000508
            )
            and T.loc[n-8, 'Concentration'] == 0.000152416
            and not pd.isna(T.loc[n, 'Lum'])
            and not pd.isna(T.loc[n-1, 'Lum'])
        ):
            T.loc[n-9, 'Concentration'] = 0.0000508053
            T.loc[n-8, 'Concentration'] = 0.000152416
            T.loc[n-7, 'Concentration'] = 0.0004572
            T.loc[n-6, 'Concentration'] = 0.0013717
            T.loc[n-5, 'Concentration'] = 0.0041152
            T.loc[n-4, 'Concentration'] = 0.012346
            T.loc[n-3, 'Concentration'] = 0.037037
            T.loc[n-2, 'Concentration'] = 0.111
            T.loc[n-1, 'Concentration'] = 0.333
            T.loc[n, 'Concentration'] = 1

    # Check order
    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition
    for n in range(len(T)-1):
        if (
            T.loc[n, 'Concentration'] == 0.03
            and T.loc[n-1, 'Concentration'] == 0.01
            and not pd.isna(T.loc[n, 'Lum'])
            and not pd.isna(T.loc[n-1, 'Lum'])
        ):
            T.loc[n-9, 'Concentration'] = 0.00000152
            T.loc[n-8, 'Concentration'] = 0.00000457
            T.loc[n-7, 'Concentration'] = 0.0000137
            T.loc[n-6, 'Concentration'] = 0.0000412
            T.loc[n-5, 'Concentration'] = 0.000123457
            T.loc[n-4, 'Concentration'] = 0.00037037
            T.loc[n-3, 'Concentration'] = 0.001111111
            T.loc[n-2, 'Concentration'] = 0.003333333
            T.loc[n-1, 'Concentration'] = 0.01
            T.loc[n, 'Concentration'] = 0.03

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition
    for n in range(len(T)-1):
        if (
            T.loc[n, 'Concentration'] == 0.1
            and (
                T.loc[n-1, 'Concentration'] == 0.03333333
                or T.loc[n-1, 'Concentration'] == 0.033333333
            )
            and T.loc[n-9, 'Concentration'] == 0.00000508
            and not pd.isna(T.loc[n, 'Lum'])
            and not pd.isna(T.loc[n-1, 'Lum'])
        ):
            T.loc[n-9, 'Concentration'] = 0.00000508053
            T.loc[n-8, 'Concentration'] = 0.0000152416
            T.loc[n-7, 'Concentration'] = 0.0000457247
            T.loc[n-6, 'Concentration'] = 0.000137174
            T.loc[n-5, 'Concentration'] = 0.000411523
            T.loc[n-4, 'Concentration'] = 0.001234568
            T.loc[n-3, 'Concentration'] = 0.003703704
            T.loc[n-2, 'Concentration'] = 0.011111111
            T.loc[n-1, 'Concentration'] = 0.03333333
            T.loc[n, 'Concentration'] = 0.101

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition
    for n in range(len(T)-1):
        if (
            T.loc[n, 'Concentration'] == 6
            and T.loc[n-1, 'Concentration'] == 2
            and T.loc[n-9, 'Concentration'] == 0.000304832
            and not pd.isna(T.loc[n, 'Lum'])
            and not pd.isna(T.loc[n-1, 'Lum'])
        ):
            T.loc[n, 'Concentration'] = 6
            T.loc[n-1, 'Concentration'] = 2
            T.loc[n-2, 'Concentration'] = 0.666666667
            T.loc[n-3, 'Concentration'] = 0.222222222
            T.loc[n-4, 'Concentration'] = 0.074074074
            T.loc[n-5, 'Concentration'] = 0.024691358
            T.loc[n-6, 'Concentration'] = 0.008230453
            T.loc[n-7, 'Concentration'] = 0.002743484
            T.loc[n-8, 'Concentration'] = 0.000914495
            T.loc[n-9, 'Concentration'] = 0.000304832

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition
    for n in range(len(T)-1):
        if (
            T.loc[n, 'Concentration'] == 3
            and T.loc[n-1, 'Concentration'] == 1
            and (
                T.loc[n-9, 'Concentration'] == 0.000152416
                or T.loc[n-9, 'Concentration'] == 0.0001524
            )
            and not pd.isna(T.loc[n, 'Lum'])
            and not pd.isna(T.loc[n-1, 'Lum'])
            and T.loc[n-9, 'Concentration'] != 0.0000508
        ):
            T.loc[n-9, 'Concentration'] = 0.00015242
            T.loc[n-8, 'Concentration'] = 0.000457247
            T.loc[n-7, 'Concentration'] = 0.001371742
            T.loc[n-6, 'Concentration'] = 0.004115227
            T.loc[n-5, 'Concentration'] = 0.012345671
            T.loc[n-4, 'Concentration'] = 0.03703671
            T.loc[n-3, 'Concentration'] = 0.1111109
            T.loc[n-2, 'Concentration'] = 0.33333301
            T.loc[n-1, 'Concentration'] = 1.01
            T.loc[n, 'Concentration'] = 3

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
    for n in range(len(T['Concentration']) - 1):
        if T['Concentration'][n] == 0.12345679:
            T.at[n, 'Concentration'] = 0.1234679

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
    for n in range(len(T['Concentration']) - 1):
        if T['Concentration'][n] == 1.111:
            T.at[n, 'Concentration'] = 1.1111

    # Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
    for n in range(len(T['Concentration']) - 1):
        if T['Concentration'][n] == 3.333333333:
            T.at[n, 'Concentration'] = 3.333


    # Loop through each unique plate name value
    for plate_name in unique_plate_names:
        # Get the rows of the table where the 'PlateName' column is equal to the current unique plate name
        plate_rows = T['Plate Name'] == plate_name

        # Find the rows where the Well column starts with 'N' and the Batch column is empty
        N_rows = T['Well'].str.startswith('N') & plate_rows & T['Batch'].isnull()
        avg_Lum_values_missing = T.loc[N_rows, 'Lum'].mean()

        # Get the unique values in the 'DrugName' and 'Concentration' columns using the unique function
        unique_drugs = T.loc[plate_rows, 'Drug Name'].unique()
        unique_concentrations = T.loc[plate_rows, 'Concentration'].unique()

        Lum_values = pd.DataFrame(index=unique_concentrations, columns=unique_drugs)

        # Loop through each unique concentration value and get the Lum value for each unique drug
        for concentration in unique_concentrations:
            concentration_rows = (T['Concentration'] == concentration) & plate_rows

            for drug in unique_drugs:
                drug_rows = T['Drug Name'] == drug
                Lum_values.loc[concentration, drug] = T.loc[concentration_rows & drug_rows, 'Lum'].mean()

        # Create a DataFrame to store the output data
        output_data = pd.DataFrame(index=range(len(unique_concentrations) + 3),
                                   columns=range(len(unique_drugs) + 1))

        # Fill the first row with the plate name
        output_data.iloc[0, 0] = plate_name

        # Fill the second row with the headers
        output_data.iloc[1, 0] = 'Concentration'
        output_data.iloc[1, 1:] = unique_drugs

        # Fill the third row with the header 'Average Background Normalization Value'
        output_data.iloc[2, 0] = 'Average Background Normalization Value'

        # Fill the third row with the calculated average Lum values
        output_data.iloc[2, 1:] = avg_Lum_values_missing

        # Fill the remaining cells with the calculated average Lum values
        output_data.iloc[3:, 0] = unique_concentrations
        output_data.iloc[3:, 1:] = Lum_values.values

        # Add an empty row after every 10 rows of data (excluding the first three rows and the newly added rows)
        for f in range(4, min(output_data.shape[0], 200)):
            if (f - 4) % 12 == 0 and f > 3:
                output_data = pd.concat([output_data.iloc[:f, :], pd.DataFrame(index=range(2),
                                                                            columns=output_data.columns),
                                        output_data.iloc[f:, :]], ignore_index=True)


        # Define the output file name based on the current plate name
        output_file = os.path.join(output_folder, plate_name + '.csv')

        # Replace NaN values with blanks
        output_data = output_data.fillna('')

        # Write the output data to a CSV file using the to_csv function
        output_data.to_csv(output_file, index=False)

        # Print a message indicating that the output file has been created
        print(f'Output file {output_file} created')

# Print a message indicating that the script has finished running
print('Script finished running')
