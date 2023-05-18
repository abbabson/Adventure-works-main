
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

![MySQL](https://img.shields.io/static/v1?style=for-the-badge&message=MySQL&color=4479A1&logo=MySQL&logoColor=FFFFFF&label=)

![Python](https://img.shields.io/static/v1?style=for-the-badge&message=Python&color=3776AB&logo=Python&logoColor=FFFFFF&label=)

![Power BI](https://img.shields.io/static/v1?style=for-the-badge&message=Power+BI&color=222222&logo=Power+BI&logoColor=F2C811&label=)
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/abbabson/Adventure-works/blob/6148e6dbdd38048df6a0061960b8009a0500e76a/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Sales Monitoring Dashboard</h3>

  <p align="center">
    Featuring database creation, data modeling in Power BI and python scripting
 <br />



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ul>
    <li><a href="#requirement">Requirement gathering</a></li>
        <li><a href="#stakeholders">Identifying stakeholders</a></li>
        <li> <a href="#raw-data">Understanding raw data</a></li>
 <li> <a href="#python-scripting">Python scripting</a></li>

 <li><a href="#database-loading">Database loading</a></li>

 <li><a href="#creating-views">Creating views </a></li>
        <li><a href="#data-cleansing">Data cleansing </a></li> 
<li><a href="#modeling">Data modeling</a></li>
   <li><a href="#visualization">Data visualization</a></li> 
    <li><a href="#insights">Insights</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</details>


<div align="left">
<!-- ABOUT THE PROJECT -->
  
## About The Project 🍪 

![Dashboard](https://github.com/abbabson/Adventure-works/blob/7fed1b5d60e198fa0c0f5fed1b00f2905e0f2481/screenshot.png)

Tracking Accidents and Casualties across UK Roads in 2021 - 2022
<a name="requirement"/>
### Requirement Gathering

Client wants a dashboard monitoring sales of company's product

#### a. Primary KPIs
- Top ten customers, filtered by:
  - product name
  - product category
  - product status
  - product line

- Top ten products by sales, filtered by:
  - product name
  - product category
  - product status
  - product line

#### b. Secondary KPIs
- Total sales by category

- Daily sales trend

<!-- -->
  <a name="stakeholders"/>
  
## Identifying Stakeholders 🧑🏽‍💼

- Sales team
- Marketing Department
  
<a name="raw-data"/>
  
### Understanding Raw Data 🥩

The raw data exists in 9 CSV files representing 1 fact table and 8 dimension tables
  

| Table | description (datatype) |
| ------------- | ------------- |
| Budget  | details budget of each product and product categories per period  |
| BudgetPeriod  | date table for the budget table  |
| customer  | each row records a customer information  |
| dimdates  | date table for the fact table  |
| dimProductCategory  | records the various product categories available |
| dimProductSubCategory  | lists the product subcategories available  |
| product  | lists individual products  |
| Sales  | The fact table: records individual sales transaction  |
| Territory  | Lists regional locations  |


  <a name="python-scripting"/>
  
### Converting CSV to SQL INSERT statements with Python 🐍

I wrote a Python <link to script> script using the csv and os modules, that takes in a csv file and outputs an SQL file with INSERT statements for each row in the CSV.


  <a name="database-loading"/>
  
### Loading into database 🧺

a MySQL database was created to host the data. The ERD is shown below and using MySQL's built-in GUI tool, it was converted into a database schema

<insert diagram here>


 <a name="creating-views"/>
  
### Creating views 🌁

To lessen the load on the BI tool further down the pipeline, and to make modeling easier, I created 4 views on top of the data <link here> (dim_customer, dim_calendar, dim_product and fact_sales)

  <a name="data-cleansing"/>
  
### Data cleansing 🧹
  
Issues
- No major cleaning issues; data was loaded directly into the BI tool


  <a name="modeling"/>
### Data Modeling 🏛 

The following star schema was created for the data model in Power BI
  
  ![Schema](https://github.com/abbabson/Adventure-works/blob/6cad93b2e2eccc03fdc10b68281975093584982f/data%20model.png)

  <a name="visualization"/>
  
### Data Visualization 🎨

- Power BI magic!✨ The report pbix file is available in this repo to explore design decisions
  
  The following DAX measures were used:
  
``` Non-Null Days = 
CALCULATE(
    COUNTROWS('awdb dim_calendar'),
    NOT(ISBLANK('awdb dim_calendar'[Day]))
)

Top 10 Customers by Sales = 
IF(RANKX(ALL('awdb dim_customer'[fullname]), [Total Sales],,DESC)<=10,[Total Sales], BLANK())

Top 10 Products by Sales = 
IF(RANKX(ALL('awdb dim_product'[product_name]), [Total Sales],,DESC)<=10,[Total Sales], BLANK())

Total Sales = 
SUM('awdb fact_sales'[SalesAmount])
  ```
  
  <a name="insights"/>
  
### Deriving Insights

- The primary source of revenue for the company is from the sales of bikes with 96% of sales coming from that category alone

- Sales peaked on the 22nd of the month
 

<!-- CONTACT  ☎️ -->

  <a name="contact"/>
  
## Contact

Abiodun Babatola - [connect on linkedin](https://www.linkedin.com/in/abbabson) - joshuaolubori@gmail.com


<p align="right">(<a href="#readme-top">back to top</a>)</p>



