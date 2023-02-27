from Base import BaseClient


class Account(BaseClient):

    def create_account_holder(self, data):

        return self._handle_request(
            method_type="POST",
            url_path="account-holders",
            data=data)

    def get_account_holder_details(self, accountHolderId):
        pass

    def get_accounts_holders_accounts(self, page_size=20, accountHolderId, page_after, page_before):
        pass

    def get_account_holders_accounts_details(
            self, accountHolderId, page_after, page_before):
        pass

    def list_account_holder(self, page_size=20, page_after, page_before):
        pass

    def create_account(self):
        pass

    def get_account_details(self):
        pass

    def list_accounts_holders_relationship(self):
        pass

    def list_accounts_account_holder(self):
        pass

    def list_allocations_relationship(self):
        pass

    def list_account_allocations(self):
        pass

    def list_accounts(self):
        pass


account = Account()
data = {
    "type": "account-holder",
    "attributes": {
        "firstName": "John",
        "lastName": "Snow",
        "middleName": "Marvolo",
        "address": {
            "street": "21 Jump Street",
            "apt_suite_flat_etc": "Apt 21",
            "city": "Boston",
            "postal_zip_code": "02111",
            "country": "UA"
        },
        "dateOfBirth": "2019-08-24",
        "nationality": "U",
        "externalId": "null"
    }
}
res = account.create_account_holder(data=data)
print(res)
