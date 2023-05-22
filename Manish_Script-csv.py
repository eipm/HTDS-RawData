import os
import pandas as pd

# Define the paths to the input and output folders
input_folder = r'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Input Python'
output_folder = r'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Output'

# Use the os.listdir() function to get a list of files in the input folder with the extension '.csv'
files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

# Loop through each file in the input folder
for file in files:
    # Read the current file into a DataFrame using read_csv function
    filepath = os.path.join(input_folder, file)
    T = pd.read_csv(filepath)

    # Get the unique values in the 'PlateName' column using the unique function
    unique_plate_names = T['Plate Name'].unique()

# Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition
for n in range(len(T)-1):
    if T.loc[n, 'Concentration'] == 1.111:
        T.loc[n, 'Concentration'] = 1.1111
        
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
                output_data = pd.concat([output_data.iloc[:f-1, :], pd.DataFrame(index=range(2),
                                                                                  columns=range(output_data.shape[1])),
                                         output_data.iloc[f-1:, :]], ignore_index=True)

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
