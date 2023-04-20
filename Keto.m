clear;
clc;

% Define the paths to the input and output folders
input_folder = 'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Input Python';
output_folder = 'C:\Users\oma4008\OneDrive - med.cornell.edu\Desktop\Data Analysis\Manish\Output';

% Use the dir function to get a list of files in the input folder with the extension '.csv'.
files = dir(fullfile(input_folder, '*.xlsx'));

% Set the format specifier for displaying numerical values
%format_specifier = '%0.14f';


% Loop through each file in the input folder.
for i = 1:length(files)

    % Read the current file into a table using readtable function
    T = readtable(fullfile(input_folder, files(i).name));

    % Flip the rows of the table from row  to row
    T(132:250,:) = flipud(T(132:250,:));


      % Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
  for n = 1:numel(T.Concentration)-1
  if T.Concentration(n) == 1.111
      T.Concentration(n) = 1.1111;
  end
  end

  % Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
  for n = 1:numel(T.Concentration)-1
  if T.Concentration(n) == 3.333333333
      T.Concentration(n) = 3.333;
  end
  end
  
  % Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n = 1:numel(T.Concentration)-1
    if T.Concentration(n) == 10 && (T.Concentration(n-9) == 0.000508053 || T.Concentration(n-9) == 0.000508052634252908 || T.Concentration(n-9) == 0.000508 || T.Concentration(n-9) == 0.00050805) && (T.Concentration(n-1) == 3.333 || T.Concentration(n-1) == 3.333333333) && ~isnan(T.Lum(n)) && ~isnan(T.Lum(n-1))
        T.Concentration(n-9:n-1) = [0.000508053, 0.001524158, 0.004572474, 0.013717421, 0.041152263, 0.1234679, 0.37037037, 1.111111111, 3.333333333];
        T.Concentration(n) = 10.001;
    end
end

  % Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n = 1:numel(T.Concentration)-1
     if T.Concentration(n) == 30 && T.Concentration(n-1) == 10 && (T.Concentration(n-9) ~= 0.000508 || T.Concentration(n-9) ~= 0.000508053 && T.Concentration(n-9) ~= 0.000508052634252908) && ~isnan(T.Lum(n)) && ~isnan(T.Lum(n-1))
 
        T.Concentration(n-9) = 0.00152401;
        T.Concentration(n-8) = 0.00457201;
        T.Concentration(n-7) = 0.01371701;
        T.Concentration(n-6) = 0.04115201;
        T.Concentration(n-5) = 0.1234601;
        T.Concentration(n-4) = 0.3703701;
        T.Concentration(n-3) = 1.111101;
        T.Concentration(n-2) = 3.33301;
        T.Concentration(n-1) = 10.01;
        T.Concentration(n) = 30;
     end
 end
 
 
 % Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
 for n = 1:numel(T.Concentration)-1
     if T.Concentration(n) == 1 && T.Concentration(n-1) == 0.333333333 && (T.Concentration(n-9) == 0.0000508053 || T.Concentration(n-9) == 0.0000508) && T.Concentration(n-8) == 0.000152416 && ~isnan(T.Lum(n)) && ~isnan(T.Lum(n-1))
 
         T.Concentration(n-9) = 0.0000508053;
         T.Concentration(n-8) = 0.000152416;
         T.Concentration(n-7) = 0.0004572;
         T.Concentration(n-6) = 0.0013717;
         T.Concentration(n-5) = 0.0041152;
         T.Concentration(n-4) = 0.012346;
         T.Concentration(n-3) = 0.037037;
         T.Concentration(n-2) = 0.111;
         T.Concentration(n-1) = 0.333;
         T.Concentration(n) = 1;
     end
 end

% Check order
% Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
for n = 1:numel(T.Concentration)-1
    if T.Concentration(n) == 0.03 && T.Concentration(n-1) == 0.01 && ~isnan(T.Lum(n)) && ~isnan(T.Lum(n-1))

        T.Concentration(n-9) = 0.00000152;
        T.Concentration(n-8) = 0.00000457;
        T.Concentration(n-7) = 0.0000137;
        T.Concentration(n-6) = 0.0000412;
        T.Concentration(n-5) = 0.000123457;
        T.Concentration(n-4) = 0.00037037;
        T.Concentration(n-3) = 0.001111111;
        T.Concentration(n-2) = 0.003333333;
        T.Concentration(n-1) = 0.01;
        T.Concentration(n) = 0.03;
    end
end
 

 % Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
 for n = 1:numel(T.Concentration)-1
     if T.Concentration(n) == 0.1 && (T.Concentration(n-1) == 0.03333333 || T.Concentration(n-1) == 0.033333333) && T.Concentration(n-9) == 0.00000508053 && ~isnan(T.Lum(n)) && ~isnan(T.Lum(n-1))
 
         T.Concentration(n-9) = 0.00000508053;
         T.Concentration(n-8) = 0.0000152416;
         T.Concentration(n-7) = 0.0000457247;
         T.Concentration(n-6) = 0.000137174;
         T.Concentration(n-5) = 0.000411523;
         T.Concentration(n-4) = 0.001234568;
         T.Concentration(n-3) = 0.003703704;
         T.Concentration(n-2) = 0.011111111;
         T.Concentration(n-1) = 0.03333333;
         T.Concentration(n) = 0.1;
     end
 end
 
 % Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
 for n = 1:numel(T.Concentration)-1
     if T.Concentration(n) == 6 && T.Concentration(n-1) == 2 && T.Concentration(n-9) == 0.000304832 && ~isnan(T.Lum(n)) && ~isnan(T.Lum(n-1))
 
         T.Concentration(n) = 6;
         T.Concentration(n-1) = 2;
         T.Concentration(n-2) = 0.666666667;
         T.Concentration(n-3) = 0.222222222;
         T.Concentration(n-4) = 0.074074074;
         T.Concentration(n-5) = 0.024691358;
         T.Concentration(n-6) = 0.008230453;
         T.Concentration(n-7) = 0.002743484;
         T.Concentration(n-8) = 0.000914495;
         T.Concentration(n-9) = 0.000304832;
     end
 end
 
 
  % Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
  for n = 1:numel(T.Concentration)-1
      if T.Concentration(n) == 3 && T.Concentration(n-1) == 1 && (T.Concentration(n-9) == 0.000152416 || T.Concentration(n-9) == 0.0001524) && ~isnan(T.Lum(n)) && ~isnan(T.Lum(n-1)) && (T.Concentration(n-9) ~= 0.0000508)
  
          T.Concentration(n-9) = 0.00015242;
          T.Concentration(n-8) = 0.000457247;
          T.Concentration(n-7) = 0.001371742;
          T.Concentration(n-6) = 0.004115226;
          T.Concentration(n-5) = 0.012345679;
          T.Concentration(n-4) = 0.037037037;
          T.Concentration(n-3) = 0.111111111;
          T.Concentration(n-2) = 0.333333333;
          T.Concentration(n-1) = 1.01;
          T.Concentration(n) = 3;
      end
  end

 % Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
  for n = 1:numel(T.Concentration)-1
      if T.Concentration(n) == 3  && T.Concentration(n-1) == 1 && T.Concentration(n-9) == 0.000152415790275873 && ~isnan(T.Lum(n)) && ~isnan(T.Lum(n-1)) && (T.Concentration(n-9) ~= 0.0000508)
  
          T.Concentration(n-9) = 0.0001524201;
          T.Concentration(n-8) = 0.00045724701;
          T.Concentration(n-7) = 0.00137174201;
          T.Concentration(n-6) = 0.00411522601;
          T.Concentration(n-5) = 0.01234567901;
          T.Concentration(n-4) = 0.03703703701;
          T.Concentration(n-3) = 0.11111111101;
          T.Concentration(n-2) = 0.33333333301;
          T.Concentration(n-1) = 1.01;
          T.Concentration(n) = 3;
      end
  end

 % Loop through each row of the table and replace values in the 'Concentration' column that meet the specified condition.
  for n = 1:numel(T.Concentration)-1
  if T.Concentration(n) == 0.12345679
      T.Concentration(n) = 0.1234679;
  end
  end
    
    % Get the unique values in the 'PlateName' column using the unique function.
    unique_plate_names = unique(T.PlateName, 'stable');

    % Loop through each unique plate name value
    for j = 1:length(unique_plate_names)

        % Get the rows of the table where the 'PlateName' column is equal to the current unique plate name
        plate_rows = strcmp(T.PlateName, unique_plate_names{j});

% Find the rows where the Well column starts with 'N' and the Batch column is empty
I_rows = startsWith(strtrim(T.Well), 'I') & plate_rows & isnan(T.Batch);
avg_Lum_values_missing = nanmean(T.Lum(I_rows));


        % Get the unique values in the 'DrugName' and 'Concentration' columns using the unique function.
        unique_drugs = unique(T.DrugName(plate_rows), 'stable');
unique_concentrations = unique(T.Concentration(plate_rows), 'stable');

        Lum_values = nan(length(unique_concentrations), length(unique_drugs));
        
        % Loop through each unique concentration value and get the Lum value for each unique drug.
        for k = 1:length(unique_concentrations)
            concentration_rows = (T.Concentration == unique_concentrations(k)) & plate_rows;

            for l = 1:length(unique_drugs)
                drug_rows = strcmp(T.DrugName, unique_drugs{l}) & plate_rows;
                Lum_values(k, l) = mean(T.Lum(concentration_rows & drug_rows));
            end
        end

        % Create a cell array to store the output data
        output_data = cell(length(unique_concentrations)+2, length(unique_drugs)+1);

        % Fill the first row with the headers
        output_data(1,1) = {'Concentration'};
        output_data(1,2:end) = unique_drugs;
       


% Fill the second row with the header 'Average Lum Value' and the calculated average Lum values.
output_data(2, 2:end) = num2cell(avg_Lum_values_missing);

        % Fill the second row with the header 'Average Lum Value'
        output_data(2,1) = {'Average Background Normalization Value'};
        
        % Fill the remaining cells with the calculated average Lum values.
        output_data(3:end,1) = num2cell(unique_concentrations);
       
        output_data(3:end,2:end) = num2cell(Lum_values);
        
        % Add an empty row after every 10 rows of data (excluding the first two rows and the newly added rows)
for f = 3:min(size(output_data, 1), 200)
    if mod(f-3, 12) == 0 && f > 2
        output_data = [output_data(1:f-1,:); cell(2, size(output_data, 2)); output_data(f:end,:)];       
        %f = f + 2; % increase the index by 2 to take into account the newly added empty rows
    end
end

        % Define the output file name based on the current plate name.
        output_file = fullfile(output_folder, strcat(unique_plate_names{j}, '.csv'));

        % Replace NaN values with blanks
nan_values = cellfun(@isnan, output_data, 'UniformOutput', false);
nan_indices = cellfun(@any, nan_values);
output_data(nan_indices) = {''};
        
        % Write the output data to a CSV file using the writematrix function.
        writecell(output_data, output_file);

        % Print a message indicating that the output file has been created.
        fprintf('Output file %s created\n', output_file);
    end
end

% Print a message indicating that the script has finished running.
fprintf('Script finished running\n');