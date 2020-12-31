# demo to show the passing the step parameter to the another step

Feature:Sharing the data between steps and scenario (globally)

    Scenario:Refund should process

        Given I find the random order from the database
        When I initiate the refund for the order
        Then the payment should get processed for the user


    Scenario:Refund should be fail on any refunded order

        When I issue a refund on the same order
        Then  the refund should fail