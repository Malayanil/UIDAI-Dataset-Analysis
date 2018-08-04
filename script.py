import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn import preprocessing

df = pd.read_csv('UIDAI.csv', dtype = object )

X = df[['Registrar', 'EnrolmentAgency', 'State', 'District', 'SubDistrict', 'PIN', 'Gender', 'Age', 'AadhaarGenerated', 'EnrolmentRejected', 'ResidentsProvidingEmail', 'ResidentsProvidingMobile']]
'''
X1 = X[['Registrar']].values
X1 = X1.ravel()
X1 = Counter(X1)
print(X1)

labels = ['CSC e-Gov. Services India Ltd.', 'NSDL e-Governance Infrastructure Ltd.' , 'DENA BANK' , 'Bank Of India' , 'MP State Electronics Dev. Corp. Ltd.  ' , 'Tamil Nadu eGovernance Agency' , 'Govt of Gujarat' , 'Dept of ITC Govt of Rajasthan' , 'Govt of Kerala' , 'Union Bank' , 'Others']
sizes = [209771,54214,33869,19791,17309,15468,13894,13565,11937,5536,45454]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2)

plt.pie(sizes, autopct='%1.1f%%', explode=explode, startangle=0)
plt.legend(labels=labels)
plt.title('Registrars')
plt.show()

# Most Used Registrar: CSC e-Governance Services India Limited (2,09,771 Enrolled)
# Least Used Registrar: DIT Lakshadweep and UT of Puducherry (1 Person Enrolled for each)


X2 = X[['EnrolmentAgency']].values
X2 = X2.ravel()
X2 = Counter(X2)
print(X2)

labels = ['CSC SPV' , 'SRM Educ & Social Welfare Society' , 'SREI INFRASTRUCTURE FINANCES L' , 'Rajcomp Info Services Ltd', 'AKSH OPTIFIBRE LIMITED' , 'TN ARASU CABLE TV CORP. LTD' , 'Akshaya' , 'MPOnline Limited' , 'CMS Computers Ltd' , 'IAP COMPANY Pvt. Ltd', 'Others']
sizes = [100357,18101,16972,12910,12580,12114,11937,10808,9229,7537,228273]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2)
plt.pie(sizes, autopct='%1.1f%%', explode=explode, startangle=180)
plt.legend(labels=labels)
plt.title('EnrolmentAgencies')
plt.show()

# Most Popular Enrollment Agency: CSC SPV (1,00,357 Entries)
# Least Popular Enrollment Agency: District IT Society Jind, District Family and Welfare Society  Jhajjar, SHRIKRISHNA KHANDASARI SUGAR M, Quick Data IT Services Pvt Ltd, District Health and Family Welfare Society Fatehabad, DIT Lakshadweep, Planning and Research Department, Integrated Systems & Services, VIKALP MULTIMEDIA, WEBEL, District Sukhmani Society Amritsar Punjab, District Family & Welfare Society Palwal (1 Entry for each)


X3 = X[['State']].values
X3 = X3.ravel()
X3 = Counter(X3)
print(X3)

labels = ['Bihar', 'Uttar Pradesh', 'West Bengal', 'Madhya Pradesh', 'Rajasthan', 'Gujarat', 'Tamil Nadu', 'Maharashtra', 'Karnataka', 'Kerala', 'Others']
sizes = [81776,69476,60485,37360,28659,24146,21196,19783,15755,12378,69805]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2)
plt.pie(sizes, autopct='%1.1f%%', explode=explode, startangle=180)
plt.legend(labels=labels)
plt.title('States')
plt.show()

# Top State of Enrollment: Bihar (81776 Entries)
# Lowest State of Enrollment: Lakshadweep (5 Entries)


X4 = X[['Gender']].values
X4 = X4.ravel()
X4 = Counter(X4)
print(X4)

labels = ['Male', 'Female', 'UnDeclared']
sizes = [292798,148013,500]
explode = (0.1, 0.1, 0.2)
plt.pie(sizes, autopct='%1.1f%%', explode=explode, startangle=180)
plt.legend(labels=labels)
plt.title('Gender')
plt.show()

# Male: 2,92798
# Female: 1,48,013
# UnDeclared: 7


X5 = X[['EnrolmentRejected']].values
X5 = X5.ravel()
X5 = Counter(X5)
print(X5)

labels = ['0', '1','>1']
sizes = [409275,27884,3669]
explode = (0.1, 0.1, 0.2)
plt.pie(sizes, autopct='%1.1f%%', explode=explode, startangle=180)
plt.legend(labels=labels)
plt.title('Enrollments Rejected')
plt.show()


X6 = X[['ResidentsProvidingEmail']].values
X6 = X6.ravel()
X6 = Counter(X6)
print(X6)

labels = ['0', '1','>1']
sizes = [422997,16763,1058]
explode = (0.1, 0.1, 0.2)
plt.pie(sizes, autopct='%1.1f%%', explode=explode, startangle=180)
plt.legend(labels=labels)
plt.title('Emails Provided')
plt.show()


X7 = X[['ResidentsProvidingMobile']].values
X7 = X7.ravel()
X7 = Counter(X7)
print(X7)

labels = ['0', '1', '2', '>2']
sizes = [112629, 267748,36068,24373]
explode = (0.1, 0.1, 0.1, 0.2)
plt.pie(sizes, autopct='%1.1f%%', explode=explode, startangle=180)
plt.legend(labels=labels)
plt.title('Mobile Numbers Provided')
plt.show()


X8 = X[['Age']].values
X8 = X8.ravel()
X8 = Counter(X8)
print(X8)

# Youngest <1 Year Old (16,797)
# Oldest 101 Years Old (1)
# Most Enrolled Age 4 (24,040)


X9 = X[['District']].values
X9 = X9.ravel()
X9 = Counter(X9)

print(X9)
'''

