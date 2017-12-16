# edx_telemetry_processing
The repository contains artificats for processing edx telemetry. The program takes edx file in json format as input and processes the file into SQL Server 2016 database.

1) The script Create_db_objects.sql creates the database [EdxStaging] and table [dbo].[Edx_DailyEvents]
2) The python script Json-Processing-Python.py processes the input telemetry and stores the parsed structured data into SQL Server.  
   The python script requires following input parameters:
   a) Input file - edx telemtry file in json format 
   b) SQL Server - Name of SQL Server instance 
   c) Port Number - SQL Server Port number 
   d) Database - Database name 
   e) UserName - SQL User name 
   f) Passoword - SQL User password 
3) The python code is developed in version 2.7.14
4) The python code uses standard modules, no custom modules are required to run the code.
   
