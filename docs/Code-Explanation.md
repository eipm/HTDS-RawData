### MATLAB Script step by step explanation:

**> This project has .m MATLAB scripts for different drug screening experiments that perform the following steps to raw data .xlsx files:**

1. Define two folder paths: input_folder and output_folder.
2. Get a list of all files in the input_folder that have the extension .xlsx using the dir function.
3. Loop through each file in the list.
4. Read the file into a table using the readtable function.
5. Flip certain rows of the table.
6. Replace certain values in the 'Concentration' column of the table based on some conditions.
7. Get the unique values in the 'PlateName' column of the table using the 'unique' function.
8. Loop through each unique plate name.
9. Get the rows of the table where the 'PlateName' column is equal to the current unique plate name.
10. Get the unique values in the 'DrugName' and 'Concentration' columns for these rows using the 'unique' function.
11. For each unique plate name, calculate the average Lum value for each unique drug at each unique concentration.
12. Create a cell array to store the output data.
13. Fill the first row with the headers.
14. Fill the remaining cells with the calculated average Lum values.
15. Calculate the average Lum value for each unique drug without a corresponding Drug Name or Concentration in the input file.
16. Add an empty row after every 10 rows of data (excluding the first two rows and the newly added rows).
17. Define the output file name based on the current plate name.
18. Write the output data to a CSV file using the 'writecell' function.
19. Print a message indicating that the output file has been created.
20. Repeat steps 7-19 for each unique plate name.
21. Print a message indicating that the script has finished running.
