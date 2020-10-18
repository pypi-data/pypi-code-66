from contextlib import contextmanager 
from bizai.framework.persistence.persistencevolume import FilePersistenceVolume, DBPersistenceVolume

@contextmanager
def transaction_handler(file_persistence_volume: FilePersistenceVolume, db_persistence_volume: DBPersistenceVolume, **params): 
    print ("Calling contextmanager transaction_handler")
    try:
        db_persistence_volume.set_autocommit_mode (False)

        yield file_persistence_volume, db_persistence_volume
    except:
        rollback(file_persistence_volume, db_persistence_volume)
        # raise
    else:
        commit(file_persistence_volume, db_persistence_volume)
    
    
def commit (file_persistence_volume, db_persistence_volume):
    print ("commit called")

def rollback (file_persistence_volume, db_persistence_volume):
    print ("rollback called")


# python -m bizai.framework.decorators.transactioncontext
if __name__ == "__main__":
    print ("bizai.framework.decorators.transactioncontext Main called")
