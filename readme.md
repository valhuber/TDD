# TDD - Test Driven Dev, with Logic Traceability

This project uses the sample app of [API Logic Server](https://github.com/valhuber/ApiLogicServer/blob/main/README.md) to explore:

1. Using [TDD](http://dannorth.net/introducing-bdd/) to define Stories and their Behaviors (tests), using [behave](https://behave.readthedocs.io/en/stable/tutorial.html).
2. Behavior / Logic Tracing - identifying logic that implements a behavior

&nbsp;&nbsp;

# Setup

The usual:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

This should enable you to run launch configuration `ApiLogicServer`.
1. Start the launch configuration `ApiLogicServer`
2. Open a terminal window, and

```
cd test/behave
behave
```

&nbsp;&nbsp;

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

&nbsp;&nbsp;

# Example 1

This diagram illustrates:
1. A running TDD test
2. Generating `behave/results` log files with rules trace and rule use

<figure><img src="https://github.com/valhuber/TDD/blob/main/images/example-1.png?raw=true"></figure>

&nbsp;&nbsp;

# Appendix - Debug behave

Basic (no IDE) procedure [noted here](https://921kiyo.com/debugging-the-Python-behave-test/).

Attempting VSCode using [this procedure](https://qxf2.com/blog/run-python-behave-from-visual-studio-code/); failing to debug:

<figure><img src="https://github.com/valhuber/TDD/blob/main/images/debug-fails.png?raw=true"></figure>

Also tried [this procedure](https://github.com/behave/behave/issues/709), unable to import:

<figure><img src="https://github.com/valhuber/TDD/blob/main/images/debug-my-behave.png?raw=true"></figure>