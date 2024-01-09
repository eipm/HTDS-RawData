library(ggplot2)  # Make sure ggplot2 is loaded

# Set the output format and directory
output_format <- "pdf"  # Change this to the desired output format: pdf, png, jpeg, svg, etc.
output_dir <- "C:/Users/oma4008/OneDrive - med.cornell.edu/Desktop/Data Analysis/AZ/output"  # Change this to the desired output directory

# Install the 'writexl' package
install.packages("writexl") 

# Load the 'writexl' package
library(writexl) # Make sure writexl is loaded


# Install the openxlsx package if not already installed
install.packages("openxlsx")

install.packages("readxl")
library(readxl)


# Load the openxlsx package
library(openxlsx)


## ----message=FALSE------------------------------------------------------------
install.packages("synergyfinder")
library(synergyfinder)
example_file <- file.choose("C:/Users/oma4008/OneDrive - med.cornell.edu/Desktop/Data Analysis/Flor/Input")
data <- read_excel(example_file)

## -----------------------------------------------------------------------------
res <- ReshapeData(
  data = data,
  data_type = "inhibition",
  impute = TRUE,
  impute_method = NULL,
  noise = TRUE,
  seed = 1)

## -----------------------------------------------------------------------------
str(res)

## ----message=FALSE, warning=FALSE---------------------------------------------
res <- CalculateSynergy(
  data = res,
  method = c("ZIP", "HSA", "Bliss", "Loewe"),
  Emin = NA,
  Emax = NA,
  correct_baseline = "all")

## -----------------------------------------------------------------------------
res$drug_pairs
str(res$synergy_scores)


## ----message=FALSE, warning=FALSE---------------------------------------------
res <- CalculateSensitivity(
  data = res,
  correct_baseline = "all"
)

## -----------------------------------------------------------------------------
sensitive_columns <- c(
  "block_id", "drug1", "drug2",
  "ic50_1", "ic50_2",
  "ri_1", "ri_2",
  "css1_ic502", "css2_ic501", "css")
res$drug_pairs[, sensitive_columns]


library(gridExtra)
library(ggplot2)


if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE)
}

library(synergyfinder)

# Set up a list to store the plots
plot_list <- list()

library(synergyfinder)

# Set up a list to store the plots
plot_list <- list()

# Define the vector of block IDs you want to plot
block_ids <- 1:30

# Set the dimensions for the PDF file containing the combined plots
pdf_file <- file.path(output_dir, "combined_plots.pdf")
pdf(pdf_file, width = 14, height = 18)  # Adjust the dimensions as needed

# Loop over the block IDs and call PlotSynergy for each block
for (block_id in block_ids) {
  # Call PlotSynergy function
  plot_synergy <- PlotSynergy(
    data = res,
    type = "2D",
    method = "HSA",
    block_ids = block_id,
    save_file = FALSE,
    file_type = "png",
    plot_title = paste("HSA Synergy Score for Block", block_id),
    dynamic = FALSE
  )
  
  # Loop through each plot and add it to the list
  for (i in 1:2) {
    plot_dose_response <- PlotDoseResponseCurve(
      data = res,
      plot_block = block_id,
      drug_index = i,
      plot_new = FALSE,
      record_plot = TRUE
    )
    plot_list[[paste0("plot", i, "_block", block_id)]] <- plot_dose_response
  }
  
  plot_heatmap_response <- Plot2DrugHeatmap(
    data = res,
    plot_block = block_id,
    drugs = c(1, 2),
    plot_value = "response",
    dynamic = FALSE,
    summary_statistic = c("mean", "median")
  )
  
  plot_heatmap_synergy <- Plot2DrugHeatmap(
    data = res,
    plot_block = block_id,
    drugs = c(1, 2),
    plot_value = "HSA_synergy",
    dynamic = FALSE,
    summary_statistic = c("quantile_25", "quantile_75")
  )
  
  # Add plots to the plot list
  plot_list[[paste0("plot3_block", block_id)]] <- plot_heatmap_response
  plot_list[[paste0("plot4_block", block_id)]] <- plot_heatmap_synergy
  
  # Call PlotSensitivity function for each block
  plot_sensitivity <- PlotSensitivitySynergy(
    data = res,
    plot_synergy = "HSA",
    show_labels = TRUE,
    dynamic = FALSE,
    plot_title = paste("HSA Sensitivity for Block", block_id)
  )
  
  plot_list[[paste0("plot_sensitivity_block", block_id)]] <- plot_sensitivity
  
 # Call PlotDoseResponse function and save the plot
  plot_dose_response_combined <- PlotDoseResponse(
    data = res,
    block_ids = block_id,
    drugs = c(1, 2),
    save_file = FALSE,
    file_type = "png"
  )
  
  # Modify the plot to adjust label spacing
  modified_plot <- plot_dose_response_combined + theme(axis.text.x = element_text(angle = 45, hjust = 1))
  
  # Save the modified plot with adjusted width using ggsave
  ggsave(
    filename = paste0(output_dir, "/plot_dose_response_block", block_id, ".png"),
    plot = modified_plot,
    width = 12,  # Adjust the width as needed
    height = 8,  # Adjust the height as needed
    units = "in"
  )
  
  # Add the modified plot to the list for combining into the PDF
  plot_list[[paste0("plot_dose_response_block", block_id)]] <- modified_plot
}


# Combine all plots into a PDF
pdf_file <- file.path(output_dir, "combined_plots.pdf")
pdf(pdf_file, width = 14, height = 18)  # Adjust the dimensions as needed

# Arrange and print plots in sets of four per page
for (i in seq(1, length(plot_list), by = 4)) {
  grid.arrange(
    do.call(arrangeGrob, c(plot_list[i:min(i+3, length(plot_list))], ncol = 2)),
    ncol = 1
  )
  
  if (i + 3 < length(plot_list)) {
    dev.new()
    pdf(pdf_file, width = 14, height = 18)  # Re-open the PDF device for a new page
  }
}

# Close the PDF device
dev.off()

# The rest of your existing code that saves the data as an Excel file
write_xlsx(res, path = file.path(output_dir, "output_file.xlsx"))
