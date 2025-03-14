## Business Intelligence (BI)

## 3. Create the cube with suitable dimension and fact tables based on ROLAP, MOLAP and HOLAP model.

# Data Cube Implementation: ROLAP, MOLAP, and HOLAP

## Overview
This project implements a data cube using three different OLAP storage models:
- **ROLAP (Relational OLAP)**
- **MOLAP (Multidimensional OLAP)**
- **HOLAP (Hybrid OLAP)**

It demonstrates the creation of suitable dimension and fact tables for each model.

## Video Reference
## This project is based on the assignment video:
[![Watch the video](https://img.youtube.com/vi/2JXiR91OXVg/0.jpg)](https://youtu.be/jwI6KFhFSS0?si=qUC8ujEBpUaXYoO5)

## Data Model
### Fact Table
The fact table contains measurable business data.
#### Columns:
- `fact_id` (Primary Key)
- `product_id` (Foreign Key to Product Dimension)
- `customer_id` (Foreign Key to Customer Dimension)
- `sales_amount`
- `quantity_sold`
- `date_id` (Foreign Key to Date Dimension)

### Dimension Tables
#### Product Dimension:
- `product_id` (Primary Key)
- `product_name`
- `category`
- `price`

#### Customer Dimension:
- `customer_id` (Primary Key)
- `customer_name`
- `region`
- `age_group`

#### Date Dimension:
- `date_id` (Primary Key)
- `date`
- `month`
- `quarter`
- `year`

## OLAP Models
### ROLAP (Relational OLAP)
- Uses a relational database (e.g., MySQL, PostgreSQL).
- Stores data in normalized form.
- Querying is performed using SQL with aggregation functions.

### MOLAP (Multidimensional OLAP)
- Uses a multidimensional database (e.g., Microsoft Analysis Services, IBM Cognos).
- Stores pre-aggregated data in cube format.
- Fast query performance but requires more storage.

### HOLAP (Hybrid OLAP)
- Combines ROLAP and MOLAP.
- Stores summarized data in cubes and detailed data in relational tables.
- Optimizes storage and query performance.



