Feature: Salary Change

  Scenario: Audit Salary Change
     Given Customer Account: VINET
      When Patch Salary to 200k
      Then Salary_audit row created


  Scenario: GET Department
     Given Department 2
      When GET Department with SubDepartments API
      Then SubDepartments returned
