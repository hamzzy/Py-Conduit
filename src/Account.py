from Base import BaseClient


class Account(BaseClient):

    def create_account_holder(self, data):

        return self._handle_request(
            method_type="POST",
            url_path="account-holders",
            data=data)

    def get_account_holder_details(self, accountHolderId):

        return self._handle_request(
            method_type="GET",
            url_path="account-holders/",
            params={
                "accountHolderId": accountHolderId})

    def get_accounts_holders_accounts(
            self,
            account_holder_id,
            page_after='',
            page_before='',
            page_size=20):
        query = {
            "page[size]": page_size,
            "page[after]": page_after,
            "page[before]": page_before
        }
        return self._handle_request(
            "GET",
            url_path=f'account-holders/${account_holder_id}/relationships/accounts',
            params=query)

    def get_account_holders_accounts_details(
            self,
            account_holder_id,
            page_after=None,
            page_before=None,
            page_size=20):
        query = {
            "page[size]": page_size,
            "page[after]": page_after,
            "page[before]": page_before
        }
        return self._handle_request(
            "GET",
            url_path=f'account-holders/{account_holder_id}/accounts',
            params=query)

    def list_account_holder(
            self,
            page_size=20,
            page_after='',
            page_before=''):
        query = {
            "page[size]": page_size,
            "page[after]": page_after,
            "page[before]": page_before
        }
        return self._handle_request(
            "GET", url_path="account-holders", params=query)

    def create_account(self, data):

        return self._handle_request(
            "POST", url_path="accounts", data=data)

    def get_account_details(self, account_id):

        return self._handle_request(
            method_type="GET",
            url_path="accounts/",
            params={
                "accountId": account_id})

    def list_accounts_holders_relationship(
            self, account_id):
        return self._handle_request(
            "GET",
            url_path=f"accounts/${account_id}/relationships/account-holders")

    def list_accounts_account_holder(self, account_id):
        return self._handle_request(
            "GET", url_path=f"accounts/${account_id}/account-holders")

    def list_allocations_relationship(
            self,
            account_id,
            page_after='',
            page_before='',
            page_size=20):

        return self._handle_request(
            "GET",
            url_path=f"accounts/${account_id}/relationships/allocations?page[size]={page_size}&page[after]={page_after}&page[before]={page_before}")

    def list_account_allocations(
            self,
            account_id,
            page_after='',
            page_before='',
            page_size=20):

        return self._handle_request(
            "GET",
            url_path=f"accounts/${account_id}/allocations?page[size]={page_size}&page[after]={page_after}&page[before]={page_before}")

    def list_accounts(
            self,
            page_after='',
            page_before='',
            page_size=20):
        query = {
            "page[size]": page_size,
            "page[after]": page_after,
            "page[before]": page_before
        }
        return self._handle_request(
            method_type="GET",
            url_path="accounts/",
            params=query)
