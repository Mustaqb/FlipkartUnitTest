Feature: Flipkart Find Product
    Scenario: Navigate to Flipkart and Search Product
        Given I Launch Chrome Browser
        When I Open Flipkart
        And Enter Product Name in search Field
        Then Click search button
    
    Scenario: Search for the Product
        Given I will be shown list of Products
        When I confirm the product present in obtained list
        Then I click on the product

    Scenario: Check For the Product 
        Given I will be shown product details
        When I Check if product is in Stock
        Then I Close all Browsers