Feature: Flipkart Find Product
    Scenario: Navigate to Flipkart and Search Product
        Given I Launch Chrome Browser
        When I Open Flipkart
        And Enter Product Name in search Field
        And Click search button
        And I will be shown list of Products
        And I confirm the product present in obtained list
        And I click on the Product
        And I will be shown product details
        And I Check if product is in Stock
        Then I Close all Browsers