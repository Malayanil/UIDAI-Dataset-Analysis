# UIDAI-Dataset-Analysis (Aadhaar Enrollment Analysis)

Welcome ! This is a generalised Read Me file for the Aadhaar Enrollment Analysis.<br><br>
<ul>
	<li>Data Insights and Analysis: HiveQL</li>
	<li>Visualization: Python 2.7.0</li>
	<li>Files and Folder:</li>
	
		UIDAI.csv -> The Dataset of 4,40,818 records downloaded from UIDAI data host site.
		sql.sql -> The SQL file for our Dataset Analysis.
		script.py -> The Python script for visualization Pie Charts.
		pie_charts -> The folder containing the PNGs of the Pie Charts used here.
	
</ul>

<b>Index: </b><br>
<ol>
	<li>Introduction</li>
	<li>Objectives and Results</li>
	<li>Code Explanation</li>
	<li>Graphical Visualization</li>
</ol>

<b>1. Introduction: </b>

  This project is an in-depth and visual analysis of the UIDAI Dataset of Aadhaar Enrollment in various states of India.<br>This dataset has been downloaded from the UIDAI host site and contains 4,40,818 records excluding the Header Row.<br>The indepth analysis has been done in HiveQL and the visual depiction has been done in Python 2.7.0.<br><br> It is well known that Pie Charts are not that helpful for visualization purposes among rest of the methods. This case was an exception and had to be visualized via Pie Charts due to the large gaps in between the number of people during categorization. 

                                               --End of Section One--


<b>2. Objectives and Results: </b>

	2.1 Count the number of identities(Aadhaar) generated by each Registrar and list top 3.
	  TOP 3: 
		a) CSC e-Governance Services India Limited: 2,09,771
		b) NSDL e-Governance Infrastructure Limited: 54,214
		c) DENA BANK: 33,869

	2.2 Count the number of identities(Aadhaar) generated by each Enrollment Agency and list top 3.
	  TOP 3: 
		a) CSC SPV: 1,00,357
		b) SRM Education And Social Welfare Society: 18,101
		c) SREI INFRASTRUCTURE FINANCES L: 16,972

	2.3 Count the number of Male, Female and UnDeclared Entries.
	  Count:
		a) Male: 2,92,798
		b) Female: 1,48,013
		c) UnDeclared: 7

	2.4 Count the number of identities(Aadhaar) generated in each state and list top 3.
	  TOP 3: 
		a) Bihar: 81,776
		b) Uttar Pradesh: 69,476
		c) West Bengal: 60,485	

	2.5 Top 3 districts with maximum identities generated for both Male and Female.
	  TOP 3:
		a) Barddhaman: 7,135
		b) North 24 Parganas: 6,894
		c) South 24 Parganas: 6,078

                                               --End of Section Two--


<b>3. Code Explanation: </b>

  We create a table named Test and load the 4,40,818 records into it and then run the queries to get our desired results.

  a) For the First Objective:
		
    SELECT COUNT(*),Registrar FROM Test GROUP BY Registrar ORDER BY COUNT(*) DESC
  
We select the Registrar column and another column as counting the number of records from our table Test and group the output by the Registrar column and order them in descending order.
    
  b) For the Second Objective:
    
    SELECT COUNT(*),EnrolmentAgency FROM Test GROUP BY EnrolmentAgency ORDER BY COUNT(*) DESC
    
We select the EnrollmentAgency column and another column as counting the number of records from our table Test and group the output by the EnrollmentAgency column and order them in descending order.

  c) For the Third Objective:
  
    SELECT COUNT(*), Gender FROM Test GROUP BY Gender ORDER BY COUNT(*) DESC

We select the Gender column and another column as counting the number of records from our table Test and group the output by the Gender column and order them in descending order.

  d) For the Fourth Objective:
  
     SELECT COUNT(*),State FROM Test GROUP BY State ORDER BY COUNT(*) DESC
     
We select the State column and another column as counting the number of records from our table Test and group the output by the State column and order them in descending order.
	
  
  e) For the Fifth Objective:
  
    SELECT COUNT(*), District FROM Test GROUP BY District ORDER BY COUNT(*) DESC

We select the District column and another column as counting the number of records from our table Test and group the output by the District column and order them in descending order.    

                                               --End of Section Three--
                                               
                                              
<b>4. Graphical Visualization: </b>                                              

![alt text](https://github.com/Malayanil/UIDAI-Dataset-Analysis/blob/master/pie_charts/combined.png)
<ul>
<li>Starting from the top left Pie Chart, the first one titled <b>Registrars</b> shows the most prevalent Registrars of Aadhar Generation in this dataset.</li> 
<li>The second Pie Chart titled <b>Enrollment Agencies</b> shows the most prevalent Enrollment Agencies of Aadhaar Generation in this dataset.</li> 
<li>The third Pie Chart titled <b>Gender</b> shows the percentage of Male, Female and UnDeclared Genders enrolling themselves for Aadhaar Generation in this dataset.</li> 
<li>The fourth Pie Chart titled <b>States</b> shows the dominant States whose people have enrolled themselves for the Aadhaar Generation in this dataset.</li>
<li>The fifth Pie Chart titled <b>Mobile Numbers Provided</b> shows the percentage of people providing their mobile numbers for Aadhaar Generation in this dataset.</li>
<li>The sixth Pie Chart titled <b>Emails Provided</b> shows the percentage of people providing their emails for Aadhaar Generation in this dataset.</li>
<li>The seventh Pie Chart titled <b>Enrollments Rejected</b> shows the percentage of people who have been rejected during the course of Aadhaar Generation for some reason in this dataset.</li>
</ul>

                                               --End of Section Four--
