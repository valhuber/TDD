Feature: Salary Change

  Scenario: Audit Salary Change
     Given Customer Account: VINET
      When Patch Salary to 200k
      Then Salary_audit row created
