# Credit-Risk-Model
*This application was posted to AWS EC2 but has since been deactiavted because I did not want to pay for it

Goals of the project
The goal of this project was to create and compare different machine learning methods in order to calculate the credit risk for individuals and then use this score to see what kind of loan they were eligible for. 
Data description
The data used was from 2 separate CSV from kaggle on credit risk. I decided to use 2 because each one had unique variables I wanted to use for my analysis such as education level and previous defaults. After preparing the data and getting my final database I had 33731 total observations. 

Age: This data represents the age of the applicant in years.

Education Level: This will represent the highest education achieved with the lowest being high school, certificate program, associates, bachelors, and PhD in a numerical scale (1-5).

Income: The annual income will be used or calculated based on salary or an hourly rate.

Debt to Income: This will be a ratio given in one data set and calculated in the other to provide a ratio of the applicants income over their current debt.

Other Debt: The total current debt of the applicant, will be used for the debt to income ratio.

Default: Will be a yes or no (0 or 1) response whether the person defaulted on their loan or not, which will be used for the training data.

Home Ownership: Whether the applicant owns a house, rents a property or other, for example living with a parent or relative.

Loan Intent: Their intended use of funds, such as education, debt consolidation, personal, etc.
Software
I used a jupyter notebook to import my database and to clean and prepare all the data for the models. I used numpy, pandas and sklearn packages in this for missing variables and the model. The models were also trained and calculated in this and then I used atom to create the code for my application. I decided to use Streamlit to create the app and integrated it into AWS EC2.
Analyses & Model Specifications
In order to successfully have a full database I used KNN algorithm to compute most missing values since there was often a correlation between them such as income and education level. After the data was prepared I used a random forest, decision tree and logistic regression to see whether the applicant would default or not and when measuring the accuracy, precision and recall the scores were 0.97 and 0.95. I then found the coefficients for the variables in the random forest classifier and used those as the multiplies essentially for my credit risk algorithm. I decided the range of numbers by finding a solid range of numbers from the data summary and what seemed most logical, for example choosing 18-80 for the age range. I then created a formula using the correlation of these variables and the numbers the applicant put in, in order to create the risk score. I chose to reject candidates with a risk score over 0.8 as that seemed to be a fair value to be able to give more people rates for the provided range of $1,000-$50,000 for loan amount and interest rates from 5-35%. I then used the credit risk score to compute the loan amount and interest rate, with the lowest interest and highest amount going to those with low credit risk scores and vice versa.
Deliverables
These formulas were then built into a Streamlit application and used to calculate the eligible amounts. I tested the formulas in the terminal to make sure they were accurate and then substituted the sys.arg values for the ones chosen in the online application that was built.
