#!/bin/bash
    set -e
    set -u
    set -o pipefail

# variables
LOG_FILE_PATH="/home/jc/Automation-OtherTools_projects/Project1_AutomotiveIndustry/Car_Manufacturing/01_Spanish/logs/bash_script.log"


# Redirect to $LOG_FILE_PATH
exec >> $LOG_FILE_PATH


# Redirect stderr to the same place as stdin
exec 2>&1

 
# Log a message with a formatted timestamp
echo -e "Script started $(date)"


abs_path_data_cleaning="/home/jc/Automation-OtherTools_projects/Project1_AutomotiveIndustry/Car_Manufacturing/01_Spanish/scripts/data_cleaning.py"

abs_path_train_model="/home/jc/Automation-OtherTools_projects/Project1_AutomotiveIndustry/Car_Manufacturing/01_Spanish/scripts/train_model.py" 

abs_path_generate_report="/home/jc/Automation-OtherTools_projects/Project1_AutomotiveIndustry/Car_Manufacturing/01_Spanish/scripts/generate_report.py"

echo -e "Step 1/3: Data Cleaning $(date)"
$abs_path_data_cleaning

echo -e "Step 2/3: train model $(date)"
$abs_path_train_model
 
echo -e "Step 3/3: generate report $(date)"
$abs_path_generate_report

# Log the end of the script
echo -e "Script finished $(date)"
