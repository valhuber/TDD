Feature: Place Order

  Scenario: Custom Service: add_order - good
     Given Customer Account: ALFKI
      When Good Order Placed
      Then Balance Adjusted


  Scenario: Custom Service: add_order - bad
     Given Customer Account: ALFKI
      When Order Placed with excessive quantity
      Then Rejected per Credit Limit