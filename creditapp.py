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
    f = 0.01912551

if(previous_default == 'No'):
    f = 0.0

score = (((80 - a) / 80) * 0.15734775) + (0.1896271 - (b * 0.03792542)) + (((100000 - c) / 100000) * 0.08167142) + ((d / 50000) * 0.39980626) + ((e / 50000) * 0.0390813) + (((e/50000) / (c/100000)) * 0.11235136) + (((d/50000) / (c/100000)) * 0.13725742) + f

if st.button('Check your rate'):
    if score > 0.8:
        st.write("You are not eligible at this time")
    else:
        intrate = round(((score / 0.02667) + 5), 2)
        loanamount = round(((0.8 - score) / 0.000016), 2)
        st.write("Your offer is $", loanamount, "at", intrate, "% interest")
