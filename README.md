## ETL Pipeline with Python

This project is a simple ETL (Extract, Transform, Load) pipeline built using Python. It extracts data from CSV, JSON, and XML files, transforms the data by merging it into a single dataset, and loads the transformed data into an Excel file. The process also includes logging to track the ETL process steps.

## Features
- **Dynamic File Detection:** Automatically detects and processes CSV, JSON, and XML files from a specified directory.
- **Data Transformation:** Merges extracted data into a single DataFrame.
- **Logging:** Detailed logs are saved to a log file.
- **Excel Export:** Saves the final transformed data into an Excel file.

## Prerequisites
Make sure you have Python 3.x installed along with the required libraries:

```bash
pip install pandas openpyxl
```

## Usage
1. **Clone the repository or download the script.**
2. **Set the directory path:**
   Update the `directory_path` variable with the path where your source files (CSV, JSON, XML) are located.

   ```python
   directory_path = r"C:\Users\YourUsername\Downloads\source"
   ```
3. **Run the ETL script:**
   
   ```bash
   python etl_script.py
   ```
4. **Check outputs:**
   - Transformed data will be saved as `transformed_data.xlsx` in the same directory.
   - Log file `log_file.txt` will be saved in the script's working directory. The script will also print the path of the log file.

## Log File
Logs provide detailed information about the ETL process, including:
- File extraction status
- Errors encountered
- Time taken to complete the process

The location of the log file will be printed on execution.

## License
This project is open-source and free to use for educational and personal purposes.

## Author
[Your Name]  
[Your Email or GitHub Profile]

