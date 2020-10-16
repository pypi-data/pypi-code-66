"""Tools for interacting with MongoDB databases.
"""

import copy

from pymongo import MongoClient
import alfred3


class MongoDBConnector:
    """Connect to a MongoDB database or collection.

    Effectively, this class provides an interface to an instace of ``pymongo.MongoClient``. For further information on how to interact with a `MongoClient`, please refer to the `pymongo documentation <https://pymongo.readthedocs.io/en/stable/tutorial.html>`_.
    
    :param str host: Hostname or IP address.
    :param int port: Port number on which to connect.
    :param str username: Username for authentication.
    :param str password: Password for authentication.
    :param str database: Database to which to the client will connect.
    :param str collection: Collection inside the specified database to which the client will connect. If left empty, the client will connect directly to the database.
    :param str auth_source: Database to authenticate on. Defaults to "admin", the MongoDB default.
    :param bool ssl: If ``True``, create a connection to the server using Transport Layer Security (TLS/SSL).
    :param str ca_file: Filepath to a file containing a single or a bundle of “certification authority” certificates, which are used to validate certificates passed from the other end of the connection. Implies ``ssl=True``. Defaults to ``None``.
    """

    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        database: str,
        collection: str = None,
        auth_source: str = "admin",
        ssl: bool = False,
        ca_file: str = None,
    ):
        """Constructor method."""

        self._host = host
        self._port = port
        self._db_name = database
        self._collection = collection
        self._username = username
        self._password = password
        self._auth_source = auth_source
        self._ssl = True if ca_file else ssl
        self._ca_file = ca_file

        self._client = None
        self._db = None

        self.connected = False
        """`True`, if a connection was established."""

        self.connect()

    def connect(self):
        """Establish the connection the MongoDB.

        If a collection was specified upon initialisation, the `MongoDBConnector` will connect to this collection. Else, it will connect to the specified database.
        """

        self._client = MongoClient(
            host=self._host,
            port=self._port,
            username=self._username,
            password=self._password,
            authSource=self._auth_source,
            tls=self._ssl,
            tlsCAFile=self._ca_file,
        )

        db = self._client[self._db_name]

        if self._collection:
            db = db[self._collection]

        self._db = db
        self.connected = True

    def disconnect(self):
        """Close the connection to the database."""

        self._client.close()
        self.connected = False

    @property
    def db(self):
        """Return the database or, if specified, collection given upon initialisation.
        
        If the instance of ``MongoDBConnector`` is not currently connected, a call to this property will trigger a call to ``MongoDBConnector.connect()`` before returning the database or collection.
        """

        if self.connected:
            if self._db is None:
                raise TypeError("No collection found.")
            else:
                return self._db

        elif not self.connected:
            self.connect()
            if self._db is None:
                raise TypeError("No collection found.")
            else:
                return self._db


class ExpMongoDBConnector:
    """Connect to an alfred experiment's MongoDB collection.
    
    Connects to the same database and collection that the given alfred 
    experiment uses to save its data. If multiple `MongoSavingAgents` 
    are attached to the experiment, :class:`ExpMongoDBConnector` will connect
    to the `MongoSavingAgent` with the lowest activation level. 
    Basically, it provides access to a copy of the
    :class:`pymongo.collection.Collection` that the experiment's saving agent
    uses. 

    For further information on how to interact with a
    `MongoClient`, please refer to the 
    `pymongo documentation <https://pymongo.readthedocs.io/en/stable/tutorial.html>`_.

    Args:
        experiment: An alfred3 experiment instance.
    """

    def __init__(self, experiment: alfred3.Experiment):
        """Constructor method."""

        self._exp = experiment

        if not isinstance(self._exp, alfred3.Experiment):
            raise ValueError("The input must be an instance of alfred3.Experiment.")

        self.exp_data_agents = []
        self.unlinked_data_agents = []
        self.codebook_agents = []

        self._gather_agents(self.exp_data_agents, self._exp.sac_main)
        self._gather_agents(self.unlinked_data_agents, self._exp.sac_unlinked)
        self._gather_agents(self.codebook_agents, self._exp.sac_codebook)

        self._exp_collection = self._connect(self.exp_data_agents)
        self._unlinked_collection = self._connect(self.unlinked_data_agents)
        self._misc_collection = self._connect(self.codebook_agents)

    def _gather_agents(self, agent_list, sac):
        """Collect all MongoSavingAgents from the provided alfred 
        experiment, sorted by activation level (lowest first).
        
        Args:
            agent_list: The list in which saving agents should be 
                collected.
            sac: The SavingAgentController, from which saving agents
                should be collected.
        """

        for agent in sac.agents.values():
            if isinstance(agent, alfred3.saving_agent.MongoSavingAgent):
                agent_list.append(copy.copy(agent))
        agent_list.sort(key=lambda x: x.activation_level)

    def _connect(self, agent_list):
        """Establishes a connection to the MongoDB collection with the 
        lowest activation level in *agent_list*."""

        if (
            len(agent_list) > 1
            and agent_list[0].activation_level == agent_list[1].activation_level
        ):
            raise ValueError(
                "There are two or more MongoSavingAgents with the highest activation level."
            )

        try:
            return agent_list[0]._col
        except IndexError:
            pass

    @property
    def unlinked_col(self):
        """Returns the unlinked mongoDB collection belonging to the
        experiment.
        """
        if not self._unlinked_collection:
            raise ValueError("No unlinked collection found.")
        return self._unlinked_collection

    @property
    def misc_col(self):
        """Returns the miscellaneous mongoDB collection belonging to the
        experiment.
        """
        if not self._misc_collection:
            raise ValueError("No miscellaneous collection found.")
        return self._misc_collection

    @property
    def db(self):
        """Returns the mongoDB collection from the experiment's 
        ``MongoSavingAgent`` with lowest activation level.
        """
        DeprecationWarning("This property is deprecated. Please use 'exp' instead.")
        if not self._exp_collection:
            raise ValueError("No experiment data collection found.")
        return self._exp_collection

    @property
    def exp_col(self):
        """Returns the mongoDB collection from the experiment's 
        ``MongoSavingAgent`` with lowest activation level.
        """
        if not self._exp_collection:
            raise ValueError("No experiment data collection found.")
        return self._exp_collection
