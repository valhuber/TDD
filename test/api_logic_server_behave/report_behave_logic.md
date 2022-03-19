# TDD - Test Driven Dev, with Logic Traceability

This project uses the sample app of [API Logic Server](https://github.com/valhuber/ApiLogicServer/blob/main/README.md) to illustrate:
  
1. Rapid project creation and customization, using API Logic Server

1. Using [TDD](http://dannorth.net/introducing-bdd/) to define Stories and their Behaviors (tests), using [behave](https://behave.readthedocs.io/en/stable/tutorial.html).  A quick reference is [shown here](https://github.com/valhuber/TDD/wiki/Stories-And-Behaviors).
  


&nbsp;
&nbsp;


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
AbstractRule Bank[0x10aa83790] (loaded 2022-03-19 10:42:47.840731)		##   - 2022-03-19 10:43:25,932 - logic_logger - INFO
Mapped Class[OrderDetail] rules:		##   - 2022-03-19 10:43:25,932 - logic_logger - INFO
  Derive OrderDetail.UnitPrice as Copy(Product.UnitPrice)		##   - 2022-03-19 10:43:25,933 - logic_logger - INFO
  Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]		##   - 2022-03-19 10:43:25,933 - logic_logger - INFO
  Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate		##   - 2022-03-19 10:43:25,933 - logic_logger - INFO
Mapped Class[Order] rules:		##   - 2022-03-19 10:43:25,933 - logic_logger - INFO
  Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)		##   - 2022-03-19 10:43:25,934 - logic_logger - INFO
  RowEvent Order.congratulate_sales_rep() 		##   - 2022-03-19 10:43:25,934 - logic_logger - INFO
  Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)		##   - 2022-03-19 10:43:25,934 - logic_logger - INFO
Mapped Class[Customer] rules:		##   - 2022-03-19 10:43:25,934 - logic_logger - INFO
  Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10ac2fca0>)		##   - 2022-03-19 10:43:25,935 - logic_logger - INFO
  Constraint Function: None 		##   - 2022-03-19 10:43:25,935 - logic_logger - INFO
  Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x10ac4c670>)		##   - 2022-03-19 10:43:25,935 - logic_logger - INFO
  Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)		##   - 2022-03-19 10:43:25,935 - logic_logger - INFO
Mapped Class[Product] rules:		##   - 2022-03-19 10:43:25,936 - logic_logger - INFO
  Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x10ac4c550>)		##   - 2022-03-19 10:43:25,936 - logic_logger - INFO
  Derive Product.UnitsInStock as Formula (1): <function>		##   - 2022-03-19 10:43:25,936 - logic_logger - INFO
Mapped Class[Employee] rules:		##   - 2022-03-19 10:43:25,937 - logic_logger - INFO
  Constraint Function: <function declare_logic.<locals>.raise_over_20_percent at 0x10ac4cdc0> 		##   - 2022-03-19 10:43:25,937 - logic_logger - INFO
  RowEvent Employee.audit_by_event() 		##   - 2022-03-19 10:43:25,937 - logic_logger - INFO
  Copy to: EmployeeAudit		##   - 2022-03-19 10:43:25,937 - logic_logger - INFO
Logic Bank - 21 rules loaded - 2022-03-19 10:43:25,938 - logic_logger - INFO
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
    1. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x10ac4c670>)  
    2. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10ac2fca0>)  
    3. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    4. RowEvent Order.congratulate_sales_rep()   
    5. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    6. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
  Product  
    7. Derive Product.UnitsInStock as Formula (1): <function>  
    8. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x10ac4c550>)  
  
 - 2022-03-19 10:43:29,631 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x10b27cf10)   (sqlalchemy flush processing)       	 - 2022-03-19 10:43:29,631 - logic_logger - INFO  
```
**Logic Log** in Scenario: Good Order Custom Service
```
Logic Phase:		ROW LOGIC(session=0x10b27cf10) (sqlalchemy before_flush)			 - 2022-03-19 10:43:29,609 - logic_logger - INFO
..Order[11111] {Delete - client} Id: 11111, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11.0000000000, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal: 56.00, Country: None, City: None, Ready: True, OrderDetailCount: 2  row: 0x10b41a1f0  session: 0x10b27cf10 - 2022-03-19 10:43:29,610 - logic_logger - INFO
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount, OrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2158.0000000000-->] 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount:  [16-->] 15, UnpaidOrderCount:  [11-->] 10  row: 0x10b44c7f0  session: 0x10b27cf10 - 2022-03-19 10:43:29,612 - logic_logger - INFO
..OrderDetail[2223] {Delete - client} Id: 2223, OrderId: 11111, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1, Discount: 0.0, Amount: 18.0000000000, ShippedDate: None  row: 0x10b44ceb0  session: 0x10b27cf10 - 2022-03-19 10:43:29,614 - logic_logger - INFO
....Product[1] {Update - Adjusting Product: UnitsShipped} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock: 39, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [0-->] -1  row: 0x10b3c6400  session: 0x10b27cf10 - 2022-03-19 10:43:29,616 - logic_logger - INFO
....Product[1] {Formula UnitsInStock} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock:  [39-->] 40, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [0-->] -1  row: 0x10b3c6400  session: 0x10b27cf10 - 2022-03-19 10:43:29,617 - logic_logger - INFO
..OrderDetail[2223] {No adjustment on deleted parent: Order} Id: 2223, OrderId: 11111, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1, Discount: 0.0, Amount: 18.0000000000, ShippedDate: None  row: 0x10b44ceb0  session: 0x10b27cf10 - 2022-03-19 10:43:29,619 - logic_logger - INFO
..OrderDetail[2224] {Delete - client} Id: 2224, OrderId: 11111, ProductId: 2, UnitPrice: 19.0000000000, Quantity: 2, Discount: 0.0, Amount: 38.0000000000, ShippedDate: None  row: 0x10b44cdc0  session: 0x10b27cf10 - 2022-03-19 10:43:29,620 - logic_logger - INFO
....Product[2] {Update - Adjusting Product: UnitsShipped} Id: 2, ProductName: Chang, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 24 - 12 oz bottles, UnitPrice: 19.0000000000, UnitsInStock: 15, UnitsOnOrder: 40, ReorderLevel: 25, Discontinued: 0, UnitsShipped:  [2-->] 0  row: 0x10b3c67c0  session: 0x10b27cf10 - 2022-03-19 10:43:29,622 - logic_logger - INFO
....Product[2] {Formula UnitsInStock} Id: 2, ProductName: Chang, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 24 - 12 oz bottles, UnitPrice: 19.0000000000, UnitsInStock:  [15-->] 17, UnitsOnOrder: 40, ReorderLevel: 25, Discontinued: 0, UnitsShipped:  [2-->] 0  row: 0x10b3c67c0  session: 0x10b27cf10 - 2022-03-19 10:43:29,624 - logic_logger - INFO
..OrderDetail[2224] {No adjustment on deleted parent: Order} Id: 2224, OrderId: 11111, ProductId: 2, UnitPrice: 19.0000000000, Quantity: 2, Discount: 0.0, Amount: 38.0000000000, ShippedDate: None  row: 0x10b44cdc0  session: 0x10b27cf10 - 2022-03-19 10:43:29,626 - logic_logger - INFO
Logic Phase:		COMMIT(session=0x10b27cf10)   										 - 2022-03-19 10:43:29,626 - logic_logger - INFO
..Order[11111] {Commit Event} Id: 11111, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11.0000000000, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal: 56.00, Country: None, City: None, Ready: True, OrderDetailCount: 2  row: 0x10b41a1f0  session: 0x10b27cf10 - 2022-03-19 10:43:29,627 - logic_logger - INFO

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
    1. Constraint Function: None   
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x10ac4c670>)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10ac2fca0>)  
    4. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    5. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    6. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
  OrderDetail  
    7. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
    8. Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]  
    9. Derive OrderDetail.UnitPrice as Copy(Product.UnitPrice)  
  Product  
    10. Derive Product.UnitsInStock as Formula (1): <function>  
    11. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x10ac4c550>)  
  
 - 2022-03-19 10:43:29,806 - logic_logger - INFO  
```
**Logic Log** in Scenario: Bad Order Custom Service
```
Logic Phase:		ROW LOGIC(session=0x10b2dd820) (sqlalchemy before_flush)			 - 2022-03-19 10:43:29,780 - logic_logger - INFO
..Order[None] {Insert - client} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 10, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal: None, Country: None, City: None, Ready: None, OrderDetailCount: None  row: 0x10b3c6fd0  session: 0x10b2dd820 - 2022-03-19 10:43:29,781 - logic_logger - INFO
....Customer[ALFKI] {Update - Adjusting Customer: UnpaidOrderCount, OrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance: 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount:  [15-->] 16, UnpaidOrderCount:  [10-->] 11  row: 0x10b405340  session: 0x10b2dd820 - 2022-03-19 10:43:29,786 - logic_logger - INFO
..OrderDetail[None] {Insert - client} Id: None, OrderId: None, ProductId: 1, UnitPrice: None, Quantity: 1111, Discount: 0, Amount: None, ShippedDate: None  row: 0x10b3bfeb0  session: 0x10b2dd820 - 2022-03-19 10:43:29,788 - logic_logger - INFO
..OrderDetail[None] {copy_rules for role: Product - UnitPrice} Id: None, OrderId: None, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1111, Discount: 0, Amount: None, ShippedDate: None  row: 0x10b3bfeb0  session: 0x10b2dd820 - 2022-03-19 10:43:29,792 - logic_logger - INFO
..OrderDetail[None] {Formula Amount} Id: None, OrderId: None, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1111, Discount: 0, Amount: 19998.0000000000, ShippedDate: None  row: 0x10b3bfeb0  session: 0x10b2dd820 - 2022-03-19 10:43:29,792 - logic_logger - INFO
....Product[1] {Update - Adjusting Product: UnitsShipped} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock: 40, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [-1-->] 1110  row: 0x10b410be0  session: 0x10b2dd820 - 2022-03-19 10:43:29,794 - logic_logger - INFO
....Product[1] {Formula UnitsInStock} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock:  [40-->] -1071, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [-1-->] 1110  row: 0x10b410be0  session: 0x10b2dd820 - 2022-03-19 10:43:29,795 - logic_logger - INFO
....Order[None] {Update - Adjusting Order: AmountTotal, OrderDetailCount} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 10, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipPostalCode: None, ShipCountry: None, AmountTotal:  [None-->] 19998.0000000000, Country: None, City: None, Ready: None, OrderDetailCount:  [None-->] 1  row: 0x10b3c6fd0  session: 0x10b2dd820 - 2022-03-19 10:43:29,797 - logic_logger - INFO
......Customer[ALFKI] {Update - Adjusting Customer: Balance} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 22100.0000000000, CreditLimit: 2300.0000000000, OrderCount: 16, UnpaidOrderCount: 11  row: 0x10b405340  session: 0x10b2dd820 - 2022-03-19 10:43:29,799 - logic_logger - INFO
......Customer[ALFKI] {Constraint Failure: balance (22100.0000000000) exceeds credit (2300.0000000000)} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 22100.0000000000, CreditLimit: 2300.0000000000, OrderCount: 16, UnpaidOrderCount: 11  row: 0x10b405340  session: 0x10b2dd820 - 2022-03-19 10:43:29,801 - logic_logger - INFO

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
    1. Constraint Function: None   
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x10ac4c670>)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10ac2fca0>)  
    4. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    5. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    6. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
  OrderDetail  
    7. Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]  
  Product  
    8. Derive Product.UnitsInStock as Formula (1): <function>  
    9. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x10ac4c550>)  
  
 - 2022-03-19 10:43:29,920 - logic_logger - INFO  
```
**Logic Log** in Scenario: Alter Item Qty to exceed credit
```
Logic Phase:		ROW LOGIC(session=0x10b41a9d0) (sqlalchemy before_flush)			 - 2022-03-19 10:43:29,902 - logic_logger - INFO
..OrderDetail[1040] {Update - client} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount: 684.0000000000, ShippedDate: None  row: 0x10b3201c0  session: 0x10b41a9d0 - 2022-03-19 10:43:29,903 - logic_logger - INFO
..OrderDetail[1040] {Formula Amount} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount:  [684.0000000000-->] 50616.0000000000, ShippedDate: None  row: 0x10b3201c0  session: 0x10b41a9d0 - 2022-03-19 10:43:29,904 - logic_logger - INFO
..OrderDetail[1040] {Prune Formula: ShippedDate [['Order.ShippedDate']]} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount:  [684.0000000000-->] 50616.0000000000, ShippedDate: None  row: 0x10b3201c0  session: 0x10b41a9d0 - 2022-03-19 10:43:29,905 - logic_logger - INFO
....Product[28] {Update - Adjusting Product: UnitsShipped} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock: 26, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] 1095  row: 0x10b425070  session: 0x10b41a9d0 - 2022-03-19 10:43:29,907 - logic_logger - INFO
....Product[28] {Formula UnitsInStock} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock:  [26-->] -1069, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] 1095  row: 0x10b425070  session: 0x10b41a9d0 - 2022-03-19 10:43:29,908 - logic_logger - INFO
....Order[10643] {Update - Adjusting Order: AmountTotal} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal:  [1086.00-->] 51018.0000000000, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10b4250d0  session: 0x10b41a9d0 - 2022-03-19 10:43:29,911 - logic_logger - INFO
......Customer[ALFKI] {Update - Adjusting Customer: Balance} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 52034.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount: 10  row: 0x10b425310  session: 0x10b41a9d0 - 2022-03-19 10:43:29,914 - logic_logger - INFO
......Customer[ALFKI] {Constraint Failure: balance (52034.0000000000) exceeds credit (2300.0000000000)} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 52034.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount: 10  row: 0x10b425310  session: 0x10b41a9d0 - 2022-03-19 10:43:29,915 - logic_logger - INFO

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
    1. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10ac2fca0>)  
    2. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
    3. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x10ac4c670>)  
  Order  
    4. RowEvent Order.congratulate_sales_rep()   
  
 - 2022-03-19 10:43:30,019 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x10b41a220)   (sqlalchemy flush processing)       	 - 2022-03-19 10:43:30,019 - logic_logger - INFO  
```
**Logic Log** in Scenario: Alter Required Date - adjust logic pruned
```
Logic Phase:		ROW LOGIC(session=0x10b41a220) (sqlalchemy before_flush)			 - 2022-03-19 10:43:30,012 - logic_logger - INFO
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate:  [2013-10-13-->] 2013-10-13 00:00:00, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10b3c63a0  session: 0x10b41a220 - 2022-03-19 10:43:30,013 - logic_logger - INFO
Logic Phase:		COMMIT(session=0x10b41a220)   										 - 2022-03-19 10:43:30,015 - logic_logger - INFO
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate:  [2013-10-13-->] 2013-10-13 00:00:00, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10b3c63a0  session: 0x10b41a220 - 2022-03-19 10:43:30,016 - logic_logger - INFO

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
    1. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x10ac4c670>)  
    2. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10ac2fca0>)  
    3. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    4. RowEvent Order.congratulate_sales_rep()   
    5. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    6. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
  OrderDetail  
    7. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
  Product  
    8. Derive Product.UnitsInStock as Formula (1): <function>  
    9. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x10ac4c550>)  
  
 - 2022-03-19 10:43:30,241 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x10b4101c0)   (sqlalchemy flush processing)       	 - 2022-03-19 10:43:30,241 - logic_logger - INFO  
```
**Logic Log** in Scenario: Set Shipped - adjust logic reuse
```
Logic Phase:		ROW LOGIC(session=0x10b4101c0) (sqlalchemy before_flush)			 - 2022-03-19 10:43:30,207 - logic_logger - INFO
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [None-->] 2013-10-13, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10b425af0  session: 0x10b4101c0 - 2022-03-19 10:43:30,208 - logic_logger - INFO
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 1016.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount:  [10-->] 9  row: 0x10b425eb0  session: 0x10b4101c0 - 2022-03-19 10:43:30,211 - logic_logger - INFO
....OrderDetail[1040] {Update - Cascading Order.ShippedDate (,...)} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: None  row: 0x10b42a310  session: 0x10b4101c0 - 2022-03-19 10:43:30,215 - logic_logger - INFO
....OrderDetail[1040] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: None  row: 0x10b42a310  session: 0x10b4101c0 - 2022-03-19 10:43:30,216 - logic_logger - INFO
....OrderDetail[1040] {Formula ShippedDate} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate:  [None-->] 2013-10-13  row: 0x10b42a310  session: 0x10b4101c0 - 2022-03-19 10:43:30,216 - logic_logger - INFO
......Product[28] {Update - Adjusting Product: UnitsShipped} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock: 26, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] -15  row: 0x10b4251f0  session: 0x10b4101c0 - 2022-03-19 10:43:30,219 - logic_logger - INFO
......Product[28] {Formula UnitsInStock} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock:  [26-->] 41, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [0-->] -15  row: 0x10b4251f0  session: 0x10b4101c0 - 2022-03-19 10:43:30,220 - logic_logger - INFO
....OrderDetail[1041] {Update - Cascading Order.ShippedDate (,...)} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: None  row: 0x10b42a370  session: 0x10b4101c0 - 2022-03-19 10:43:30,221 - logic_logger - INFO
....OrderDetail[1041] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: None  row: 0x10b42a370  session: 0x10b4101c0 - 2022-03-19 10:43:30,222 - logic_logger - INFO
....OrderDetail[1041] {Formula ShippedDate} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate:  [None-->] 2013-10-13  row: 0x10b42a370  session: 0x10b4101c0 - 2022-03-19 10:43:30,223 - logic_logger - INFO
......Product[39] {Update - Adjusting Product: UnitsShipped} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock: 69, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [0-->] -21  row: 0x10b440880  session: 0x10b4101c0 - 2022-03-19 10:43:30,225 - logic_logger - INFO
......Product[39] {Formula UnitsInStock} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock:  [69-->] 90, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [0-->] -21  row: 0x10b440880  session: 0x10b4101c0 - 2022-03-19 10:43:30,226 - logic_logger - INFO
....OrderDetail[1042] {Update - Cascading Order.ShippedDate (,...)} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: None  row: 0x10b42a2b0  session: 0x10b4101c0 - 2022-03-19 10:43:30,228 - logic_logger - INFO
....OrderDetail[1042] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: None  row: 0x10b42a2b0  session: 0x10b4101c0 - 2022-03-19 10:43:30,229 - logic_logger - INFO
....OrderDetail[1042] {Formula ShippedDate} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate:  [None-->] 2013-10-13  row: 0x10b42a2b0  session: 0x10b4101c0 - 2022-03-19 10:43:30,230 - logic_logger - INFO
......Product[46] {Update - Adjusting Product: UnitsShipped} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock: 95, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [0-->] -2  row: 0x10b4404f0  session: 0x10b4101c0 - 2022-03-19 10:43:30,232 - logic_logger - INFO
......Product[46] {Formula UnitsInStock} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock:  [95-->] 97, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [0-->] -2  row: 0x10b4404f0  session: 0x10b4101c0 - 2022-03-19 10:43:30,233 - logic_logger - INFO
Logic Phase:		COMMIT(session=0x10b4101c0)   										 - 2022-03-19 10:43:30,234 - logic_logger - INFO
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [None-->] 2013-10-13, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10b425af0  session: 0x10b4101c0 - 2022-03-19 10:43:30,235 - logic_logger - INFO

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
    1. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x10ac4c670>)  
    2. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10ac2fca0>)  
    3. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    4. RowEvent Order.congratulate_sales_rep()   
    5. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    6. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
  OrderDetail  
    7. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
  Product  
    8. Derive Product.UnitsInStock as Formula (1): <function>  
    9. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x10ac4c550>)  
  
 - 2022-03-19 10:43:30,463 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x10b410700)   (sqlalchemy flush processing)       	 - 2022-03-19 10:43:30,464 - logic_logger - INFO  
```
**Logic Log** in Scenario: Reset Shipped - adjust logic reuse
```
Logic Phase:		ROW LOGIC(session=0x10b410700) (sqlalchemy before_flush)			 - 2022-03-19 10:43:30,430 - logic_logger - INFO
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [2013-10-13-->] None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10b320250  session: 0x10b410700 - 2022-03-19 10:43:30,431 - logic_logger - INFO
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [1016.0000000000-->] 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount:  [9-->] 10  row: 0x10b42a190  session: 0x10b410700 - 2022-03-19 10:43:30,434 - logic_logger - INFO
....OrderDetail[1040] {Update - Cascading Order.ShippedDate (,...)} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: 2013-10-13  row: 0x10b42aa30  session: 0x10b410700 - 2022-03-19 10:43:30,438 - logic_logger - INFO
....OrderDetail[1040] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate: 2013-10-13  row: 0x10b42aa30  session: 0x10b410700 - 2022-03-19 10:43:30,439 - logic_logger - INFO
....OrderDetail[1040] {Formula ShippedDate} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity: 15, Discount: 0.25, Amount: 684.0000000000, ShippedDate:  [2013-10-13-->] None  row: 0x10b42aa30  session: 0x10b410700 - 2022-03-19 10:43:30,439 - logic_logger - INFO
......Product[28] {Update - Adjusting Product: UnitsShipped} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock: 41, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [-15-->] 0  row: 0x10b42a580  session: 0x10b410700 - 2022-03-19 10:43:30,442 - logic_logger - INFO
......Product[28] {Formula UnitsInStock} Id: 28, ProductName: Rössle Sauerkraut, SupplierId: 12, CategoryId: 7, QuantityPerUnit: 25 - 825 g cans, UnitPrice: 45.6000000000, UnitsInStock:  [41-->] 26, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 1, UnitsShipped:  [-15-->] 0  row: 0x10b42a580  session: 0x10b410700 - 2022-03-19 10:43:30,443 - logic_logger - INFO
....OrderDetail[1041] {Update - Cascading Order.ShippedDate (,...)} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: 2013-10-13  row: 0x10b42aa90  session: 0x10b410700 - 2022-03-19 10:43:30,445 - logic_logger - INFO
....OrderDetail[1041] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate: 2013-10-13  row: 0x10b42aa90  session: 0x10b410700 - 2022-03-19 10:43:30,445 - logic_logger - INFO
....OrderDetail[1041] {Formula ShippedDate} Id: 1041, OrderId: 10643, ProductId: 39, UnitPrice: 18.0000000000, Quantity: 21, Discount: 0.25, Amount: 378.0000000000, ShippedDate:  [2013-10-13-->] None  row: 0x10b42aa90  session: 0x10b410700 - 2022-03-19 10:43:30,446 - logic_logger - INFO
......Product[39] {Update - Adjusting Product: UnitsShipped} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock: 90, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [-21-->] 0  row: 0x10b42a790  session: 0x10b410700 - 2022-03-19 10:43:30,448 - logic_logger - INFO
......Product[39] {Formula UnitsInStock} Id: 39, ProductName: Chartreuse verte, SupplierId: 18, CategoryId: 1, QuantityPerUnit: 750 cc per bottle, UnitPrice: 18.0000000000, UnitsInStock:  [90-->] 69, UnitsOnOrder: 0, ReorderLevel: 5, Discontinued: 0, UnitsShipped:  [-21-->] 0  row: 0x10b42a790  session: 0x10b410700 - 2022-03-19 10:43:30,449 - logic_logger - INFO
....OrderDetail[1042] {Update - Cascading Order.ShippedDate (,...)} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: 2013-10-13  row: 0x10b42a9d0  session: 0x10b410700 - 2022-03-19 10:43:30,451 - logic_logger - INFO
....OrderDetail[1042] {Prune Formula: Amount [['UnitPrice', 'Quantity']]} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate: 2013-10-13  row: 0x10b42a9d0  session: 0x10b410700 - 2022-03-19 10:43:30,452 - logic_logger - INFO
....OrderDetail[1042] {Formula ShippedDate} Id: 1042, OrderId: 10643, ProductId: 46, UnitPrice: 12.0000000000, Quantity: 2, Discount: 0.25, Amount: 24.0000000000, ShippedDate:  [2013-10-13-->] None  row: 0x10b42a9d0  session: 0x10b410700 - 2022-03-19 10:43:30,452 - logic_logger - INFO
......Product[46] {Update - Adjusting Product: UnitsShipped} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock: 97, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [-2-->] 0  row: 0x10b42afa0  session: 0x10b410700 - 2022-03-19 10:43:30,454 - logic_logger - INFO
......Product[46] {Formula UnitsInStock} Id: 46, ProductName: Spegesild, SupplierId: 21, CategoryId: 8, QuantityPerUnit: 4 - 450 g glasses, UnitPrice: 12.0000000000, UnitsInStock:  [97-->] 95, UnitsOnOrder: 0, ReorderLevel: 0, Discontinued: 0, UnitsShipped:  [-2-->] 0  row: 0x10b42afa0  session: 0x10b410700 - 2022-03-19 10:43:30,456 - logic_logger - INFO
Logic Phase:		COMMIT(session=0x10b410700)   										 - 2022-03-19 10:43:30,457 - logic_logger - INFO
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [2013-10-13-->] None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipPostalCode: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3  row: 0x10b320250  session: 0x10b410700 - 2022-03-19 10:43:30,459 - logic_logger - INFO

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
  
 - 2022-03-19 10:43:30,575 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x10b3c6310)   (sqlalchemy flush processing)       	 - 2022-03-19 10:43:30,576 - logic_logger - INFO  
Logic Phase:		ROW LOGIC(session=0x10b45d6a0) (sqlalchemy before_flush)			 - 2022-03-19 10:43:30,767 - logic_logger - INFO  
..Employee[5] {Update - client} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [200000.0000000000-->] 95000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x10b45db20  session: 0x10b45d6a0 - 2022-03-19 10:43:30,769 - logic_logger - INFO  
..Employee[5] {BEGIN Copy to: EmployeeAudit} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [200000.0000000000-->] 95000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x10b45db20  session: 0x10b45d6a0 - 2022-03-19 10:43:30,775 - logic_logger - INFO  
....EmployeeAudit[None] {Insert - Copy EmployeeAudit} Id: None, Title: Sales Manager, Salary: 95000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: None  row: 0x10b45da60  session: 0x10b45d6a0 - 2022-03-19 10:43:30,777 - logic_logger - INFO  
....EmployeeAudit[None] {early_row_event_all_classes - handle_all sets 'Created_on} Id: None, Title: Sales Manager, Salary: 95000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: 2022-03-19 10:43:30.777892  row: 0x10b45da60  session: 0x10b45d6a0 - 2022-03-19 10:43:30,778 - logic_logger - INFO  
Logic Phase:		COMMIT(session=0x10b45d6a0)   										 - 2022-03-19 10:43:30,779 - logic_logger - INFO  
..Employee[5] {Commit Event} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [200000.0000000000-->] 95000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x10b45db20  session: 0x10b45d6a0 - 2022-03-19 10:43:30,781 - logic_logger - INFO  
  
Rules Fired:  
  Employee  
    1. RowEvent Employee.audit_by_event()   
  
 - 2022-03-19 10:43:30,783 - logic_logger - INFO  
Logic Phase:		FLUSH(session=0x10b45d6a0)   (sqlalchemy flush processing)       	 - 2022-03-19 10:43:30,783 - logic_logger - INFO  
```
**Logic Log** in Scenario: Audit Salary Change
```
Logic Phase:		ROW LOGIC(session=0x10b3c6310) (sqlalchemy before_flush)			 - 2022-03-19 10:43:30,565 - logic_logger - INFO
..Employee[5] {Update - client} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [95000.0000000000-->] 200000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x10b405b80  session: 0x10b3c6310 - 2022-03-19 10:43:30,566 - logic_logger - INFO
..Employee[5] {BEGIN Copy to: EmployeeAudit} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [95000.0000000000-->] 200000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x10b405b80  session: 0x10b3c6310 - 2022-03-19 10:43:30,570 - logic_logger - INFO
....EmployeeAudit[None] {Insert - Copy EmployeeAudit} Id: None, Title: Sales Manager, Salary: 200000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: None  row: 0x10b405d30  session: 0x10b3c6310 - 2022-03-19 10:43:30,572 - logic_logger - INFO
....EmployeeAudit[None] {early_row_event_all_classes - handle_all sets 'Created_on} Id: None, Title: Sales Manager, Salary: 200000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: 2022-03-19 10:43:30.572509  row: 0x10b405d30  session: 0x10b3c6310 - 2022-03-19 10:43:30,572 - logic_logger - INFO
Logic Phase:		COMMIT(session=0x10b3c6310)   										 - 2022-03-19 10:43:30,573 - logic_logger - INFO
..Employee[5] {Commit Event} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Photo: None, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: http://accweb/emmployees/buchanan.bmp, IsCommissioned: 0, Salary:  [95000.0000000000-->] 200000, WorksForDepartmentId: 3, OnLoanDepartmentId: None  row: 0x10b405b80  session: 0x10b3c6310 - 2022-03-19 10:43:30,574 - logic_logger - INFO

```
</details>
  
4 features passed, 0 failed, 0 skipped  
10 scenarios passed, 0 failed, 0 skipped  
34 steps passed, 0 failed, 0 skipped, 0 undefined  
Took 0m0.502s  