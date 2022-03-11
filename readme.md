# TDD - Test Driven Dev, with Logic Traceability

This project is to explore:

1. Using [TDD](http://dannorth.net/introducing-bdd/) to define Stories and their Behaviors (tests), using [behave](https://behave.readthedocs.io/en/stable/tutorial.html).
2. Behavior / Logic Tracing - identifying logic that implements a behavior

# Stories and Behaviors

From the TDD article

## Story
```
As a [X]
I want [Y-feature]
so that [Z-benefit]
```

### Place Order
```
As a Sales Manager,
I want Place Order services
So that I can check credit and reorder products
```


## Behavior (aka Scenario)
```
Given some initial context (the GIVEN),   ==> Class
   And other conditions,
When an EVENT occurs,                     ==> Class
Then ensure some OUTCOME,                 ==> Class
   And other outcomes.
```

### Place Order > Check Credit
```
Given a CustomerAccount with an assigned credit limit,
When an OrderIsPlaced
Then ensure OrderAccepted if credit limit is not exceeded
And ensure OrderRejected if the credit limit is exceeded
```
### Place Order > Reorder Products
```
Given Products with assigned reorder points
When an OrderIsShipped
Then ensure ProductsAreReordered iff the reorder points execeeds recomputed Units-Available
```

# behave stubs

```
Feature: Application Integration 

  Scenario: GET Customer          # features/api.feature:3
    Given Customer Account: ALFKI # features/steps/api.py:3 0.000s
    When GET Customer API         # features/steps/api.py:7 0.000s
    Then ALFKI retrieved          # features/steps/api.py:11 0.000s

  Scenario: GET Department                      # features/api.feature:9
    Given Department TBD                        # features/steps/api.py:16 0.000s
    When GET Department with SubDepartments API # features/steps/api.py:20 0.000s
    Then SubDepartments returned                # features/steps/api.py:24 0.000s

Feature: Place Order # features/place_order.feature:1

  Scenario: Custom Service: add_order - good  # features/place_order.feature:3
    Given Customer Account: ALFKI             # features/steps/api.py:3 0.000s
    When Good Order Placed                    # features/steps/place_order.py:3 0.000s
    Then Balance Adjusted                     # features/steps/place_order.py:7 0.000s

  Scenario: Custom Service: add_order - bad   # features/place_order.feature:9
    Given Customer Account: ALFKI             # features/steps/api.py:3 0.000s
    When Order Placed with excessive quantity # features/steps/place_order.py:12 0.000s
    Then Rejected per Credit Limit            # features/steps/place_order.py:16 0.000s

2 features passed, 0 failed, 0 skipped
4 scenarios passed, 0 failed, 0 skipped
12 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.001s
```

&nbsp;&nbsp;

# Debug behave

Basic (no IDE) procedure [noted here](https://921kiyo.com/debugging-the-Python-behave-test/).

Attempting VSCode using [this procedure](https://qxf2.com/blog/run-python-behave-from-visual-studio-code/); failing to debug:

<figure><img src="https://github.com/valhuber/TDD/blob/main/images/debug-fails.png?raw=true"></figure>
