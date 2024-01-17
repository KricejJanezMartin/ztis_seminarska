# encoding: UTF-8
import unittest
from tests.actionwords import Actionwords

class TestZTIS(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_import_a_feature_file(self):
        # You can easily import one or multiple feature files in a folder, by uploading them or directly from a Git repository
        # Given a feature file named "is_it_friday_yet.feature" with content:
        self.actionwords.a_feature_file_named_p1_with_content(p1 = "is_it_friday_yet.feature", free_text = "Feature: Is it Friday yet?\n  Everybody wants to know when it's Friday\n\n  Scenario: Sunday is not Friday\n    Given today is Sunday\n    When I ask whether it's Friday yet\n    Then I should be told \"Nope\"\n\n  Scenario: Friday is Friday\n    Given today is Friday\n    When I ask whether it's Friday yet\n    Then I should be told \"TGIF\"")
        # When "Bob" imports the feature file "is_it_friday_yet.feature" to folder "Calendar"
        self.actionwords.p1_imports_the_feature_file_p2_to_folder_p3(p1 = "Bob", p2 = "is_it_friday_yet.feature", p3 = "Calendar")
        # Then "Bob" should get a folder "Is it Friday yet?" under the folder "Calendar" with the scenarios:
        self.actionwords.p1_should_get_a_folder_p2_under_the_folder_p3_with_the_scenarios(p1 = "Bob", p2 = "Is it Friday yet?", p3 = "Calendar", datatable = "      | scenario-name |\n      | Sunday is not Friday |\n      | Friday is Friday |")

    def test_rename_a_step_in_every_scenarios_that_use_it(self):
        # While editing a step in a scenario or in a feature background, you can decide whether the modification should impact only the current step or every places where this step is used
        # Given two scenarios
        self.actionwords.two_scenarios(free_text = "  Scenario: Sunday is not Friday\n    Given today is Sunday\n    When I ask whether it's Friday yet\n    Then I should be told \"Nope\"\n\n  Scenario: Friday is Friday\n    Given today is Friday\n    When I ask whether it's Friday yet\n    Then I should be told \"TGIF\"")
        # When "Bob" renames globally the step "Then I should be told "response"" by "Then I should get the answer "response""
        self.actionwords.p1_renames_globally_the_step_p2responsep3_by_p4responsep5(p1 = "Bob", p2 = "Then I should be told ", p3 = "", p4 = "Then I should get the answer ", p5 = "")
        # Then the scenarios using step "Then I should be told "response"" should be:
        self.actionwords.the_scenarios_using_step_p1responsep2_should_be(p1 = "Then I should be told ", p2 = "", free_text = "  Scenario: Sunday is not Friday\n    Given today is Sunday\n    When I ask whether it's Friday yet\n    Then I should get the answer \"Nope\"\n\n  Scenario: Friday is Friday\n    Given today is Friday\n    When I ask whether it's Friday yet\n    Then I should get the answer \"TGIF\"")

    def test_use_parameters_in_a_step(self):
        # It is possible to collapse similar steps into a single one by using **parameters**
        # It makes future modifications on this step easier, for example to modify your business language, and accelerates automation of your features as there is only one step to automate instead of multiple ones.
        # Given two scenarios
        self.actionwords.two_scenarios(free_text = "Scenario: Sunday isn't Friday\n  Given today is Sunday\n  When I ask whether it's Friday yet\n  Then I should be told \"Nope\"\n\nScenario: Friday is Friday\n  Given today is Friday\n  When I ask whether it's Friday yet\n  Then I should be told \"TGIF\"")
        # When Bob creates a new step "today is "day""
        self.actionwords.bob_creates_a_new_step_p1dayp2(p1 = "today is ", p2 = "")
        # And changes the two scenarios as
        self.actionwords.changes_the_two_scenarios_as(free_text = "Scenario: Sunday isn't Friday\n  Given today is \"Sunday\"\n  When I ask whether it's Friday yet\n  Then I should be told \"Nope\"\n\nScenario: Friday is Friday\n  Given today is \"Friday\"\n  When I ask whether it's Friday yet\n  Then I should be told \"TGIF\"")
        # Then Bob has only the step "today is "day"" to maintain instead of these two
        self.actionwords.bob_has_only_the_step_p1dayp2_to_maintain_instead_of_these_two(p1 = "today is ", p2 = "", datatable = "      | step |\n      | today is Sunday |\n      | today is Friday |")

    def test_scenario_with_multiple_examples(self):
        # You can collapse multiple similar scenarios into one using **Datatable** and **parameters** in steps
        # Given two scenarios
        self.actionwords.two_scenarios(free_text = "Scenario: Sunday isn't Friday\n    Given today is Sunday\n    When I ask whether it's Friday yet\n    Then I should be told \"Nope\"\n\n  Scenario: Friday is Friday\n    Given today is Friday\n    When I ask whether it's Friday yet\n    Then I should be told \"TGIF\"")
        # When "Bob" adds a new scenario "Today is or is not Friday" with the content
        self.actionwords.p1_adds_a_new_scenario_p2_with_the_content(p1 = "Bob", p2 = "Today is or is not Friday", free_text = "Given today is \"=day\"\nWhen I ask whether it's Friday yet\nThen I should be told \"=answer\"")
        # And the datatable
        self.actionwords.the_datatable(datatable = "       | day            | answer |\n       | Friday         | TGIF |\n       | Sunday         | Nope |\n       | anything else! | Nope |")
        # Then "Bob" has a scenario "Today is or is not Friday" to describe the same behaviour than these scenarios
        self.actionwords.p1_has_a_scenario_p2_to_describe_the_same_behaviour_than_these_scenarios(p1 = "Bob", p2 = "Today is or is not Friday", datatable = "      | scenario name |\n      | Sunday isn't Friday |\n      | Friday is Friday |")

    def test_download_feature_file(self):
        # Once your feature is ready, you can export it as a **.feature** file so it can be automated
        # Given a folder "Is it Friday yet?" with the scenarios:
        self.actionwords.a_folder_p1_with_the_scenarios(p1 = "Is it Friday yet?", datatable = "      | scenario-name |\n      | Sunday is not Friday |\n      | Friday is Friday |")
        # When "Bob" download folder "Is it Friday yet?"
        self.actionwords.p1_download_folder_p2(p1 = "Bob", p2 = "Is it Friday yet?")
        # Then "Bob" should get a feature file "is_it_friday_yet.feature" with content:
        self.actionwords.p1_should_get_a_feature_file_p2_with_content(p1 = "Bob", p2 = "is_it_friday_yet.feature", free_text = "Feature: Is it Friday yet?\n  Everybody wants to know when it's Friday\n\n  Scenario: Sunday is not Friday\n    Given today is Sunday\n    When I ask whether it's Friday yet\n    Then I should be told \"Nope\"\n\n  Scenario: Friday is Friday\n    Given today is Friday\n    When I ask whether it's Friday yet\n    Then I should be told \"TGIF\"")

    def test_account_has_sufficient_funds(self):
        # Given the account balance is $100
        self.actionwords.the_account_balance_is_100()
        # And the card is valid
        self.actionwords.the_card_is_valid()
        # And the machine contains enough money
        self.actionwords.the_machine_contains_enough_money()
        # When the Account Holder requests $20
        self.actionwords.the_account_holder_requests_20()
        # Then the ATM should dispense $20
        self.actionwords.the_atm_should_dispense_20()
        # And the account balance should be $80
        self.actionwords.the_account_balance_should_be_80()
        # And the card should be returned
        self.actionwords.the_card_should_be_returned()

    def test_account_has_insufficient_funds(self):
        # Given the account balance is $10
        self.actionwords.the_account_balance_is_10()
        # And the card is valid
        self.actionwords.the_card_is_valid()
        # And the machine contains enough money
        self.actionwords.the_machine_contains_enough_money()
        # When the Account Holder requests $20
        self.actionwords.the_account_holder_requests_20()
        # Then the ATM should not dispense any money
        self.actionwords.the_atm_should_not_dispense_any_money()
        # And the ATM should say there are insufficient funds
        self.actionwords.the_atm_should_say_there_are_insufficient_funds()
        # And the account balance should be $10
        self.actionwords.the_account_balance_should_be_10()
        # And the card should be returned
        self.actionwords.the_card_should_be_returned()

    def test_card_has_been_disabled(self):
        # Given the card is disabled
        self.actionwords.the_card_is_disabled()
        # When the Account Holder requests $20
        self.actionwords.the_account_holder_requests_20()
        # Then the ATM should retain the card
        self.actionwords.the_atm_should_retain_the_card()
        # And the ATM should say the card has been retained
        self.actionwords.the_atm_should_say_the_card_has_been_retained()

    def test_the_atm_has_insufficient_funds(self):
        # Given the account balance is $100
        self.actionwords.the_account_balance_is_100()
        # And the card is valid
        self.actionwords.the_card_is_valid()
        # And the machine contains only $10
        self.actionwords.the_machine_contains_only_10()
        # When the Account Holder requests $20
        self.actionwords.the_account_holder_requests_20()
        # Then the ATM should not dispense any money
        self.actionwords.the_atm_should_not_dispense_any_money()
        # And the ATM should say it has insufficient funds
        self.actionwords.the_atm_should_say_it_has_insufficient_funds()
        # And the account balance should be $100
        self.actionwords.the_account_balance_should_be_100()
        # And the card should be returned
        self.actionwords.the_card_should_be_returned()
