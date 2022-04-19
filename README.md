## Notion_SDK
Notion_SDK is pythonic interface to use [Notion Beta API](https://developers.notion.com/reference/intro).

###  Getting Started

    from Notion_SDK import NotionClient
    notion_client = NotionClient("NOTION_ACCESS_TOKEN")
Now to use [database](https://developers.notion.com/reference/database) related API we can simply write.

    response = notion_client.databases.query_database("database_id")
    print(response)
