from .base import Base

class chain(Base):
    def __init__(self, url):
        super(chain, self).__init__(url)

    def get_info(self):
        """
        获取与节点相关的最新信息

        :return:
        """
        return self.get("/v1/chain/get_info")

    def get_block(self, block_num_or_id):
        """
        获取一个块的信息

        :param block_num_or_id: id值
        :return:
        """
        data_dict = {
            "block_num_or_id": block_num_or_id
        }
        return self.post("/v1/chain/get_block", data=data_dict)

    def get_account(self, account_name):
        """
        获取账户的信息

        :param account_name: 账户名
        :return:
        """
        data_dict = {
            "account_name": account_name
        }
        return self.post("/v1/chain/get_account", data=data_dict)

    def get_code(self, account_name):
        """
        获取智能合约代码

        :param account_name: 账户名
        :return:
        """
        data_dict = {
            "account_name": account_name,
            "code_as_wasm": "true"
        }
        return self.post("/v1/chain/get_code", data=data_dict)

    def get_table_rows(self, account_details):
        """
        从帐户中获取智能合同数据。

        :param account_details: (str)帐户详细信息，格式
        must be a string of a json
        :return: response object
        """
        path = '/v1/chain/get_table_rows'

        return self.post(path, data=account_details)

    def abi_json_to_bin(self, data):
        """
        将json序列化为二进制十六进制。生成的二进制十六进制通常是
        用于push_transaction中的数据字段。

        :param data: json 字符串
        :return: response object
        """
        path = '/v1/chain/abi_json_to_bin'
        return self.post(path, data=data)

    def abi_bin_to_json(self, data):
        """
        将二进制十六进制序列化回json。

        :param data: json字符串
        :return:response object
        """
        path = '/v1/chain/abi_bin_to_json'
        return self.post(path, data=data)

    def push_transaction(self, transaction):
        """
        这个方法期望一个JSON格式的事务，并且将会这样做
        试着把它应用到区块链上，

        :param transaction: json字符串
        :return: response object
        """
        path = '/v1/chain/push_transaction'
        return self.post(path, data=transaction)

    def push_transactions(self, transactions):
        """
        此方法一次推送多个事务。

        :param transactions: json字符串
        :return: response object
        """
        path = '/v1/chain/push_transaction'
        return self.post(path, data=transactions)

    def get_required_keys(self, transaction_data):
        """
        从您的密钥列表中获取签署事务所需的密钥。

        :param transaction_data: json字符串
        :return: response object
        """
        path = '/v1/chain/get_required_keys'
        return self.post(path, data=transaction_data)
