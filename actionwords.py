# encoding: UTF-8

from atm import ATM
from card import Card
from account import Account

class Actionwords:
    def __init__(self, test):
        self.test = test
        self.atm = ATM(100)
        self.card = Card()
        self.account = Account(100)


    def a_feature_file_named_p1_with_content(self, p1 = "", free_text = ""):
        pass

    def p1_imports_the_feature_file_p2_to_folder_p3(self, p1 = "", p2 = "", p3 = ""):
        pass

    def p1_should_get_a_folder_p2_under_the_folder_p3_with_the_scenarios(self, p1 = "", p2 = "", p3 = "", datatable = ""):
        pass

    def two_scenarios(self, free_text = ""):
        pass

    def p1_renames_globally_the_step_p2responsep3_by_p4responsep5(self, p1 = "", p2 = "", p3 = "", p4 = "", p5 = ""):
        pass

    def the_scenarios_using_step_p1responsep2_should_be(self, p1 = "", p2 = "", free_text = ""):
        pass

    def bob_creates_a_new_step_p1dayp2(self, p1 = "", p2 = ""):
        pass

    def changes_the_two_scenarios_as(self, free_text = ""):
        pass

    def bob_has_only_the_step_p1dayp2_to_maintain_instead_of_these_two(self, p1 = "", p2 = "", datatable = ""):
        pass

    def p1_adds_a_new_scenario_p2_with_the_content(self, p1 = "", p2 = "", free_text = ""):
        pass

    def the_datatable(self, datatable = ""):
        pass

    def p1_has_a_scenario_p2_to_describe_the_same_behaviour_than_these_scenarios(self, p1 = "", p2 = "", datatable = ""):
        pass

    def a_folder_p1_with_the_scenarios(self, p1 = "", datatable = ""):
        pass

    def p1_download_folder_p2(self, p1 = "", p2 = ""):
        pass

    def p1_should_get_a_feature_file_p2_with_content(self, p1 = "", p2 = "", free_text = ""):
        pass

    def the_account_balance_is_100(self):
        self.account.balance = 100

    def the_card_is_valid(self):
        self.card.is_valid = True

    def the_machine_contains_enough_money(self):
        self.atm.balance = 100

    def the_account_holder_requests_20(self):
        self.atm.insert_card(self.card, self.account)
        self.dispensed = self.atm.request_money(20)

    def the_atm_should_dispense_20(self):
        self.test.assertEqual(self.dispensed, 20)

    def the_account_balance_should_be_80(self):
        self.test.assertEqual(self.account.balance, 80)

    def the_card_should_be_returned(self):
        self.test.assertTrue(self.atm.return_card())

    def the_account_balance_is_10(self):
        self.account.balance = 10

    def the_atm_should_not_dispense_any_money(self):
        self.atm.insert_card(self.card, self.account)
        dispensed = self.atm.request_money(20)
        self.test.assertEqual(dispensed, 0)

    def the_atm_should_say_there_are_insufficient_funds(self):
        self.test.assertFalse(self.atm.request_money(20) > 0)

    def the_account_balance_should_be_10(self):
        self.test.assertEqual(self.account.balance, 10)

    def the_card_is_disabled(self):
        self.card.is_valid = False

    def the_atm_should_retain_the_card(self):
        self.test.assertFalse(self.atm.insert_card(self.card, self.account))

    def the_atm_should_say_the_card_has_been_retained(self):
        self.test.assertFalse(self.atm.insert_card(self.card, self.account))

    def the_machine_contains_only_10(self):
        self.atm.balance = 10

    def the_atm_should_say_it_has_insufficient_funds(self):
        self.test.assertFalse(self.atm.request_money(20) > 0)

    def the_account_balance_should_be_100(self):
        self.test.assertEqual(self.account.balance, 100)
