import streamlit as st

############################# Streamlit ############################

st.write("""
# Loan Rate
This app will give an applicant their loan amount and interest rate if elgible. Please enter your information and click on check my rate.
""")


# Age input slider
st.write("""
## Age
""")
age = st.slider('Age', value=30, min_value=18, max_value=80, step=1)



# Income
st.write("""
## Annual Income
""")
income = float(st.slider('Income', value=40000, min_value=10000, max_value=100000, step=1000))


# Debt
st.write("""
## Current Debt
""")
debt = st.slider('Debt', value=0, min_value=0, max_value=50000, step=1000)


# Loan Amount
st.write("""
## Loan Amount
""")
amount = st.slider('Amount of money you want to take out', value=10000, min_value=1000, max_value=50000, step=1000)


# Previous Default
st.write("""
## Have you previously defaulted on a Loan?
""")
previous_default = st.radio("Choose", ["Yes", "No"])


# Education level
st.write("""
## Highest Education level Completed
""")

education = st.slider("1=High School, 2=Associate, 3=Bachelor, 4=Masters and 5=PhD", value = 1, min_value = 1, max_value = 5, step = 1)


#age
a = age
#education
b = education
#income
c = income
#debt
d = debt
#loan amount
e = amount
#previous default

if(previous_default == 'Yes'):
    f = 0.0227

if(previous_default == 'No'):
    f = 0.0

score = ((80 - a) * 0.0029) + (0.0898 - (b * 0.01796)) + (((100000 - c) / 1000) * 0.0008067) + ((d / 1000) * 0.008338) + ((e / 1000) * 0.0005378) + ((e / c) * 0.045825) + ((d / c) * 0.01615) + f

if st.button('Check your rate'):
    if score > 0.8:
        st.write("You are not eligible at this time")
    else:
        intrate = round(((score / 0.02667) + 5), 2)
        loanamount = round(((0.8 - score) / 0.000016), 2)
        st.write("Your offer is $", loanamount, "at", intrate, "% interest")
