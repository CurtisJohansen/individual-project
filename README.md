# Individual Project

### Idea

- For this project I am looking to see if there is a pay gap between genders and ethnicity for employees working for the city of San Antonio TX


### Project Data

- I am using the **Fiscal Year 2020 City Compensation Report** database off the City of San Antonio website

- Website to find data https://www.sanantonio.gov/Finance/bfi/CityComp2

- Total Compensation Reports for all City employees who either received a paycheck during a given fiscal year or where actively employed by the City as of fiscal year end.

### Project Goals:

- Analyze and model using salary data from fiscal year 2020
- look for paygaps in gender

## Project Summary

### Project Deliverables

- A clearly named final notebook. This notebook will be what you present and should contain plenty of markdown documentation and cleaned up code.

- A README that explains what the project is, how to reproduce you work, and your notes from project planning.

- A Python module or modules that automate the data acquisistion and preparation process

### Data Dictionary:

|          Feature               |            Definition               | Datatype |
|--------------------------------|-------------------------------------|:--------:|
|FIRST NAME                      |employee's first name                |object    |
|MIDDLE NAME                     |employee's middle name               |object    |
|LAST NAME                       |employee's last name                 |object    |
|EMPLOYEE CATEGORY               |uniform fire, uniform police, civilian                                    |object    |
|HIRE DATE1                      |reflects the most recent date of hire with the City in the event the employee left employment and was rehired or was a temporary employee and became a full time permanent employee                                    |datetime64|
|FY20 ANNUAL SALARY2             | reflects what the employee's current base salary would be for a year based on the position held at September 30, 2020                                    |float64   |
|FY20 BASE PAY3                  |reflects the regular salary the employee actually earned during the fiscal year regardless of position held.  It is possible with position changes, length of time with the City, etc. that an employee's Base Pay will not equal their Annual Salary                                    |float64   |
|FY20 LEAVE PAYOUT4              |reflects leave the employee sold back to the City during the fiscal year.  For full-time employees who separated during the fiscal year this may also include accrued leave sold back to the City upon separation                                     |float64   |
|FY20 OTHER5                     |reflects various incentives paid to City employees based on their job position and education level.  Incentives include but are not limited to education pay; language skill pay; certification pay; car allowance; transportation allowance; cell phone reimbursement; clothing allowance; and shift differential                                     |float64   |
|FY20 ARBITRATION & SETTLEMENTS6 |reflect the amount of backpay owed to an individual based on arbitration awards or settlements                                     |float64   |
|FY20 OVERTIME7                  |City policy allows employees to bank overtime hours for future compensated absences                                     |float64   |
|FY20 GROSS EARNINGS8            |reflect the total pay employees received between October 1st and September 30th                                     |float64   |
|FY20 ADDITIONAL BENEFITS9       |are incremental costs incurred by the City of behalf of employees to include the employer's share of FICA/Medicare, TMRS [Pension], annual Health Assessment [average healthcare benefit costs] and other related fringe provided to employees                                     |float64   |
|FY20 TOTAL COMPENSATION10       |reflects the total cost the City incurred for the employee's services received between October 1st and September 30th                                     |float64   |
|JOB TITLE                       |job code and job description         |object    |
|BUSINESS AREA                   |job dempartment                      |object    |
|GENDER                          |gender of employee - male or female  |object    |
|ETHNIC ORIGIN11                 |ethnicity information from employees through voluntary reporting (self identification)                                     |object    |
|EMPLOYEE SUBGROUP               |full and part time with department   |object    | 
|WITHDRAW DATE                   |last day of empoyment                |datetime64|
|---------------------------------------------------------------------------------|


## Hypothesis

#### Hypothesis 1 
- Is there a relationship between a person gender and the department worked in

#### Hypothesis 2
- Is there a relationship between a person ethnicity and the department worked in

#### Hypothesis 3 
- Is there a relationship between a persons gender and their annual salary

#### Hypothesis 4
- Is there a relationship between a persons ethnicity and their annual salary

#### Takeaways from Hypothesis Testing:
- The chi^2 test shows that there is a relationship between gender and department.
- The chi^2 test shows that there is a relationship between ethnicity and department.
- The chi^2 test shows that there is a relationship between gender and salary.
- The chi^2 test shows that there is a relationship between ethnicity and salary.

## Executive Summary - Conclusions & Next Steps

- There is a salary gap based on gender and on ethnicity

- Model performance has 75% accuracy when predicting gender using features like salary, gender and ethnicity

**Recommendations & next steps:**

- Recommend that the city research further into the pay gaps and the possible reasons they have those gaps in salaries

- Recommend that they look into developing a program to bring equality across gender and ethnicity

**If I had more time:**

- I would like to split up the salaries by department and investigating pay gap discrepancies

- Try other models and features

- Compare data from previous years to see if there is a trend

## Pipeline Stages Breakdown


### Acquire

- retrieved the data from the City of San Antonio website https://www.sanantonio.gov/Finance/bfi/CityComp2 downloaded and used the Fiscal Year 2020 City Compensation Report

###  Prepare  

- Column data types are appropriate for the data they contain

- Missing values are investigated and handled
 
- remove nulls in columns/rows
    
- remove any duplicates
     
- removes outliers
    
- split the data into train, validate, test 
    
### Explore

- The interaction between independent variables and the target variable is explored using visualization and statistical testing

### Model 

- At least 2 different models are created and their performance is compared. 

- One model is the distinct combination of algorithm, hyperparameters, and features.

- Best practices on data splitting are followed


## Reproduce My Project

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

- retrieved the data from the City of San Antonio website https://www.sanantonio.gov/Finance/bfi/CityComp2 downloaded and used the Fiscal Year 2020 City Compensation Report
- Open .xlxs file and delete rows 1 thur 14. Rows have description about the data
- Read this README.md
- Download the wrangle.py, explore.py, model.py and individual_project.ipynb files into your directory
- Run the individual_project.ipynb notebook

