Feature: Application Integration

  Scenario: GET Customer
     Given Customer Account: ALFKI
      When GET Customer API
      Then ALFKI retrieved


  Scenario: GET Department
     Given Department TBD
      When GET Department with SubDepartments API
      Then SubDepartments returned
