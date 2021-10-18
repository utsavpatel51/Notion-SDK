from features.databases import Databases


class NotionClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    @property
    def databases(self):
        return Databases(self)

    # @property
    # def Pages(self):
    #     pass

    # @property
    # def Blocks(self):
    #     pass

    # @property
    # def Users(self):
    #     pass
