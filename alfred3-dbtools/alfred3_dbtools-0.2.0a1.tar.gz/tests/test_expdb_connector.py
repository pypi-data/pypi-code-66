import copy
import pytest
import mongomock
import alfred3 as al

from alfred3_dbtools.mongotools import ExpMongoDBConnector


@pytest.fixture
def exp(tmp_path):
    config = al.config.init_configuration(expdir=tmp_path)
    client = mongomock.MongoClient()
    exp = al.Experiment(config=config)

    exp_agent = al.saving_agent.MongoSavingAgent(
        client=client, database="alfred", collection="exp_col", experiment=exp, name="a1"
    )
    unlinked_agent = al.saving_agent.MongoSavingAgent(
        client=client, database="alfred", collection="unlinked_col", experiment=exp, name="a2"
    )
    codebook_agent = al.saving_agent.MongoSavingAgent(
        client=client, database="alfred", collection="misc_col", experiment=exp, name="a3"
    )

    exp.sac_main.append(exp_agent)
    exp.sac_unlinked.append(unlinked_agent)
    exp.sac_codebook.append(codebook_agent)

    return exp


class TestExpDBConnector:
    def test_init(self, exp):
        db = ExpMongoDBConnector(experiment=exp)
        assert db

    def test_access(self, exp):
        db = ExpMongoDBConnector(experiment=exp)
        assert db.exp_col
        assert db.db
        assert db.unlinked_col
        assert db.misc_col

    def test_multi_agent(self, exp):
        client = mongomock.MongoClient()
        a1b = al.saving_agent.MongoSavingAgent(
            client=client,
            database="alfred",
            collection="exp_col2",
            experiment=exp,
            name="a1b",
            activation_level=1,
        )
        exp.sac_main.append(a1b)
        exp.sac_main.agents["a1"].activation_level = 2

        db = ExpMongoDBConnector(experiment=exp)

        assert db.exp_col.name == "exp_col2"

        a1c = al.saving_agent.MongoSavingAgent(
            client=client,
            database="alfred",
            collection="exp_col3",
            experiment=exp,
            name="a1c",
            activation_level=0.5,
        )

        exp.sac_main.append(a1c)

        db2 = ExpMongoDBConnector(experiment=exp)

        assert db2.exp_col.name == "exp_col3"

    def test_no_agent(self, exp):
        exp.sac_main._agents = {}
        exp.sac_unlinked._agents = {}
        exp.sac_codebook._agents = {}
        db = ExpMongoDBConnector(exp)

        with pytest.raises(ValueError):
            db.exp_col

        with pytest.raises(ValueError):
            db.db

        with pytest.raises(ValueError):
            db.unlinked_col

        with pytest.raises(ValueError):
            db.misc_col
