from api_endpoint import APIEndpoint


class Databases(APIEndpoint):

    def query_database(self, database_id: str, **kwargs):
        """Query a database

        Args:
            database_id (str)
        Keyword Args:
            filter (Optional[dict]):
                When supplied, limits which pages are
                returned based on the "https://developers.notion.com/reference
                /post-database-query#post-database-query-filter".

                Example:- {or: [
                            {
                                property: 'In stock',
                                checkbox: {
                                    equals: true,
                                },
                            },
                            {
                                property: 'Cost of next trip',
                                number: {
                                    greater_than_or_equal_to: 2,
                                },
                            },
                        ]}
            sort (Optional[list]):
                When supplied, orders the results based on
                the provided https://developers.notion.com/reference/
                post-database-query#post-database-query-sort.

                Example:- [{
                        property: 'Last ordered',
                        direction: 'ascending',
                        },]
            start_cursor (Optional[string]):
                When supplied, returns a page of
                results starting after the cursor provided. If not supplied,
                this endpoint will return the first page of results.
            page_size(Optionalint]):
                The number of items from the full list desired in the response.
                Maximum: 100. Deafult it will provide the iterator of all items

        Returns:
            Response
        """
        path = "/databases/%s/query" % (database_id)
        payload = {}
        if kwargs.get('filter'):
            payload['filter'] = kwargs['filter']
        if kwargs.get('sorts'):
            payload['sorts'] = kwargs['sorts']
        if kwargs.get('start_cursor'):
            payload['start_cursor'] = kwargs['start_cursor']
        if kwargs.get('page_size'):
            payload['page_size'] = kwargs['page_size']

        data = self.post(path, payload=payload)
        if kwargs.get('page_size'):
            return data
        else:
            while data.get('has_more', False):
                yield data
                payload['start_cursor'] = data.get('next_cursor')
                data = self.post(path, payload=payload)
            yield data

    def create_database(self, page_id: str, properties: dict, **kwargs):
        """Create a database

        Args:
            page_id (str)
        Keyword Args:
            properties: (dict)
                Property schema of database. The keys are the names of
                properties as they appear in Notion and the values are
                property schema objects. https://developers.notion.com/
                reference/create-a-database#property-schema-object

                Example: {
                    "Name": {
                        "title": {}
                    },
                    "Description": {
                        "rich_text": {}
                    }
                }

            title (Optional[list]):
                Title of database as it appears in Notion. An array of rich
                text objects. https://developers.notion.com/reference/rich-text

                Example: [
                    {
                        "type": "text",
                        "text": {
                            "content": "Grocery List",
                            "link": null
                        }
                    }
                ]

        Returns:
            [type]: [description]
        """
        path = "/databases"
        payload = {}
        payload['parent'] = {
            "type": "page_id",
            "page_id": page_id
            }
        payload['properties'] = properties
        if kwargs.get('title'):
            payload['title'] = kwargs['title']

        return self.post(path, payload=payload)

    def update_database(self):
        pass

    def retrieve_database(self):
        pass
