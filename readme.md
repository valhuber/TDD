# TDD - Test Driven Dev, with Logic Traceability

This project is to explore
1. Using [TDD](http://dannorth.net/introducing-bdd/) to define Stories and their Behaviors (tests)
2. Behavior / Logic Tracing - identifying logic that implements a behavior

# Stories and Behaviors

From the TDD article

## Story
```
As a [X]
I want [Y]
so that [Z]
```

### Place Order
```
As a Sales Manager,
I want Place Orders services
So that I can check credit and reorder products
```


## Behavior
```
Given some initial context (the givens),  
When an event occurs,  
Then ensure some outcomes.
```

### Place Order > Check Credit
```
Given a customer account with an assigned credit limit,
When an Order is Placed
Then Accept the Order if credit limit is not exceeded
And Reject the Order if the credit limit is exceeded
```
### Place Order > Reorder Products
```
Given products with assigned reorder points
When an Order is Shipped
Then Reorder Products where the reorder points execeeds Units-Available
```
