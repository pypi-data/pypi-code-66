from .base import Base

class wallet(Base):
    def __init__(self, url):
        super(wallet, self).__init__(url)

    def wallet_create(self, wallet_name):
        """
        使用给定的名称创建一个新的钱包。

        :param wallet_name: (str)要创建的钱包的名称
        :return:
        """
        path = '/v1/wallet/create'
        return self.post(path, data=wallet_name)

    def wallet_open(self, wallet_name):
        """
        打开给定名称的现有钱包。

        :param wallet_name:(str)待打开钱包的名称
        :return:
        """
        path = '/v1/wallet/open'
        return self.post(path, data=wallet_name)

    def wallet_lock_all(self, wallet_name):
        """
        锁上指定名字的钱包

        :param wallet_name:(str)待打开钱包的名称
        :return:
        """
        path = '/v1/wallet/lock_all'
        return self.post(path, data=wallet_name)

    def wallet_lock_all(self):
        """
        锁定所有的钱包。

        :return:
        """
        path = '/v1/wallet/lock_all'
        return self.get(path=path)

    def wallet_unlock(self, wallet_name_password):
        """
        用给定的名称和密码解锁钱包

        :param wallet_name_passord: (str)包含名称和密码的列表
        of the given wallet
        :return:
        """
        path = '/v1/wallet/unlock'
        return self.post(path, data=wallet_name_password)

    def wallet_import_key(self, wallet_name_privKey):
        """
        将私钥导入到给定名称的钱包

        :param wallet_name_privKey:(str)包含钱包的列表
        name and private key
        :return:
        """
        path = '/v1/wallet/import_key'
        return self.post(path, data=wallet_name_privKey)

    def wallet_list(self):
        """
        列出所有的钱包

        :return:
        """
        path = '/v1/wallet/list_wallets'
        return self.get(path)

    def wallet_list_keys(self):
        """
        列出所有钱包上的所有密钥对

        :return:
        """
        path = '/v1/wallet/list_keys'
        return self.get(path)

    def wallet_get_public_keys(self):
        """
        列出所有钱包上的所有公钥

        :return:
        """
        path = '/v1/wallet/get_public_keys'
        return self.get(path)

    def wallet_set_timeout(self, timeout):
        """
        设置钱包自动锁定超时(秒)

        :param timeout
        :return:
        """
        path = '/v1/wallet/set_timeout'
        return self.post(path, data=timeout)

    def wallet_sign_trx(self, transaction_data):
        """
        给定一个事务数组，对事务进行签名
        公钥和链id
        :param transaction_data: (str)事务json和公钥列表
        :return: response key
        """
        path = '/v1/wallet/sign_transaction'
        return self.post(path, data=transaction_data)
