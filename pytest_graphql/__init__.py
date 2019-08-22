import pytest
from aiohttp.test_utils import AioHTTPTestCase
from aiohttp.web import Application


class GraphQLTestCase(AioHTTPTestCase):
    async def setUpAsync(self):
        self.affected_tables = []
        self.session = (await self.get_application())["db"]

    async def tearDownAsync(self):
        if not self.affected_tables:
            return
        for table in self.affected_tables:
            self.session.execute(f"TRUNCATE {table}")

        self.affected_tables = []

    async def get_application(self) -> Application:
        """
        Method to returns the Application object.
        Needs to be implemented in test cases
        """
        pass

    async def query_graphql(self, query: str, variables: dict = None):
        """
        Helper method to post a graphql query.
        """
        headers = {"content-type": "application/json"}
        json = {"query": query}

        if variables:
            json["variables"] = variables

        return await self.client.post("/graphql", headers=headers, json=json)
