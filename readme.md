# TDD - Test Driven Dev, with Logic Traceability

This project is to explore
1. Using [TDD](http://dannorth.net/introducing-bdd/) to define Stories and their Behaviors (tests)
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
Given some initial context (the GIVEN),  ==> Class
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
Given products with assigned reorder points
When an Order is Shipped
Then Reorder Products where the reorder points execeeds Units-Available
```
