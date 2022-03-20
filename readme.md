# TDD - Test Driven Development, with Logic Traceability

This project uses the sample app of [API Logic Server](https://github.com/valhuber/ApiLogicServer/blob/main/README.md) to illustrate:
  
1. **Rapid project creation and customization:** using API Logic Server, for 1-command creation of projects providing User Interfaces and APIs from a database.  Runnng screens are an excellent way to engage business user collaboration.

1. **Logic Automation:** using spreadsheet-like rules for dramatically reduce backend code, and make logic transparent to the team.

1. **Transparent TDD Testing:** using [behave](https://behave.readthedocs.io/en/stable/tutorial.html) (a [TDD](http://dannorth.net/introducing-bdd/) framework) for defining systems, to promote Agile collaboration with business users.  You define Features and Scenarios (tests) in `behave`, with underlying Python test implementations.

2. **Transparent Test / Logic Tracing:** further promote Agile collaboration, by making logic transparent and integrated with Testing, in this generated `readme.md` (see the [TDD Report,](#tdd-report) at end).
  
&nbsp;&nbsp;

# Confirm Project Installation: Install, Test Run

This project is the API Logic Server sample.  Install and run as described below.

<details>
<summary>Use the following procedure to install and test</summary>

&nbsp;&nbsp;

## 1. Install API Logic Server

Installation differs slightly, depending on whether you are using `venv` or docker.

&nbsp;&nbsp;

#### 1a. Using 'venv`

If you are using `venv`: the usual (if cryptography fails, get a recent version of pip):
  
```
python -m venv venv
source venv/bin/activate  # windows venv\Scripts\activate
pip install -r requirements.txt
```

&nbsp;&nbsp;

#### 1b. Or, using Docker

If you are using docker, just accept the default docker (must be current).

```
cd TDD         # directory of API Logic Server projects on local host

# Start (installs if required) the API Logic Server docker container
docker run -it --name api_logic_server --rm -p 5656:5656 -p 5002:5002 -v ${PWD}:/localhost apilogicserver/api_logic_server
```

ApiLogicServer create-and-run --project_name=/localhost/ApiLogicProject --db_url=

&nbsp;&nbsp;

## 2. Start the API Logic Server

Open the project in VS Code, and run launch configuration `ApiLogicServer`.

&nbsp;&nbsp;

## 3. Execute the TDD Test

Run launch configuration `Debug Behave Logic`.

&nbsp;&nbsp;

## 4. Run the TDD Report

Run Launch Configuration `Report Behave Logic` to create `report_behave_logic.md`.  Examine in your IDE.

</details>

&nbsp;&nbsp;

# How this project was created

This is the sample project from API Logic Server, based on the Northwind database:

<figure><img src="https://github.com/valhuber/LogicBank/raw/main/images/nw.png"></figure>

The created project provides the User Interface and API described below, and implements the transactional logic described in the [TDD Report.](#tdd-report).  It was created, customized and tested as described in the subsections below.

&nbsp;&nbsp;

## 1. Create project with API Logic Server

With API Logic Server installed, we created the project with this command, using `venv` based installs:

```
ApiLogicServer create db_url= project_name=TDD
```

or, like this, using docker-based installs:
```
ApiLogicServer create-and-run --project_name=/localhost/ApiLogicProject --db_url=
```

This creates an executable project that provides:

&nbsp;&nbsp;

#### 1a. An **Admin App**

The app shown below [(more detail here)](https://github.com/valhuber/ApiLogicServer#admin-app-multi-page-multi-table-automatic-joins) is suitable for initial business user collaboration to confirm the data model structure, and basic _back office_ data maintenance.

You can [customize it](https://github.com/valhuber/ApiLogicServer#admin-app-customization) by editing a simple `yaml`file (e.g, field captions, ordering etc.)

<figure><img src="https://github.com/valhuber/ApiLogicServer/wiki/images/ui-admin/run-admin-app.png?raw=true"></figure>

&nbsp;&nbsp;

#### 1b. An **API**

An API is created for application integration, and creating custom User Interfaces.  The API enforces the business logic described below.

The [created project is customizable,](https://github.com/valhuber/ApiLogicServer/blob/main/README.md#customize-and-debug) using a standard IDE.

&nbsp;&nbsp;

##### Fix `models.py` for cascade delete
  
The tests perform cascade delete operations.  The `models.py` file was altered [as described here](https://github.com/valhuber/ApiLogicServer/wiki#edit-modelspy-referential-integrity-eg-sqlite).

&nbsp;&nbsp;

>  Key Take-away: instead of weeks of effort, you have an Admin App and API, ready for business user collaboration

&nbsp;&nbsp;

## 2. Customize using your IDE

We customized the created project by adding logic and a custom service, as described below.

&nbsp;&nbsp;

### 2a. Add Logic: 21 rules (`logic/declare_logic.py`) - not hundreds of lines of code
The core of TDD is to test behavior, in this case transaction behavior.  API Logic Server provides Logic Automation, where logic is implemented as:

* [Spreadsheet-like rules](https://github.com/valhuber/LogicBank/wiki/Examples) for multi-table derivations and constraints, and

* Python, to implement logic not addressed in rules

So, [instead of several hundred lines of code](https://github.com/valhuber/LogicBank/wiki/by-code), we declared 21 rules [(more details here)](https://github.com/valhuber/ApiLogicServer/blob/main/README.md#logic).  5 key rules are shown below:

<figure><img src="https://github.com/valhuber/ApiLogicServer/raw/main/images/docker/VSCode/nw-readme/declare-logic.png"></figure>


&nbsp;&nbsp;

>  Key Take-away: logic spreadsheet-like rules can dramatically reduce backend logic

&nbsp;&nbsp;

### 2b. Add Custom Service: 10 lines of Python (`api/customize_api.py`)
Next, we defined a custom service to add an order and it's Order Details, as [described here](https://github.com/valhuber/ApiLogicServer/blob/main/README.md#api-customization).

&nbsp;&nbsp;

## 3. Define and Run TDD Tests

Define and Run TDD Tests as shown below:

<figure><img src="https://github.com/valhuber/TDD/blob/main/images/TDD-overview.png?raw=true"></figure>

For more on TDD, [see here](https://github.com/valhuber/TDD/wiki/Stories-And-Behaviors).

&nbsp;&nbsp;

#### 3a. Define Tests (e.g., `place_order.feature`)

TDD is designed for business use collaboration by making Features and Scenarios transparent.  So, the start of Behave is to define one or more `.feature` files.  See the example above.

&nbsp;&nbsp;

#### 3b. Implement Tests (e.g., `place_order.py`)

Implement the actual tests in Python, using annotations to match tests and implementations.  In this project, the implementation is basically calling APIs to get old data, run transactions, and check results.

The rules fire as transactions are run, and produce [Logic Log output](https://github.com/valhuber/ApiLogicServer/wiki/Logic:-Rules-plus-Python#debugging).  The highlight code on lines 50-51 signals that the Logic Log should be directed to files in `results_when`.  These are later used in Report Behave Logic, described below.

&nbsp;&nbsp;

#### 3c. Run Tests, using Launch Configuration `Debug Behave Logic`

With the server started, run your tests using Launch Configuration `Debug Behave Logic`:
1. You can use the debugger to stop in a test and verify results
2. When your test is running, run it one last time to create the `behave.log`, like this:

`
cd test/api_logic_server_behave
behave > behave.log
`

&nbsp;&nbsp;

#### 3d. Create TDD/Logic Reports, by running Launch Configuration `Report Behave Logic`

Run Launch Configuration `Report Behave Logic` to create `report_behave_logic.md`.  

This runs `report_behave_logic.py`, which
1. Reads your current `readme.md` file (text like you are reading now), and
2. Appends the [TDD Report:](#tdd-report) by
   1. Reading the `behave.log` from step 3c
   2. Injecting the `results_when` Logic Log files


&nbsp;&nbsp;

>  Key Take-away: TDD makes *requirements and tests* transparent; rules make your *logic* transparent; combine them both into the [**TDD Report.**](#tdd-report)

&nbsp;&nbsp;

#### Working with TDD
For more information, see [Working with Behave.](https://github.com/valhuber/TDD/wiki/Working-With-Behave)

&nbsp;&nbsp;

# Business Agility
The underlying objective here is to promote _business agilty:_

1. TDD promotes transparent and testable behaviors
2. Unlike code, logic is transparent - business users can read it and collaborate (_"hey, you forgot to add tax"_)


<figure><img src="https://github.com/valhuber/TDD/blob/main/images/business-agility.png?raw=true"></figure>

### Increased Transparency: TDD Report, _with logic_

This project illustrates you can extract the logic from the Logic Log, and insert it into the TDD output:
1. The TDD Report follows (converted to wiki format)

2. Click the __disclosure icons__ to see the rules actually used, including how they operate on the given scenario

  
&nbsp;&nbsp;

# TDD Report
&nbsp;
&nbsp;
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
AbstractRule Bank[0x107170af0] (loaded 2022-03-17 19:23:55.973607)		##   - 2022-03-17 19:24:04,654 - logic_logger - INFO
Mapped Class[OrderDetail] rules:		##   - 2022-03-17 19:24:04,654 - logic_logger - INFO
  Derive OrderDetail.UnitPrice as Copy(Product.UnitPrice)		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
Mapped Class[Order] rules:		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  RowEvent Order.congratulate_sales_rep() 		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
Mapped Class[Customer] rules:		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x1072c6940>)		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  Constraint Function: None 		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x1072e9310>)		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
Mapped Class[Product] rules:		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x1072e91f0>)		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  Derive Product.UnitsInStock as Formula (1): <function>		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
Mapped Class[Employee] rules:		##   - 2022-03-17 19:24:04,655 - logic_logger - INFO
  Constraint Function: <function declare_logic.<locals>.raise_over_20_percent at 0x1072e9a60> 		##   - 2022-03-17 19:24:04,656 - logic_logger - INFO
  RowEvent Employee.audit_by_event() 		##   - 2022-03-17 19:24:04,656 - logic_logger - INFO
  Copy to: EmployeeAudit		##   - 2022-03-17 19:24:04,656 - logic_logger - INFO
Logic Bank - 21 rules loaded - 2022-03-17 19:24:04,656 - logic_logger - INFO
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
unable to find LogicLog file: results_when/GET_Customer.log
  
&nbsp;
&nbsp;
### Scenario: GET Department
&emsp;  Scenario: GET Department  
&emsp;&emsp;    Given Department 2  
&emsp;&emsp;    When GET Department with SubDepartments API  
&emsp;&emsp;    Then SubDepartments returned  
unable to find LogicLog file: results_when/GET_Department.log
  
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
    1. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x1072e9310>)  
    2. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x1072c6940>)  
  Order  
    4. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    5. RowEvent Order.congratulate_sales_rep()   
    6. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
  Product  
    7. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x1072e91f0>)  
    8. Derive Product.UnitsInStock as Formula (1): <function>  
  
 - 2022-03-17 19:24:04,804 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x107969790)   (sqlalchemy flush processing)       	 - 2022-03-17 19:24:04,804 - logic_logger - INFO  
```
**Logic Log** in Scenario: Good Order Custom Service
```
Logic Phase:		ROW LOGIC(session=0x107969790) (sqlalchemy before_flush)			 - 2022-03-17 19:24:04,795 - logic_logger - INFO
..Order[11108] {Delete - client} Id: 11108, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11.0000000000, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal: 56.00, Country: None, City: None, Ready: True, OrderDetailCount: 2  row: 0x107980bb0  session: 0x107969790 - 2022-03-17 19:24:04,795 - logic_logger - INFO
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount, OrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2158.0000000000-->] 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount:  [16-->] 15, UnpaidOrderCount:  [11-->] 10  row: 0x107997580  session: 0x107969790 - 2022-03-17 19:24:04,796 - logic_logger - INFO
..OrderDetail[2217] {Delete - client} Id: 2217, OrderId: 11108, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1, Discount: 0.0, Amount: 18.0000000000, ShippedDate: None  row: 0x107997340  session: 0x107969790 - 2022-03-17 19:24:04,797 - logic_logger - INFO
....Product[1] {Update - Adjusting Product: UnitsShipped} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock: 39, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [0-->] -1  row: 0x1079805b0  session: 0x107969790 - 2022-03-17 19:24:04,799 - logic_logger - INFO
....Product[1] {Formula UnitsInStock} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock:  [39-->] 40, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [0-->] -1  row: 0x1079805b0  session: 0x107969790 - 2022-03-17 19:24:04,799 - logic_logger - INFO
..OrderDetail[2217] {No adjustment on deleted parent: Order} Id: 2217, OrderId: 11108, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1, Discount: 0.0, Amount: 18.0000000000, ShippedDate: None  row: 0x107997340  session: 0x107969790 - 2022-03-17 19:24:04,800 - logic_logger - INFO
..OrderDetail[2218] {Delete - client} Id: 2218, OrderId: 11108, ProductId: 2, UnitPrice: 19.0000000000, Quantity: 2, Discount: 0.0, Amount: 38.0000000000, ShippedDate: None  row: 0x1079972e0  session: 0x107969790 - 2022-03-17 19:24:04,800 - logic_logger - INFO
....Product[2] {Update - Adjusting Product: UnitsShipped} Id: 2, ProductName: Chang, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 24 - 12 oz bottles, UnitPrice: 19.0000000000, UnitsInStock: 15, UnitsOnOrder: 40, ReorderLevel: 25, Discontinued: 0, UnitsShipped:  [2-->] 0  row: 0x10799f880  session: 0x107969790 - 2022-03-17 19:24:04,801 - logic_logger - INFO
....Product[2] {Formula UnitsInStock} Id: 2, ProductName: Chang, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 24 - 12 oz bottles, UnitPrice: 19.0000000000, UnitsInStock:  [15-->] 17, UnitsOnOrder: 40, ReorderLevel: 25, Discontinued: 0, UnitsShipped:  [2-->] 0  row: 0x10799f880  session: 0x107969790 - 2022-03-17 19:24:04,802 - logic_logger - INFO
..OrderDetail[2218] {No adjustment on deleted parent: Order} Id: 2218, OrderId: 11108, ProductId: 2, UnitPrice: 19.0000000000, Quantity: 2, Discount: 0.0, Amount: 38.0000000000, ShippedDate: None  row: 0x1079972e0  session: 0x107969790 - 2022-03-17 19:24:04,802 - logic_logger - INFO
Logic Phase:		COMMIT(session=0x107969790)   										 - 2022-03-17 19:24:04,803 - logic_logger - INFO
..Order[11108] {Commit Event} Id: 11108, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11.0000000000, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal: 56.00, Country: None, City: None, Ready: True, OrderDetailCount: 2  row: 0x107980bb0  session: 0x107969790 - 2022-03-17 19:24:04,803 - logic_logger - INFO

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
    1. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x1072e9310>)  
    2. Constraint Function: None   
    3. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    4. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x1072c6940>)  
  Order  
    5. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    6. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
  OrderDetail  
    7. Derive OrderDetail.UnitPrice as Copy(Product.UnitPrice)  
    8. Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]  
    9. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
  Product  
    10. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x1072e91f0>)  
    11. Derive Product.UnitsInStock as Formula (1): <function>  
  
 - 2022-03-17 19:24:04,854 - logic_logger - INFO  
```
**Logic Log** in Scenario: Bad Order Custom Service
```
Logic Phase:		ROW LOGIC(session=0x10799fe20) (sqlalchemy before_flush)			 - 2022-03-17 19:24:04,844 - logic_logger - INFO
..Order[None] {Insert - client} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 10, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal: None, Country: None, City: None, Ready: None, OrderDetailCount: None  row: 0x10799f310  session: 0x10799fe20 - 2022-03-17 19:24:04,844 - logic_logger - INFO
....Customer[ALFKI] {Update - Adjusting Customer: UnpaidOrderCount, OrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance: 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount:  [15-->] 16, UnpaidOrderCount:  [10-->] 11  row: 0x1079c0b80  session: 0x10799fe20 - 2022-03-17 19:24:04,847 - logic_logger - INFO
..OrderDetail[None] {Insert - client} Id: None, OrderId: None, ProductId: 1, UnitPrice: None, Quantity: 1111, Discount: 0, Amount: None, ShippedDate: None  row: 0x10799f5b0  session: 0x10799fe20 - 2022-03-17 19:24:04,848 - logic_logger - INFO
..OrderDetail[None] {copy_rules for role: Product - UnitPrice} Id: None, OrderId: None, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1111, Discount: 0, Amount: None, ShippedDate: None  row: 0x10799f5b0  session: 0x10799fe20 - 2022-03-17 19:24:04,849 - logic_logger - INFO
..OrderDetail[None] {Formula Amount} Id: None, OrderId: None, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1111, Discount: 0, Amount: 19998.0000000000, ShippedDate: None  row: 0x10799f5b0  session: 0x10799fe20 - 2022-03-17 19:24:04,850 - logic_logger - INFO
....Product[1] {Update - Adjusting Product: UnitsShipped} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock: 40, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [-1-->] 1110  row: 0x1079c0040  session: 0x10799fe20 - 2022-03-17 19:24:04,850 - logic_logger - INFO
....Product[1] {Formula UnitsInStock} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock:  [40-->] -1071, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [-1-->] 1110  row: 0x1079c0040  session: 0x10799fe20 - 2022-03-17 19:24:04,851 - logic_logger - INFO
....Order[None] {Update - Adjusting Order: AmountTotal, OrderDetailCount} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 10, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal:  [None-->] 19998.0000000000, Country: None, City: None, Ready: None, OrderDetailCount:  [None-->] 1  row: 0x10799f310  session: 0x10799fe20 - 2022-03-17 19:24:04,851 - logic_logger - INFO
......Customer[ALFKI] {Update - Adjusting Customer: Balance} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 22100.0000000000, CreditLimit: 2300.0000000000, OrderCount: 16, UnpaidOrderCount: 11  row: 0x1079c0b80  session: 0x10799fe20 - 2022-03-17 19:24:04,852 - logic_logger - INFO
......Customer[ALFKI] {Constraint Failure: balance (22100.0000000000) exceeds credit (2300.0000000000)} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 22100.0000000000, CreditLimit: 2300.0000000000, OrderCount: 16, UnpaidOrderCount: 11  row: 0x1079c0b80  session: 0x10799fe20 - 2022-03-17 19:24:04,853 - logic_logger - INFO

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
    1. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x1072e9310>)  
    2. Constraint Function: None   
    3. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    4. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x1072c6940>)  
  Order  
    5. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    6. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
  OrderDetail  
    7. Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]  
  Product  
    8. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x1072e91f0>)  
    9. Derive Product.UnitsInStock as Formula (1): <function>  
  
 - 2022-03-17 19:24:04,890 - logic_logger - INFO  
```
**Logic Log** in Scenario: Alter Item Qty to exceed credit
```
Logic Phase:		ROW LOGIC(session=0x1079c2ac0) (sqlalchemy before_flush)			 - 2022-03-17 19:24:04,883 - logic_logger - INFO
..OrderDetail[1040] {Update - client} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount: 684.0000000000, ShippedDate: None  row: 0x1079c2460  session: 0x1079c2ac0 - 2022-03-17 19:24:04,883 - logic_logger - INFO
..OrderDetail[1040] {Formula Amount} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount:  [684.0000000000-->] 50616.0000000000, ShippedDate: None  row: 0x1079c2460  session: 0x1079c2ac0 - 2022-03-17 19:24:04,884 - logic_logger - INFO
..OrderDetail[1040] {Prune Formula: ShippedDate [['Order.ShippedDate']]} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount:  [684.0000000000-->] 50616.0000000000, ShippedDate: None  row: 0x1079c2460  session: 0x1079c2ac0 - 2022-03-17 19:24:04,884 - logic_logger - INFO
....Product[28] {Update - Adjusting Product: UnitsShipped} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock: 26, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] 1095  row: 0x1079c2910  session: 0x1079c2ac0 - 2022-03-17 19:24:04,885 - logic_logger - INFO
....Product[28] {Formula UnitsInStock} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock:  [26-->] -1069, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] 1095  row: 0x1079c2910  session: 0x1079c2ac0 - 2022-03-17 19:24:04,885 - logic_logger - INFO
....Order[10643] {Update - Adjusting Order: AmountTotal} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal:  [1086.00-->] 51018.0000000000, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x1079c0d00  session: 0x1079c2ac0 - 2022-03-17 19:24:04,887 - logic_logger - INFO
......Customer[ALFKI] {Update - Adjusting Customer: Balance} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 52034.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount: 10  row: 0x1079c0c40  session: 0x1079c2ac0 - 2022-03-17 19:24:04,889 - logic_logger - INFO
......Customer[ALFKI] {Constraint Failure: balance (52034.0000000000) exceeds credit (2300.0000000000)} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 52034.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount: 10  row: 0x1079c0c40  session: 0x1079c2ac0 - 2022-03-17 19:24:04,889 - logic_logger - INFO

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
    1. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x1072e9310>)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x1072c6940>)  
  Order  
    4. RowEvent Order.congratulate_sales_rep()   
  
 - 2022-03-17 19:24:04,920 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x1079aab20)   (sqlalchemy flush processing)       	 - 2022-03-17 19:24:04,920 - logic_logger - INFO  
```
**Logic Log** in Scenario: Alter Required Date - adjust logic pruned
```
Logic Phase:		ROW LOGIC(session=0x1079aab20) (sqlalchemy before_flush)			 - 2022-03-17 19:24:04,918 - logic_logger - INFO
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate:  [2013-10-13-->] 2013-10-13 00:00:00, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x1079c04c0  session: 0x1079aab20 - 2022-03-17 19:24:04,918 - logic_logger - INFO
Logic Phase:		COMMIT(session=0x1079aab20)   										 - 2022-03-17 19:24:04,919 - logic_logger - INFO
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate:  [2013-10-13-->] 2013-10-13 00:00:00, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x1079c04c0  session: 0x1079aab20 - 2022-03-17 19:24:04,920 - logic_logger - INFO

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
    1. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x1072e9310>)  
    2. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x1072c6940>)  
  Order  
    4. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    5. RowEvent Order.congratulate_sales_rep()   
    6. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
  OrderDetail  
    7. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
  Product  
    8. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x1072e91f0>)  
    9. Derive Product.UnitsInStock as Formula (1): <function>  
  
 - 2022-03-17 19:24:04,983 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x1079972b0)   (sqlalchemy flush processing)       	 - 2022-03-17 19:24:04,983 - logic_logger - INFO  
```
**Logic Log** in Scenario: Set Shipped - adjust logic reuse
```
Logic Phase:		ROW LOGIC(session=0x1079972b0) (sqlalchemy before_flush)			 - 2022-03-17 19:24:04,969 - logic_logger - INFO
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [None-->] 2013-10-13, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x107989eb0  session: 0x1079972b0 - 2022-03-17 19:24:04,970 - logic_logger - INFO
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 1016.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount:  [10-->] 9  row: 0x10791f730  session: 0x1079972b0 - 2022-03-17 19:24:04,971 - logic_logger - INFO
....OrderDetail[1040] {Update - Cascading Order.ShippedDate (,...)} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: None  row: 0x107905e20  session: 0x1079972b0 - 2022-03-17 19:24:04,973 - logic_logger - INFO
....OrderDetail[1040] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: None  row: 0x107905e20  session: 0x1079972b0 - 2022-03-17 19:24:04,973 - logic_logger - INFO
....OrderDetail[1040] {Formula ShippedDate} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate:  [None-->] 2013-10-13  row: 0x107905e20  session: 0x1079972b0 - 2022-03-17 19:24:04,974 - logic_logger - INFO
......Product[28] {Update - Adjusting Product: UnitsShipped} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock: 26, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] -15  row: 0x10790c4c0  session: 0x1079972b0 - 2022-03-17 19:24:04,974 - logic_logger - INFO
......Product[28] {Formula UnitsInStock} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock:  [26-->] 41, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] -15  row: 0x10790c4c0  session: 0x1079972b0 - 2022-03-17 19:24:04,975 - logic_logger - INFO
....OrderDetail[1041] {Update - Cascading Order.ShippedDate (,...)} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: None  row: 0x107905cd0  session: 0x1079972b0 - 2022-03-17 19:24:04,976 - logic_logger - INFO
....OrderDetail[1041] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: None  row: 0x107905cd0  session: 0x1079972b0 - 2022-03-17 19:24:04,976 - logic_logger - INFO
....OrderDetail[1041] {Formula ShippedDate} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate:  [None-->] 2013-10-13  row: 0x107905cd0  session: 0x1079972b0 - 2022-03-17 19:24:04,976 - logic_logger - INFO
......Product[39] {Update - Adjusting Product: UnitsShipped} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock: 69, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [0-->] -21  row: 0x10790c820  session: 0x1079972b0 - 2022-03-17 19:24:04,977 - logic_logger - INFO
......Product[39] {Formula UnitsInStock} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock:  [69-->] 90, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [0-->] -21  row: 0x10790c820  session: 0x1079972b0 - 2022-03-17 19:24:04,978 - logic_logger - INFO
....OrderDetail[1042] {Update - Cascading Order.ShippedDate (,...)} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: None  row: 0x107905e50  session: 0x1079972b0 - 2022-03-17 19:24:04,978 - logic_logger - INFO
....OrderDetail[1042] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: None  row: 0x107905e50  session: 0x1079972b0 - 2022-03-17 19:24:04,979 - logic_logger - INFO
....OrderDetail[1042] {Formula ShippedDate} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate:  [None-->] 2013-10-13  row: 0x107905e50  session: 0x1079972b0 - 2022-03-17 19:24:04,979 - logic_logger - INFO
......Product[46] {Update - Adjusting Product: UnitsShipped} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock: 95, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [0-->] -2  row: 0x10790cd30  session: 0x1079972b0 - 2022-03-17 19:24:04,980 - logic_logger - INFO
......Product[46] {Formula UnitsInStock} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock:  [95-->] 97, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [0-->] -2  row: 0x10790cd30  session: 0x1079972b0 - 2022-03-17 19:24:04,980 - logic_logger - INFO
Logic Phase:		COMMIT(session=0x1079972b0)   										 - 2022-03-17 19:24:04,981 - logic_logger - INFO
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [None-->] 2013-10-13, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x107989eb0  session: 0x1079972b0 - 2022-03-17 19:24:04,981 - logic_logger - INFO

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
    1. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x1072e9310>)  
    2. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x1072c6940>)  
  Order  
    4. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    5. RowEvent Order.congratulate_sales_rep()   
    6. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
  OrderDetail  
    7. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
  Product  
    8. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x1072e91f0>)  
    9. Derive Product.UnitsInStock as Formula (1): <function>  
  
 - 2022-03-17 19:24:05,048 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x1078dffd0)   (sqlalchemy flush processing)       	 - 2022-03-17 19:24:05,048 - logic_logger - INFO  
```
**Logic Log** in Scenario: Reset Shipped - adjust logic reuse
```
Logic Phase:		ROW LOGIC(session=0x1078dffd0) (sqlalchemy before_flush)			 - 2022-03-17 19:24:05,034 - logic_logger - INFO
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [2013-10-13-->] None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10778a460  session: 0x1078dffd0 - 2022-03-17 19:24:05,035 - logic_logger - INFO
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [1016.0000000000-->] 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount:  [9-->] 10  row: 0x107a5a5b0  session: 0x1078dffd0 - 2022-03-17 19:24:05,036 - logic_logger - INFO
....OrderDetail[1040] {Update - Cascading Order.ShippedDate (,...)} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: 2013-10-13  row: 0x107a5acd0  session: 0x1078dffd0 - 2022-03-17 19:24:05,038 - logic_logger - INFO
....OrderDetail[1040] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: 2013-10-13  row: 0x107a5acd0  session: 0x1078dffd0 - 2022-03-17 19:24:05,038 - logic_logger - INFO
....OrderDetail[1040] {Formula ShippedDate} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate:  [2013-10-13-->] None  row: 0x107a5acd0  session: 0x1078dffd0 - 2022-03-17 19:24:05,039 - logic_logger - INFO
......Product[28] {Update - Adjusting Product: UnitsShipped} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock: 41, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [-15-->] 0  row: 0x1079c2f40  session: 0x1078dffd0 - 2022-03-17 19:24:05,040 - logic_logger - INFO
......Product[28] {Formula UnitsInStock} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock:  [41-->] 26, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [-15-->] 0  row: 0x1079c2f40  session: 0x1078dffd0 - 2022-03-17 19:24:05,040 - logic_logger - INFO
....OrderDetail[1041] {Update - Cascading Order.ShippedDate (,...)} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: 2013-10-13  row: 0x107a5ad30  session: 0x1078dffd0 - 2022-03-17 19:24:05,041 - logic_logger - INFO
....OrderDetail[1041] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: 2013-10-13  row: 0x107a5ad30  session: 0x1078dffd0 - 2022-03-17 19:24:05,041 - logic_logger - INFO
....OrderDetail[1041] {Formula ShippedDate} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate:  [2013-10-13-->] None  row: 0x107a5ad30  session: 0x1078dffd0 - 2022-03-17 19:24:05,042 - logic_logger - INFO
......Product[39] {Update - Adjusting Product: UnitsShipped} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock: 90, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [-21-->] 0  row: 0x107997a30  session: 0x1078dffd0 - 2022-03-17 19:24:05,042 - logic_logger - INFO
......Product[39] {Formula UnitsInStock} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock:  [90-->] 69, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [-21-->] 0  row: 0x107997a30  session: 0x1078dffd0 - 2022-03-17 19:24:05,043 - logic_logger - INFO
....OrderDetail[1042] {Update - Cascading Order.ShippedDate (,...)} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: 2013-10-13  row: 0x107a5ac70  session: 0x1078dffd0 - 2022-03-17 19:24:05,044 - logic_logger - INFO
....OrderDetail[1042] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: 2013-10-13  row: 0x107a5ac70  session: 0x1078dffd0 - 2022-03-17 19:24:05,044 - logic_logger - INFO
....OrderDetail[1042] {Formula ShippedDate} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate:  [2013-10-13-->] None  row: 0x107a5ac70  session: 0x1078dffd0 - 2022-03-17 19:24:05,044 - logic_logger - INFO
......Product[46] {Update - Adjusting Product: UnitsShipped} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock: 97, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [-2-->] 0  row: 0x1079aaca0  session: 0x1078dffd0 - 2022-03-17 19:24:05,045 - logic_logger - INFO
......Product[46] {Formula UnitsInStock} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock:  [97-->] 95, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [-2-->] 0  row: 0x1079aaca0  session: 0x1078dffd0 - 2022-03-17 19:24:05,045 - logic_logger - INFO
Logic Phase:		COMMIT(session=0x1078dffd0)   										 - 2022-03-17 19:24:05,046 - logic_logger - INFO
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [2013-10-13-->] None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10778a460  session: 0x1078dffd0 - 2022-03-17 19:24:05,047 - logic_logger - INFO

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
  
 - 2022-03-17 19:24:05,084 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x107a5a610)   (sqlalchemy flush processing)       	 - 2022-03-17 19:24:05,084 - logic_logger - INFO  
Logic Phase:		ROW LOGIC(session=0x107a5aaf0) (sqlalchemy before_flush)			 - 2022-03-17 19:24:05,133 - logic_logger - INFO  
..Employee[5] {Update - client} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [200000.0000000000-->] 95000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x107aa9f40  session: 0x107a5aaf0 - 2022-03-17 19:24:05,133 - logic_logger - INFO  
..Employee[5] {BEGIN Copy to: EmployeeAudit} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [200000.0000000000-->] 95000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x107aa9f40  session: 0x107a5aaf0 - 2022-03-17 19:24:05,135 - logic_logger - INFO  
....EmployeeAudit[None] {Insert - Copy EmployeeAudit} Id: None, Title: Sales Manager, Salary: 95000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: None  row: 0x107ac10d0  session: 0x107a5aaf0 - 2022-03-17 19:24:05,136 - logic_logger - INFO  
....EmployeeAudit[None] {early_row_event_all_classes - handle_all sets 'Created_on} Id: None, Title: Sales Manager, Salary: 95000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: 2022-03-17 19:24:05.136175  row: 0x107ac10d0  session: 0x107a5aaf0 - 2022-03-17 19:24:05,136 - logic_logger - INFO  
Logic Phase:		COMMIT(session=0x107a5aaf0)   										 - 2022-03-17 19:24:05,136 - logic_logger - INFO  
..Employee[5] {Commit Event} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [200000.0000000000-->] 95000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x107aa9f40  session: 0x107a5aaf0 - 2022-03-17 19:24:05,137 - logic_logger - INFO  
  
Rules Fired:  
  Employee  
    1. RowEvent Employee.audit_by_event()   
  
 - 2022-03-17 19:24:05,137 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x107a5aaf0)   (sqlalchemy flush processing)       	 - 2022-03-17 19:24:05,137 - logic_logger - INFO  
```
**Logic Log** in Scenario: Audit Salary Change
```
Logic Phase:		ROW LOGIC(session=0x107a5a610) (sqlalchemy before_flush)			 - 2022-03-17 19:24:05,080 - logic_logger - INFO
..Employee[5] {Update - client} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [95000.0000000000-->] 200000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x107a5a520  session: 0x107a5a610 - 2022-03-17 19:24:05,080 - logic_logger - INFO
..Employee[5] {BEGIN Copy to: EmployeeAudit} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [95000.0000000000-->] 200000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x107a5a520  session: 0x107a5a610 - 2022-03-17 19:24:05,082 - logic_logger - INFO
....EmployeeAudit[None] {Insert - Copy EmployeeAudit} Id: None, Title: Sales Manager, Salary: 200000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: None  row: 0x107a5a1f0  session: 0x107a5a610 - 2022-03-17 19:24:05,083 - logic_logger - INFO
....EmployeeAudit[None] {early_row_event_all_classes - handle_all sets 'Created_on} Id: None, Title: Sales Manager, Salary: 200000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: 2022-03-17 19:24:05.083395  row: 0x107a5a1f0  session: 0x107a5a610 - 2022-03-17 19:24:05,083 - logic_logger - INFO
Logic Phase:		COMMIT(session=0x107a5a610)   										 - 2022-03-17 19:24:05,083 - logic_logger - INFO
..Employee[5] {Commit Event} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [95000.0000000000-->] 200000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x107a5a520  session: 0x107a5a610 - 2022-03-17 19:24:05,084 - logic_logger - INFO

```
</details>
  
4 features passed, 0 failed, 0 skipped  
10 scenarios passed, 0 failed, 0 skipped  
34 steps passed, 0 failed, 0 skipped, 0 undefined  
Took 0m0.502s  