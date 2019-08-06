# PyTest GraphQL

A TestCase for PyTest based on AioHTTPTestCase, with GraphQL and Scylla.

The `get_application` method needs to be implemented in the test case.

Method `query_graphql` allows you to send a query to the graphql endpoint, and takes a query and optionally variables.

On test teardown, if `self.affected_tables` contains table names, these tables will be truncated.
