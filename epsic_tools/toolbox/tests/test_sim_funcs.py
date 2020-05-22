
import os
import numpy.testing as nptest
print(os.getcwd())
from sim_utils import sim_to_hs
from sim_utils import parse_params_file

def test_sim_to_hs():
    root_path = os.path.dirname(epsic.__file__)
    test_data_path = os.join(root_path , 'toolbox', 'tests', 'test_data', 'test_sim.h5')
    d = sim_to_hs(test_data_path)
    shape = d.data.shape
    nptest.assert_equal(shape, (4, 4, 256, 256))

def test_parse_params_file():
    root_path = os.path.dirname(epsic.__file__)
    test_data_path = os.join(root_path , 'toolbox', 'tests', 'test_data', 'test_sim.h5')
    test_params_path = os.join(root_path , 'toolbox', 'tests', 'test_data', 'test_sim_params.txt')
    d = parse_params_file(test_params_path, test_data_path)
    assert t['accel_voltage(eV)'] == 80000
    


