import numpy as np
import numba
from sklearn import svm
import quple
import qiskit
from sklearn.model_selection import GridSearchCV

from .qsvm_logger import QSVMLogger

from pdb import set_trace

@numba.vectorize([numba.float64(numba.complex128),numba.float32(numba.complex64)])
def abs2(x):
    return x.real**2 + x.imag**2


class QSVM:
    def __init__(self):
        pass
    
    @staticmethod
    def get_kernel_matrix(state_vectors_left, state_vectors_right):
        return abs2(state_vectors_left.conjugate() @ state_vectors_right.T)
    
    @staticmethod
    def run(encoding_circuit, x_train, y_train, x_test, y_test, 
            random_seed = 0, backend=None, **kwargs):
        attributes = {}
        attributes['encoding_circuit'] = type(encoding_circuit).__name__
        attributes['feature_dimension'] = x_train.shape[1]
        attributes['train_size'] = x_train.shape[0]
        attributes['test_size'] = x_test.shape[0]
        
        if isinstance(encoding_circuit, quple.ParameterisedCircuit):
            attributes['n_qubit'] = encoding_circuit.n_qubit
            attributes['encoding_map'] = encoding_circuit.encoding_map.__name__ if \
                isinstance(encoding_circuit, quple.data_encoding.EncodingCircuit) else ''            
            logger = QSVMLogger(attributes)
            logger.info('Evaluating state vectors for train data...')
            train_state_vectors = encoding_circuit.get_state_vectors(x_train)
            logger.info('Evaluating state vectors for test data...')
            test_state_vectors = encoding_circuit.get_state_vectors(x_test)
            
        elif isinstance(encoding_circuit, qiskit.QuantumCircuit):    
            attributes['n_qubit'] = encoding_circuit.num_qubits
            attributes['encoding_map'] = encoding_circuit._data_map_func.__name__ 
            logger = QSVMLogger(attributes)            
            from quple.qiskit_interface.tools import get_qiskit_state_vectors
            logger.info('Evaluating state vectors for train data...')
            train_state_vectors = get_qiskit_state_vectors(backend, encoding_circuit, x_train)
            logger.info('Evaluating state vectors for test data...')
            test_state_vectors = get_qiskit_state_vectors(backend, encoding_circuit, x_test)
        else:
            raise ValueError('Unknown type for encoding circuit: {}'.format(type(encoding_circuit)))
        
        logger.info('Evaluating kernel matrix for train data...')
        train_kernel_matrix = QSVM.get_kernel_matrix(train_state_vectors, train_state_vectors)
        logger.info('Evaluating kernel matrix for test data...')
        train_test_kernel_matrix = QSVM.get_kernel_matrix(test_state_vectors, train_state_vectors)

        logger.info('Training started')
        svc = svm.SVC(kernel='precomputed', probability=True, random_state=random_seed)

        tune_params = {
                       'C': [1,10,100,200,400,800],
                       'gamma': [0.01,0.1,1]
                      }

        clf = GridSearchCV(estimator=svc, param_grid=tune_params, n_jobs=-1, cv=3, scoring='roc_auc')

        clf.fit(train_kernel_matrix,y_train)

        logger.on_train_end(clf, train_kernel_matrix, train_test_kernel_matrix, y_test)
        return clf