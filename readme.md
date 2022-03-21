# Automation: Agile, TDD Process

This project uses the sample app of [API Logic Server](https://github.com/valhuber/ApiLogicServer/blob/main/README.md) to illustrate:
  
1. **Rapid project creation and customization:** using API Logic Server, for 1-command creation of projects that provide User Interfaces and APIs from a database.  Runnng screens are an excellent way to engage business user collaboration.

1. **Logic Automation:** using spreadsheet-like rules to dramatically reduce backend code, and make logic transparent to the team.

1. **Transparent TDD Testing:** using [behave](https://behave.readthedocs.io/en/stable/tutorial.html) (a [TDD](http://dannorth.net/introducing-bdd/) framework) for defining systems, to promote Agile collaboration with business users.  You define Features (aka Stories) and Scenarios (aka tests) in `behave`, with underlying Python test implementations.

2. **Transparent Test / Logic Tracing:** further promote Agile collaboration, by making logic transparent and integrated with Testing, in this generated `readme.md` (see the [TDD Report,](#tdd-report) at end).

  
&nbsp;&nbsp;

# Sample Project

This is the sample project from API Logic Server, based on the Northwind database (sqlite database located in the `database` folder - no installation required):

<figure><img src="https://github.com/valhuber/LogicBank/raw/main/images/nw.png"></figure>

&nbsp;&nbsp;

### Verify Installation

You can confirm its working by installing and running [as described here](https://github.com/valhuber/TDD/wiki/Setup).

&nbsp;&nbsp;

# Process Overview

The created project provides the User Interface and API described below, and implements the transactional logic described in the [TDD Report](#tdd-report).  It was created, customized and tested as described in the subsections below.

<figure><img src="https://github.com/valhuber/TDD/blob/main/images/TDD-process.png"></figure>
  
&nbsp;&nbsp;

## Table of Contents

* [Process Overview](#process-overview)
   * [1. Create Api Logic Project](#1-create-api-logic-project)
         * [1a. Creates Admin App](#1a-creates-admin-app)
         * [1b. And <strong>API</strong>](#1b-and-api)
   * [2. Collaborate using <strong>Admin App</strong>](#2-collaborate-using-admin-app)
         * [2a. Iterate Data Model](#2a-iterate-data-model)
         * [2b. Uncover TDD Scenarios](#2b-uncover-tdd-scenarios)
   * [3. Define Scenarios in Behave](#3-define-scenarios-in-behave)
      * [3a. Add Custom Service](#3a-add-custom-service)
   * [4. Logic Specification](#4-logic-specification)
   * [5. Declare Logic: 21 rules](#5-declare-logic-21-rules)
   * [6. Code/Run TDD Tests](#6-coderun-tdd-tests)
   * [7. <strong>Create TDD/Logic Reports</strong>](#7-create-tddlogic-reports)
         * [Working with TDD](#working-with-tdd)
* [Business Agility](#business-agility)
      * [Increased Transparency: TDD Report, <em>with logic</em>](#increased-transparency-tdd-report-with-logic)
* [TDD Report](#tdd-report)

&nbsp;&nbsp;

## 1. Create Api Logic Project

API Logic Server is used once you have a preliminary database design.  Use your existing procedures.  Include at least minimal test data.


Then (presuming API Logic Server [is installed](https://github.com/valhuber/ApiLogicServer/blob/main/README.md)), create the project with this command, using `venv` based installs:

```
ApiLogicServer create db_url= project_name=TDD
```

or, like this, using docker-based installs:
```
ApiLogicServer create-and-run --project_name=/localhost/ApiLogicProject --db_url=
```

&nbsp;&nbsp;

#### 1a. Creates Admin App

The Agile objective of collaboration is typically best-served with _running_ screens.  The problem is, it takes quite a long time to create the API and screens to reach this point.  And this work can be wasted if there were misunderstandings.

Ideally, User Interface creation would be automatic.

So, API Logic Server creates first-cut screens, automatically from the data model.  

The app shown below [(more detail here)](https://github.com/valhuber/ApiLogicServer#admin-app-multi-page-multi-table-automatic-joins) is suitable for initial business user collaboration to confirm the data model structure, and basic _back office_ data maintenance.

You can [customize it](https://github.com/valhuber/ApiLogicServer#admin-app-customization) by editing a simple `yaml`file (e.g, field captions, ordering etc.)

<figure><img src="https://github.com/valhuber/ApiLogicServer/wiki/images/ui-admin/run-admin-app.png?raw=true"></figure>


&nbsp;&nbsp;

#### 1b. And **API**

It is not difficult to create a single endpoint API.  The problem is that it's quite a bit more work to create an endpoint for each table, with support for related data, pagination, filtering and sorting.

Ideally, API creation would be automatic.

So, API Logic Server creates such an API instantly, suitable for application integration, and creating custom User Interfaces.  The API enforces the business logic described below.

The [created project is customizable,](https://github.com/valhuber/ApiLogicServer/blob/main/README.md#customize-and-debug) using a standard IDE.


&nbsp;&nbsp;

## 2. Collaborate using **Admin App**

As noted above, running screens are an excellent way to engage business user collaboration and ensure the 
system meets actual user needs.  Such collaboration typically leads in two important directions, as described below.

&nbsp;&nbsp;

#### 2a. Iterate Data Model

You may discover that the data model is incorrect (_"Wait!  Customers have multiple addresses!!"_).  

In a conventional system, this would mean revising the API and App.  However, since these are created instantly through automation, such iterations are trivial.

&nbsp;&nbsp;


#### 2b. Uncover TDD Scenarios

User Interfaces also spark insight about the Features ("Place Order") and Scenarios ("Check Credit"): _"When the customer places an order, we need to reject it if it exceeds the credit limit:._


&nbsp;&nbsp;

## 3. Define Scenarios in Behave

(e.g., `place_order.feature`)

TDD is designed for business use collaboration by making Features and Scenarios transparent.  So, the start of Behave is to define one or more `.feature` files.  For example:

< Figure TBD >

&nbsp;&nbsp;

### 3a. Add Custom Service

10 lines of Python (`api/customize_api.py`)
Next, we defined a custom service to add an order and it's Order Details, as [described here](https://github.com/valhuber/ApiLogicServer/blob/main/README.md#api-customization).

&nbsp;&nbsp;

## 4. Logic Specification

 ("cocktail napkin")

&nbsp;&nbsp;

## 5. Declare Logic: 21 rules

Business Logic is the heart of the system, enforcing our business policies.  These consist of multi-table constraints and derivations, and actions such as sending email and messages.  A core TDD objective is to define and test such behavior.

It's generally accepted that such domain-specific logic _must_ require domain-specific code.  The problem is that this is:
* **slow** (it's often nearly half the system)
* **opaque** to business users
* **painful to maintain** - it's no secret that developers hate maintenance, since it's less coding than the "archaeology" of first understanding existing code to understand where to insert the new logic

Ideally, we could capture TDD requirements as executable statements.

So, API Logic Server provides Logic Automation, where logic is implemented as:

* [Spreadsheet-like rules](https://github.com/valhuber/LogicBank/wiki/Examples) for multi-table derivations and constraints, and

* Python, to implement logic not addressed in rules such as sending email or messages

So, [instead of several hundred lines of code](https://github.com/valhuber/LogicBank/wiki/by-code), we declared 21 rules [(more details here)](https://github.com/valhuber/ApiLogicServer/blob/main/README.md#logic).  Rules are entered in Python, with code completion.  5 key rules are shown below:

<figure><img src="https://github.com/valhuber/ApiLogicServer/raw/main/images/docker/VSCode/nw-readme/declare-logic.png"></figure>

Unlike manual code, logic is 
* **automatically reused** - it is enforced as part of the API, so automatically shared across *all* screens and services.
* **automatically ordered** - maintenance is simply altering the rules; the system computes their execution order by automatically discovering their dependencies.  No more archaeology.
* **transparent** - business users can read the spreadsheet-like rules.


&nbsp;&nbsp;

>  Key Take-away: logic spreadsheet-like rules can dramatically reduce the effort for backend logic, and make it transparent

&nbsp;&nbsp;

## 6. Code/Run TDD Tests

Define and Run TDD Tests as shown below:

<figure><img src="https://github.com/valhuber/TDD/blob/main/images/TDD-ide.png?raw=true"></figure>

For more on TDD, [see here](https://github.com/valhuber/TDD/wiki/Stories-And-Behaviors).

&nbsp;&nbsp;

 (e.g., `place_order.py`)

Implement the actual tests in Python, using annotations to match tests and implementations.  In this project, the implementation is basically calling APIs to get old data, run transactions, and check results.

The rules fire as transactions are run, and produce [Logic Log output](https://github.com/valhuber/ApiLogicServer/wiki/Logic:-Rules-plus-Python#debugging).  The highlighted code on lines 50-51 signals that the Logic Log should be directed to files in `results_when`.  These are later used in Report Behave Logic, described below. 

With the server started, run your tests using Launch Configuration `Debug Behave Logic`.  It creates the following files:
1. `test/api_logic_server_behave/behave.log`
2. `results_when/<scenario-name>.log` (one for each scenario)

>  You can use the debugger to stop in a test and verify results


&nbsp;&nbsp;

## 7. **Create TDD/Logic Reports**

Run Launch Configuration `Report Behave Logic` to create `report_behave_logic.md`.  

This runs `report_behave_logic.py`, which
1. Reads your current `readme.md` file (text like you are reading now), and
2. Appends the [TDD Report:](#tdd-report) by processing the files created in step 3c
   1. Reading the `behave.log`, and
   2. Injecting the `results_when` Logic Log files


&nbsp;&nbsp;

>  Key Take-away: TDD makes *requirements and tests* transparent; rules make your *logic* transparent; combine them both into the [**TDD Report.**](#tdd-report)

&nbsp;&nbsp;

#### Working with TDD
For more information, see [Working with Behave.](https://github.com/valhuber/TDD/wiki/Working-With-Behave)

&nbsp;&nbsp;

# Business Agility


<figure><img src="https://github.com/valhuber/TDD/blob/main/images/business-agility.png?raw=true"></figure>

The underlying objective here is to promote _business agilty:_

1. **Working Software, *Now:*** the project creation process creates screens for business user collaboration
2. **Customer Collaboration:** 
   * Screen-based collaboration, as noted above
   * TDD is a transparent process for defining testable behaviors
   * Logic (unlike code) is *transparent* - business users can read it and collaborate (_"hey, you forgot to add tax"_).
      * This opens up the opportunity to combine the TDD Report _with a Logic report,_ as described below
3. **Responding to Change:**
   * Rebuild the App as requirements are uncovered
   * Alter logic, utilizing *automatic ordering* to keep things agile

&nbsp;&nbsp;

### Increased Transparency: TDD Report, _with logic_

This project illustrates you can extract the logic from the Logic Log, and insert it into the TDD output:
1. The TDD Report follows (converted to wiki format)

2. Click the __disclosure icons__ to see the rules actually used, including how they operate on the given scenario


&nbsp;
&nbsp;


# TDD Report
&nbsp;
&nbsp;
   * [Feature: About Sample](#feature-about-sample)
      * [Scenario: Transaction Processing](#scenario-transaction-processing)
   * [Feature: Application Integration](#feature-application-integration)
      * [Scenario: GET Customer](#scenario-get-customer)
      * [Scenario: GET Department](#scenario-get-department)
   * [Feature: Place Order](#feature-place-order)
      * [Scenario: Good Order Custom Service](#scenario-good-order-custom-service)
      * [Scenario: Bad Order Custom Service](#scenario-bad-order-custom-service)
      * [Scenario: Alter Item Qty to exceed credit](#scenario-alter-item-qty-to-exceed-credit)
      * [Scenario: Alter Required Date - adjust logic pruned](#scenario-alter-required-date---adjust-logic-pruned)
      * [Scenario: Set Shipped - adjust logic reuse](#scenario-set-shipped---adjust-logic-reuse)
      * [Scenario: Reset Shipped - adjust logic reuse](#scenario-reset-shipped---adjust-logic-reuse)
   * [Feature: Salary Change](#feature-salary-change)
      * [Scenario: Audit Salary Change](#scenario-audit-salary-change)
## Feature: About Sample  
  
&nbsp;
&nbsp;
### Scenario: Transaction Processing
&emsp;  Scenario: Transaction Processing  
&emsp;&emsp;    Given Sample Database  
&emsp;&emsp;    When Transactions are submitted  
&emsp;&emsp;    Then Enforce business policies with Logic (rules + code)  
<details>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Rules Used** in Scenario: Transaction Processing
```
```
**Logic Log** in Scenario: Transaction Processing
```
AbstractRule Bank[0x108dfcaf0] (loaded 2022-03-20 06:19:51.851110
Mapped Class[OrderDetail] rules
  Derive OrderDetail.UnitPrice as Copy(Product.UnitPrice
  Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...
  Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDat
Mapped Class[Order] rules
  Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None
  RowEvent Order.congratulate_sales_rep()
  Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None
Mapped Class[Customer] rules
  Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x108f528b0>
  Constraint Function: None
  Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108f5d280>
  Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None
Mapped Class[Product] rules
  Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x108f5d160>
  Derive Product.UnitsInStock as Formula (1): <function
Mapped Class[Employee] rules
  Constraint Function: <function declare_logic.<locals>.raise_over_20_percent at 0x108f5d9d0>
  RowEvent Employee.audit_by_event()
  Copy to: EmployeeAudi
Logic Bank - 21 rules loaded - 2022-03-20 06:21:27,941 - logic_logger - INF
```
</details>
  
&nbsp;
&nbsp;
## Feature: Application Integration  
  
&nbsp;
&nbsp;
### Scenario: GET Customer
&emsp;  Scenario: GET Customer  
&emsp;&emsp;    Given Customer Account: VINET  
&emsp;&emsp;    When GET Orders API  
&emsp;&emsp;    Then VINET retrieved  
  
&nbsp;
&nbsp;
### Scenario: GET Department
&emsp;  Scenario: GET Department  
&emsp;&emsp;    Given Department 2  
&emsp;&emsp;    When GET Department with SubDepartments API  
&emsp;&emsp;    Then SubDepartments returned  
  
&nbsp;
&nbsp;
## Feature: Place Order  
  
&nbsp;
&nbsp;
### Scenario: Good Order Custom Service
&emsp;  Scenario: Good Order Custom Service  
&emsp;&emsp;    Given Customer Account: ALFKI  
&emsp;&emsp;    When Good Order Placed  
&emsp;&emsp;    Then Logic adjusts Balance (demo: chain up)  
&emsp;&emsp;    Then Logic adusts Products Reordered  
&emsp;&emsp;    Then Logic adjusts aggregates down on delete order  
<details>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Rules Used** in Scenario: Good Order Custom Service
```
  Customer  
    1. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108f5d280>)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x108f528b0>)  
  Order  
    4. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    5. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    6. RowEvent Order.congratulate_sales_rep()   
  Product  
    7. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x108f5d160>)  
    8. Derive Product.UnitsInStock as Formula (1): <function>  
  
```
**Logic Log** in Scenario: Good Order Custom Service
```
Logic Phase:		ROW LOGIC(session=0x1095f6790) (sqlalchemy before_flush)			 - 2022-03-20 06:21:28,140 - logic_logger - INF
..Order[11115] {Delete - client} Id: 11115, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11.0000000000, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal: 56.00, Country: None, City: None, Ready: True, OrderDetailCount: 2  row: 0x109592490  session: 0x1095f6790 - 2022-03-20 06:21:28,141 - logic_logger - INF
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount, OrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2158.0000000000-->] 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount:  [16-->] 15, UnpaidOrderCount:  [11-->] 10  row: 0x109624580  session: 0x1095f6790 - 2022-03-20 06:21:28,142 - logic_logger - INF
..OrderDetail[2231] {Delete - client} Id: 2231, OrderId: 11115, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1, Discount: 0.0, Amount: 18.0000000000, ShippedDate: None  row: 0x109624340  session: 0x1095f6790 - 2022-03-20 06:21:28,143 - logic_logger - INF
....Product[1] {Update - Adjusting Product: UnitsShipped} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock: 39, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [0-->] -1  row: 0x10960dcd0  session: 0x1095f6790 - 2022-03-20 06:21:28,145 - logic_logger - INF
....Product[1] {Formula UnitsInStock} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock:  [39-->] 40, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [0-->] -1  row: 0x10960dcd0  session: 0x1095f6790 - 2022-03-20 06:21:28,145 - logic_logger - INF
..OrderDetail[2231] {No adjustment on deleted parent: Order} Id: 2231, OrderId: 11115, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1, Discount: 0.0, Amount: 18.0000000000, ShippedDate: None  row: 0x109624340  session: 0x1095f6790 - 2022-03-20 06:21:28,146 - logic_logger - INF
..OrderDetail[2232] {Delete - client} Id: 2232, OrderId: 11115, ProductId: 2, UnitPrice: 19.0000000000, Quantity: 2, Discount: 0.0, Amount: 38.0000000000, ShippedDate: None  row: 0x1096242e0  session: 0x1095f6790 - 2022-03-20 06:21:28,147 - logic_logger - INF
....Product[2] {Update - Adjusting Product: UnitsShipped} Id: 2, ProductName: Chang, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 24 - 12 oz bottles, UnitPrice: 19.0000000000, UnitsInStock: 15, UnitsOnOrder: 40, ReorderLevel: 25, Discontinued: 0, UnitsShipped:  [2-->] 0  row: 0x10962c880  session: 0x1095f6790 - 2022-03-20 06:21:28,148 - logic_logger - INF
....Product[2] {Formula UnitsInStock} Id: 2, ProductName: Chang, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 24 - 12 oz bottles, UnitPrice: 19.0000000000, UnitsInStock:  [15-->] 17, UnitsOnOrder: 40, ReorderLevel: 25, Discontinued: 0, UnitsShipped:  [2-->] 0  row: 0x10962c880  session: 0x1095f6790 - 2022-03-20 06:21:28,148 - logic_logger - INF
..OrderDetail[2232] {No adjustment on deleted parent: Order} Id: 2232, OrderId: 11115, ProductId: 2, UnitPrice: 19.0000000000, Quantity: 2, Discount: 0.0, Amount: 38.0000000000, ShippedDate: None  row: 0x1096242e0  session: 0x1095f6790 - 2022-03-20 06:21:28,149 - logic_logger - INF
Logic Phase:		COMMIT(session=0x1095f6790)   										 - 2022-03-20 06:21:28,149 - logic_logger - INF
..Order[11115] {Commit Event} Id: 11115, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11.0000000000, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal: 56.00, Country: None, City: None, Ready: True, OrderDetailCount: 2  row: 0x109592490  session: 0x1095f6790 - 2022-03-20 06:21:28,149 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Bad Order Custom Service
&emsp;  Scenario: Bad Order Custom Service  
&emsp;&emsp;    Given Customer Account: ALFKI  
&emsp;&emsp;    When Order Placed with excessive quantity  
&emsp;&emsp;    Then Rejected per Credit Limit  
&emsp;&emsp;    Then exceeds credit in response  
<details>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Rules Used** in Scenario: Bad Order Custom Service
```
  Customer  
    1. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108f5d280>)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x108f528b0>)  
    4. Constraint Function: None   
  Order  
    5. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    6. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
  OrderDetail  
    7. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
    8. Derive OrderDetail.UnitPrice as Copy(Product.UnitPrice)  
    9. Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]  
  Product  
    10. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x108f5d160>)  
    11. Derive Product.UnitsInStock as Formula (1): <function>  
  
```
**Logic Log** in Scenario: Bad Order Custom Service
```
Logic Phase:		ROW LOGIC(session=0x10962ce20) (sqlalchemy before_flush)			 - 2022-03-20 06:21:28,209 - logic_logger - INF
..Order[None] {Insert - client} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 10, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal: None, Country: None, City: None, Ready: None, OrderDetailCount: None  row: 0x10962c310  session: 0x10962ce20 - 2022-03-20 06:21:28,209 - logic_logger - INF
....Customer[ALFKI] {Update - Adjusting Customer: UnpaidOrderCount, OrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance: 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount:  [15-->] 16, UnpaidOrderCount:  [10-->] 11  row: 0x109646b80  session: 0x10962ce20 - 2022-03-20 06:21:28,212 - logic_logger - INF
..OrderDetail[None] {Insert - client} Id: None, OrderId: None, ProductId: 1, UnitPrice: None, Quantity: 1111, Discount: 0, Amount: None, ShippedDate: None  row: 0x10962c5b0  session: 0x10962ce20 - 2022-03-20 06:21:28,213 - logic_logger - INF
..OrderDetail[None] {copy_rules for role: Product - UnitPrice} Id: None, OrderId: None, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1111, Discount: 0, Amount: None, ShippedDate: None  row: 0x10962c5b0  session: 0x10962ce20 - 2022-03-20 06:21:28,215 - logic_logger - INF
..OrderDetail[None] {Formula Amount} Id: None, OrderId: None, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1111, Discount: 0, Amount: 19998.0000000000, ShippedDate: None  row: 0x10962c5b0  session: 0x10962ce20 - 2022-03-20 06:21:28,215 - logic_logger - INF
....Product[1] {Update - Adjusting Product: UnitsShipped} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock: 40, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [-1-->] 1110  row: 0x109646040  session: 0x10962ce20 - 2022-03-20 06:21:28,215 - logic_logger - INF
....Product[1] {Formula UnitsInStock} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock:  [40-->] -1071, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [-1-->] 1110  row: 0x109646040  session: 0x10962ce20 - 2022-03-20 06:21:28,216 - logic_logger - INF
....Order[None] {Update - Adjusting Order: AmountTotal, OrderDetailCount} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 10, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal:  [None-->] 19998.0000000000, Country: None, City: None, Ready: None, OrderDetailCount:  [None-->] 1  row: 0x10962c310  session: 0x10962ce20 - 2022-03-20 06:21:28,217 - logic_logger - INF
......Customer[ALFKI] {Update - Adjusting Customer: Balance} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 22100.0000000000, CreditLimit: 2300.0000000000, OrderCount: 16, UnpaidOrderCount: 11  row: 0x109646b80  session: 0x10962ce20 - 2022-03-20 06:21:28,218 - logic_logger - INF
......Customer[ALFKI] {Constraint Failure: balance (22100.0000000000) exceeds credit (2300.0000000000)} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 22100.0000000000, CreditLimit: 2300.0000000000, OrderCount: 16, UnpaidOrderCount: 11  row: 0x109646b80  session: 0x10962ce20 - 2022-03-20 06:21:28,218 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Alter Item Qty to exceed credit
&emsp;  Scenario: Alter Item Qty to exceed credit  
&emsp;&emsp;    Given Customer Account: ALFKI  
&emsp;&emsp;    When Order Detail Quantity altered very high  
&emsp;&emsp;    Then Rejected per Credit Limit  
&emsp;&emsp;    Then exceeds credit in response  
<details>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Rules Used** in Scenario: Alter Item Qty to exceed credit
```
  Customer  
    1. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108f5d280>)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x108f528b0>)  
    4. Constraint Function: None   
  Order  
    5. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    6. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
  OrderDetail  
    7. Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]  
  Product  
    8. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x108f5d160>)  
    9. Derive Product.UnitsInStock as Formula (1): <function>  
  
```
**Logic Log** in Scenario: Alter Item Qty to exceed credit
```
Logic Phase:		ROW LOGIC(session=0x10964fac0) (sqlalchemy before_flush)			 - 2022-03-20 06:21:28,270 - logic_logger - INF
..OrderDetail[1040] {Update - client} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount: 684.0000000000, ShippedDate: None  row: 0x10964f460  session: 0x10964fac0 - 2022-03-20 06:21:28,270 - logic_logger - INF
..OrderDetail[1040] {Formula Amount} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount:  [684.0000000000-->] 50616.0000000000, ShippedDate: None  row: 0x10964f460  session: 0x10964fac0 - 2022-03-20 06:21:28,271 - logic_logger - INF
..OrderDetail[1040] {Prune Formula: ShippedDate [['Order.ShippedDate']]} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount:  [684.0000000000-->] 50616.0000000000, ShippedDate: None  row: 0x10964f460  session: 0x10964fac0 - 2022-03-20 06:21:28,271 - logic_logger - INF
....Product[28] {Update - Adjusting Product: UnitsShipped} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock: 26, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] 1095  row: 0x10964f910  session: 0x10964fac0 - 2022-03-20 06:21:28,272 - logic_logger - INF
....Product[28] {Formula UnitsInStock} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock:  [26-->] -1069, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] 1095  row: 0x10964f910  session: 0x10964fac0 - 2022-03-20 06:21:28,273 - logic_logger - INF
....Order[10643] {Update - Adjusting Order: AmountTotal} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal:  [1086.00-->] 51018.0000000000, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x109646d00  session: 0x10964fac0 - 2022-03-20 06:21:28,275 - logic_logger - INF
......Customer[ALFKI] {Update - Adjusting Customer: Balance} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 52034.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount: 10  row: 0x109646c40  session: 0x10964fac0 - 2022-03-20 06:21:28,276 - logic_logger - INF
......Customer[ALFKI] {Constraint Failure: balance (52034.0000000000) exceeds credit (2300.0000000000)} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 52034.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount: 10  row: 0x109646c40  session: 0x10964fac0 - 2022-03-20 06:21:28,277 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Alter Required Date - adjust logic pruned
&emsp;  Scenario: Alter Required Date - adjust logic pruned  
&emsp;&emsp;    Given Customer Account: ALFKI  
&emsp;&emsp;    When Order RequiredDate altered (2013-10-13)  
&emsp;&emsp;    Then Balance not adjusted  
<details>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Rules Used** in Scenario: Alter Required Date - adjust logic pruned
```
  Customer  
    1. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108f5d280>)  
    2. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x108f528b0>)  
    3. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    4. RowEvent Order.congratulate_sales_rep()   
  
```
**Logic Log** in Scenario: Alter Required Date - adjust logic pruned
```
Logic Phase:		ROW LOGIC(session=0x109646bb0) (sqlalchemy before_flush)			 - 2022-03-20 06:21:28,325 - logic_logger - INF
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate:  [2013-10-13-->] 2013-10-13 00:00:00, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10964f460  session: 0x109646bb0 - 2022-03-20 06:21:28,326 - logic_logger - INF
Logic Phase:		COMMIT(session=0x109646bb0)   										 - 2022-03-20 06:21:28,327 - logic_logger - INF
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate:  [2013-10-13-->] 2013-10-13 00:00:00, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10964f460  session: 0x109646bb0 - 2022-03-20 06:21:28,327 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Set Shipped - adjust logic reuse
&emsp;  Scenario: Set Shipped - adjust logic reuse  
&emsp;&emsp;    Given Customer Account: ALFKI  
&emsp;&emsp;    When Order ShippedDate altered (2013-10-13)  
&emsp;&emsp;    Then Balance reduced 1086  
<details>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Rules Used** in Scenario: Set Shipped - adjust logic reuse
```
  Customer  
    1. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108f5d280>)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x108f528b0>)  
  Order  
    4. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    5. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    6. RowEvent Order.congratulate_sales_rep()   
  OrderDetail  
    7. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
  Product  
    8. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x108f5d160>)  
    9. Derive Product.UnitsInStock as Formula (1): <function>  
  
```
**Logic Log** in Scenario: Set Shipped - adjust logic reuse
```
Logic Phase:		ROW LOGIC(session=0x10964fe80) (sqlalchemy before_flush)			 - 2022-03-20 06:21:28,420 - logic_logger - INF
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [None-->] 2013-10-13, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10960d4f0  session: 0x10964fe80 - 2022-03-20 06:21:28,421 - logic_logger - INF
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 1016.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount:  [10-->] 9  row: 0x1095ab1c0  session: 0x10964fe80 - 2022-03-20 06:21:28,422 - logic_logger - INF
....OrderDetail[1040] {Update - Cascading Order.ShippedDate (,...)} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: None  row: 0x109592f10  session: 0x10964fe80 - 2022-03-20 06:21:28,425 - logic_logger - INF
....OrderDetail[1040] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: None  row: 0x109592f10  session: 0x10964fe80 - 2022-03-20 06:21:28,425 - logic_logger - INF
....OrderDetail[1040] {Formula ShippedDate} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate:  [None-->] 2013-10-13  row: 0x109592f10  session: 0x10964fe80 - 2022-03-20 06:21:28,425 - logic_logger - INF
......Product[28] {Update - Adjusting Product: UnitsShipped} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock: 26, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] -15  row: 0x10964f340  session: 0x10964fe80 - 2022-03-20 06:21:28,426 - logic_logger - INF
......Product[28] {Formula UnitsInStock} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock:  [26-->] 41, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] -15  row: 0x10964f340  session: 0x10964fe80 - 2022-03-20 06:21:28,427 - logic_logger - INF
....OrderDetail[1041] {Update - Cascading Order.ShippedDate (,...)} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: None  row: 0x109592c40  session: 0x10964fe80 - 2022-03-20 06:21:28,428 - logic_logger - INF
....OrderDetail[1041] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: None  row: 0x109592c40  session: 0x10964fe80 - 2022-03-20 06:21:28,428 - logic_logger - INF
....OrderDetail[1041] {Formula ShippedDate} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate:  [None-->] 2013-10-13  row: 0x109592c40  session: 0x10964fe80 - 2022-03-20 06:21:28,428 - logic_logger - INF
......Product[39] {Update - Adjusting Product: UnitsShipped} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock: 69, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [0-->] -21  row: 0x1095925b0  session: 0x10964fe80 - 2022-03-20 06:21:28,430 - logic_logger - INF
......Product[39] {Formula UnitsInStock} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock:  [69-->] 90, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [0-->] -21  row: 0x1095925b0  session: 0x10964fe80 - 2022-03-20 06:21:28,430 - logic_logger - INF
....OrderDetail[1042] {Update - Cascading Order.ShippedDate (,...)} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: None  row: 0x109592e80  session: 0x10964fe80 - 2022-03-20 06:21:28,431 - logic_logger - INF
....OrderDetail[1042] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: None  row: 0x109592e80  session: 0x10964fe80 - 2022-03-20 06:21:28,431 - logic_logger - INF
....OrderDetail[1042] {Formula ShippedDate} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate:  [None-->] 2013-10-13  row: 0x109592e80  session: 0x10964fe80 - 2022-03-20 06:21:28,432 - logic_logger - INF
......Product[46] {Update - Adjusting Product: UnitsShipped} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock: 95, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [0-->] -2  row: 0x109592580  session: 0x10964fe80 - 2022-03-20 06:21:28,433 - logic_logger - INF
......Product[46] {Formula UnitsInStock} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock:  [95-->] 97, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [0-->] -2  row: 0x109592580  session: 0x10964fe80 - 2022-03-20 06:21:28,433 - logic_logger - INF
Logic Phase:		COMMIT(session=0x10964fe80)   										 - 2022-03-20 06:21:28,434 - logic_logger - INF
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [None-->] 2013-10-13, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10960d4f0  session: 0x10964fe80 - 2022-03-20 06:21:28,434 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Reset Shipped - adjust logic reuse
&emsp;  Scenario: Reset Shipped - adjust logic reuse  
&emsp;&emsp;    Given Shipped Order  
&emsp;&emsp;    When Order ShippedDate set to None  
&emsp;&emsp;    Then Logic adjusts Balance by -1086  
<details>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Rules Used** in Scenario: Reset Shipped - adjust logic reuse
```
  Customer  
    1. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108f5d280>)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x108f528b0>)  
  Order  
    4. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    5. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    6. RowEvent Order.congratulate_sales_rep()   
  OrderDetail  
    7. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
  Product  
    8. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x108f5d160>)  
    9. Derive Product.UnitsInStock as Formula (1): <function>  
  
```
**Logic Log** in Scenario: Reset Shipped - adjust logic reuse
```
Logic Phase:		ROW LOGIC(session=0x1096466d0) (sqlalchemy before_flush)			 - 2022-03-20 06:21:28,530 - logic_logger - INF
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [2013-10-13-->] None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10956dac0  session: 0x1096466d0 - 2022-03-20 06:21:28,530 - logic_logger - INF
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [1016.0000000000-->] 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount:  [9-->] 10  row: 0x1096e45b0  session: 0x1096466d0 - 2022-03-20 06:21:28,531 - logic_logger - INF
....OrderDetail[1040] {Update - Cascading Order.ShippedDate (,...)} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: 2013-10-13  row: 0x1096e4cd0  session: 0x1096466d0 - 2022-03-20 06:21:28,533 - logic_logger - INF
....OrderDetail[1040] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: 2013-10-13  row: 0x1096e4cd0  session: 0x1096466d0 - 2022-03-20 06:21:28,534 - logic_logger - INF
....OrderDetail[1040] {Formula ShippedDate} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate:  [2013-10-13-->] None  row: 0x1096e4cd0  session: 0x1096466d0 - 2022-03-20 06:21:28,534 - logic_logger - INF
......Product[28] {Update - Adjusting Product: UnitsShipped} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock: 41, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [-15-->] 0  row: 0x109646040  session: 0x1096466d0 - 2022-03-20 06:21:28,535 - logic_logger - INF
......Product[28] {Formula UnitsInStock} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock:  [41-->] 26, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [-15-->] 0  row: 0x109646040  session: 0x1096466d0 - 2022-03-20 06:21:28,535 - logic_logger - INF
....OrderDetail[1041] {Update - Cascading Order.ShippedDate (,...)} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: 2013-10-13  row: 0x1096e4d30  session: 0x1096466d0 - 2022-03-20 06:21:28,536 - logic_logger - INF
....OrderDetail[1041] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: 2013-10-13  row: 0x1096e4d30  session: 0x1096466d0 - 2022-03-20 06:21:28,537 - logic_logger - INF
....OrderDetail[1041] {Formula ShippedDate} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate:  [2013-10-13-->] None  row: 0x1096e4d30  session: 0x1096466d0 - 2022-03-20 06:21:28,537 - logic_logger - INF
......Product[39] {Update - Adjusting Product: UnitsShipped} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock: 90, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [-21-->] 0  row: 0x109624160  session: 0x1096466d0 - 2022-03-20 06:21:28,538 - logic_logger - INF
......Product[39] {Formula UnitsInStock} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock:  [90-->] 69, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [-21-->] 0  row: 0x109624160  session: 0x1096466d0 - 2022-03-20 06:21:28,538 - logic_logger - INF
....OrderDetail[1042] {Update - Cascading Order.ShippedDate (,...)} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: 2013-10-13  row: 0x1096e4c70  session: 0x1096466d0 - 2022-03-20 06:21:28,539 - logic_logger - INF
....OrderDetail[1042] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: 2013-10-13  row: 0x1096e4c70  session: 0x1096466d0 - 2022-03-20 06:21:28,539 - logic_logger - INF
....OrderDetail[1042] {Formula ShippedDate} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate:  [2013-10-13-->] None  row: 0x1096e4c70  session: 0x1096466d0 - 2022-03-20 06:21:28,540 - logic_logger - INF
......Product[46] {Update - Adjusting Product: UnitsShipped} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock: 97, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [-2-->] 0  row: 0x109624610  session: 0x1096466d0 - 2022-03-20 06:21:28,541 - logic_logger - INF
......Product[46] {Formula UnitsInStock} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock:  [97-->] 95, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [-2-->] 0  row: 0x109624610  session: 0x1096466d0 - 2022-03-20 06:21:28,541 - logic_logger - INF
Logic Phase:		COMMIT(session=0x1096466d0)   										 - 2022-03-20 06:21:28,542 - logic_logger - INF
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [2013-10-13-->] None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10956dac0  session: 0x1096466d0 - 2022-03-20 06:21:28,542 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
## Feature: Salary Change  
  
&nbsp;
&nbsp;
### Scenario: Audit Salary Change
&emsp;  Scenario: Audit Salary Change  
&emsp;&emsp;    Given Customer Account: VINET  
&emsp;&emsp;    When Patch Salary to 200k  
&emsp;&emsp;    Then Salary_audit row created  
<details>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Rules Used** in Scenario: Audit Salary Change
```
  Employee  
    1. RowEvent Employee.audit_by_event()   
  
```
**Logic Log** in Scenario: Audit Salary Change
```
Logic Phase:		ROW LOGIC(session=0x1096e4610) (sqlalchemy before_flush)			 - 2022-03-20 06:21:28,590 - logic_logger - INF
..Employee[5] {Update - client} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [95000.0000000000-->] 200000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x1096e4520  session: 0x1096e4610 - 2022-03-20 06:21:28,590 - logic_logger - INF
..Employee[5] {BEGIN Copy to: EmployeeAudit} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [95000.0000000000-->] 200000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x1096e4520  session: 0x1096e4610 - 2022-03-20 06:21:28,592 - logic_logger - INF
....EmployeeAudit[None] {Insert - Copy EmployeeAudit} Id: None, Title: Sales Manager, Salary: 200000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: None  row: 0x1096e41f0  session: 0x1096e4610 - 2022-03-20 06:21:28,593 - logic_logger - INF
....EmployeeAudit[None] {early_row_event_all_classes - handle_all sets 'Created_on} Id: None, Title: Sales Manager, Salary: 200000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: 2022-03-20 06:21:28.593443  row: 0x1096e41f0  session: 0x1096e4610 - 2022-03-20 06:21:28,593 - logic_logger - INF
Logic Phase:		COMMIT(session=0x1096e4610)   										 - 2022-03-20 06:21:28,593 - logic_logger - INF
..Employee[5] {Commit Event} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [95000.0000000000-->] 200000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x1096e4520  session: 0x1096e4610 - 2022-03-20 06:21:28,594 - logic_logger - INF

```
</details>
  
4 features passed, 0 failed, 0 skipped  
10 scenarios passed, 0 failed, 0 skipped  
34 steps passed, 0 failed, 0 skipped, 0 undefined  
Took 0m0.809s  