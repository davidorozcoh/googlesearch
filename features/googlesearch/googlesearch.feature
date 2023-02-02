Feature: Google Search

   Background: Search on Google
     Given I’m on the homepage

   Scenario: User can search with “Google Search”
     When I type test automation into the search field
     And I click the Google search button
     Then I go to the search results page, and the first 3 results contain the word automation


   Scenario: User can go to the first search result
     Given I search test automation by keyword in field
     When I click on the first result link
     Then I go to the page, and the page title contains the word automation

