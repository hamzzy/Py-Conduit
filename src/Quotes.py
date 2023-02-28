from Base import BaseClient


class Quotes(BaseClient):

    def create_quotes(self, data):

        return self._handle_request(
            method_type="POST",
            url_path="quotes",
            data=data)

    def get_quotes_details(self, qoute_id):

        return self._handle_request(
            method_type="GET",
            url_path="quotes",
            params={
                "qouteId": qoute_id})

    def list_quotes(
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
            "GET", url_path="", params=query)



