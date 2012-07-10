"""
    clsReynoldsExperiment.py - This class looks after the running of the
    experiment. Setup agents, and starts them running.
"""
#// --------------------------------------------------------------------------
#// ------------------------------------- Modules/Packages to be imported ----
#// --------------------------------------------------------------------------
'''
import re
from string import Template
from string import *
'''

#// ---------------------------------------------------------------------------
#// ------------------------------------- Class Definitions -------------------
#// ---------------------------------------------------------------------------
class clReynoldsExperiment:
    """
        Attributes:

        Methods:

        Exceptions:
            MyClassTopLevelError(Exception)
            MyClassFirstLevelError(MyClassTopLevelError)
    """
    
    def __init__(self, NumRuns, OilDistribution, ResultsFileName, AgentsData):
        """
            The class intialise function.
            Arguments:
                NumRuns = the number of runs in this experiment
                OilDistribution = which oil distribution to use
                ResultsFileName = where to save the aggregate expectations results
                AgentsData = a list of tuples containing each agents information
                             (AgentType, OptimismLevel, PessimismLevel)
            Specifics:
        """
        try:
            print "From experiment class:: Number of Runs: ", NumRuns, " Oil Distribution: ", OilDistribution, " Results Filename: ", ResultsFileName, " Agent Data: ", AgentsData

        except:
            raise ReynoldsExperimentError()

#// -------------------------------------------------------------------------------
#// ------------------------------------- Attribute Definitions -------------------
    def setAttribute(self, NewValue):
        """
            To set the Window Title attribute of the form.
            Arguments:
                strFormTitle: The title for the main window.
            Specifics:
        """
        try:
            self.attribute = NewValue
        except:
            pass
##            raise MyClassTopLevelError()

#// ----------------------------------------------------------------------------
#// ------------------------------------- Method Definitions -------------------
    def GenericMethod(self):
        """
            Generic Method.
            Arguments:
            Specifics:
        """
        try:
            pass
##        except MyClassSecond_B_LevelError:
##            raise MyClassSecond_B_LevelError()
##        except MyClassSecond_A_LevelError:
##            raise MyClassSecond_A_LevelError()
##        except MyClassFirstLevelError:
##            raise MyClassFirstLevelError()
        except:
            pass
##            raise MyClassTopLevelError()



#// -------------------------------------------------------------------------------------
#// ------------------------------------- Internal Method Definitions -------------------
'''    def _InternalGenericMethod(self):
        try:


        except MyClassSecond_B_LevelError:
            raise MyClassSecond_B_LevelError()
        except MyClassSecond_A_LevelError:
            raise MyClassSecond_A_LevelError()
        except:
            raise MyClassFirstLevelError()

    def _A_DeeperInternalGenericMethod(self):
        try:
                      
        except:
            raise MyClassSecond_A_LevelError()
'''

#// ---------------------------------------------------------------------------
#// ------------------------------------- Exception Class Definitions ---------
#// ---------------------------------------------------------------------------
class ReynoldsExperimentError(Exception): pass
'''
class MyClassFirstLevelError(MyClassTopLevelError): pass
class MyClassSecond_A_LevelError(MyClassFirstLevelError): pass
class MyClassSecond_B_LevelError(MyClassFirstLevelError): pass
'''
#// ---------------------------------------------------------------------------
#// ------------------------------------- unittest Test Cases -----------------
#// ---------------------------------------------------------------------------
##class TestMyClass(unittest.TestCase):
##
##    def setUp(self):
##
##    def test_something(self):
##        self.assertEqual(self.seq, list(range(10)))
##        self.assertRaises(TypeError, random.shuffle, (1,2,3))
##
##    def test_something_else(self):
##        self.assertTrue(element in self.seq)


if __name__ == '__main__':
    unittest.main()
