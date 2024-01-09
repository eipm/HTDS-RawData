import pandas as pd

# Load the Excel file from the specified sheet
file_path = "C:/Users/omar7/OneDrive/Desktop/Data Analysis/AZ/Raw data/112123_FARAGE COMBO SCREEN.xlsx"
df_raw = pd.read_excel(file_path, sheet_name="Sheet1")

# Define the sorting pattern as per your instructions
pattern_lists = [
    ['B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9'],
    ['B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
    ['B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
    ['B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
    ['B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
    ['B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
    ['B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
    ['I9', 'J9', 'K9', 'L9', 'M9', 'N9', 'O9'],
    ['I8', 'J8', 'K8', 'L8', 'M8', 'N8', 'O8'],
    ['I7', 'J7', 'K7', 'L7', 'M7', 'N7', 'O7'],
    ['I6', 'J6', 'K6', 'L6', 'M6', 'N6', 'O6'],
    ['I5', 'J5', 'K5', 'L5', 'M5', 'N5', 'O5'],
    ['I4', 'J4', 'K4', 'L4', 'M4', 'N4', 'O4'],
    ['I3', 'J3', 'K3', 'L3', 'M3', 'N3', 'O3'],
    ['B16', 'C16', 'D16', 'E16', 'F16', 'G16', 'H16'],
    ['B15', 'C15', 'D15', 'E15', 'F15', 'G15', 'H15'],
    ['B14', 'C14', 'D14', 'E14', 'F14', 'G14', 'H14'],
    ['B13', 'C13', 'D13', 'E13', 'F13', 'G13', 'H13'],
    ['B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12'],
    ['B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11'],
    ['B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10'],
    ['I16', 'J16', 'K16', 'L16', 'M16', 'N16', 'O16'],
    ['I15', 'J15', 'K15', 'L15', 'M15', 'N15', 'O15'],
    ['I14', 'J14', 'K14', 'L14', 'M14', 'N14', 'O14'],
    ['I13', 'J13', 'K13', 'L13', 'M13', 'N13', 'O13'],
    ['I12', 'J12', 'K12', 'L12', 'M12', 'N12', 'O12'],
    ['I11', 'J11', 'K11', 'L11', 'M11', 'N11', 'O11'],
    ['I10', 'J10', 'K10', 'L10', 'M10', 'N10', 'O10'],
    ['B23', 'C23', 'D23', 'E23', 'F23', 'G23', 'H23'],
    ['B22', 'C22', 'D22', 'E22', 'F22', 'G22', 'H22'],
    ['B21', 'C21', 'D21', 'E21', 'F21', 'G21', 'H21'],
    ['B20', 'C20', 'D20', 'E20', 'F20', 'G20', 'H20'],
    ['B19', 'C19', 'D19', 'E19', 'F19', 'G19', 'H19'],
    ['B18', 'C18', 'D18', 'E18', 'F18', 'G18', 'H18'],
    ['B17', 'C17', 'D17', 'E17', 'F17', 'G17', 'H17'],
    ['I23', 'J23', 'K23', 'L23', 'M23', 'N23', 'O23'],
    ['I22', 'J22', 'K22', 'L22', 'M22', 'N22', 'O22'],
    ['I21', 'J21', 'K21', 'L21', 'M21', 'N21', 'O21'],
    ['I20', 'J20', 'K20', 'L20', 'M20', 'N20', 'O20'],
    ['I19', 'J19', 'K19', 'L19', 'M19', 'N19', 'O19'],
    ['I18', 'J18', 'K18', 'L18', 'M18', 'N18', 'O18'],
    ['I17', 'J17', 'K17', 'L17', 'M17', 'N17', 'O17'],
]
# Flatten the pattern_lists into a single list
pattern = [well for sublist in pattern_lists for well in sublist]

# Create a mapping from well to position
pattern_mapping = {well: index for index, well in enumerate(pattern)}

# Function to sort a single plate's data based on the pattern
def sort_plate_data(plate, pattern_mapping):
    plate = plate.copy()
    plate['SortOrder'] = plate['Well'].map(pattern_mapping)
    sorted_plate = plate.sort_values(by='SortOrder').drop('SortOrder', axis=1)
    return sorted_plate

# Split the raw data into sets of 299 rows for each plate
plates = [df_raw.iloc[i*299:(i+1)*299] for i in range(len(df_raw)//299)]

# Sort each plate
sorted_plates = [sort_plate_data(plate, pattern_mapping) for plate in plates]

# Combine the sorted plates
sorted_data = pd.concat(sorted_plates).reset_index(drop=True)

# Save the sorted data to a new Excel file
output_path = "C:/Users/omar7/OneDrive/Desktop/Data Analysis/AZ/output/Sorted_Plate_Data.xlsx"
sorted_data.to_excel(output_path, index=False)