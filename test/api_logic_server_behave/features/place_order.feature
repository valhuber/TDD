Feature: Place Order

  Scenario: Custom Service: add_order - good
     Given Customer Account: ALFKI
      When Good Order Placed
      Then Balance Adjusted (demo: chain up)
      Then Products Reordered
      Then Proper delete


  Scenario: Custom Service: add_order - bad
     Given Customer Account: ALFKI
      When Order Placed with excessive quantity
      Then Rejected per Credit Limit
      Then exceeds credit in response


  Scenario: Alter Item Qty to exceed credit
     Given Customer Account: ALFKI
      When Order Detail Quantity altered very high
      Then Rejected per Credit Limit
      Then exceeds credit in response


  Scenario: Alter Required Date - adjust logic pruned
     Given Customer Account: ALFKI
      When Order RequiredDate altered (2013-10-13)
      Then Balance not adjusted
