"""
    ReynoldsWindow.py The basic form for starting the Reynolds oil
                      exploration game. Allows the researcher to define certain
                      key variables such as the oil distribution and the
                      number of runs.
"""

#// --------------------------------------------------------------------------
#// ------------------------------------- Modules/Packages to be imported ----
#// --------------------------------------------------------------------------
from Tkinter import *
import tkFont
import tkMessageBox as messagebox
import sys

#// --------------------------------------------------------------------------
#// ------------------------------------- Class Modules to be imported -------
#// --------------------------------------------------------------------------
import clsReynoldsExperiment
from clsReynoldsExperiment import *

#// ---------------------------------------------------------------------------
#// ------------------------------------- Class Definitions -------------------
#// ---------------------------------------------------------------------------
class frmApplicationWindow(Frame):
    """
        Tk Widgets:

        Attributes:

        Methods:

    """

    def __init__(self, GUIsession=None):
        """
            The form intialise function.
            Arguments:
                GUIsession: The actual tk session for the form
            Specifics:

        """

        try:
            #// This section puts an area to write widgets to.
            Frame.__init__(self, GUIsession)
            self.pack(expand=YES)

            self._CreateWidgets()
        except ReynoldsWindowCreateWidgetsError as AnError:
            raise ReynoldsWindowCreateWidgetsError(AnError)
        except:
            raise ReynoldsWindowError("Window Failed to Start")
            
#// -------------------------------------------------------------------------------
#// ------------------------------------- Attribute Definitions -------------------
    def setTitle(self, strFormTitle):
        """
            To set the Window Title attribute of the form.
            Arguments:
                strFormTitle: The title for the main window.
            Specifics:
        """
        try:
            self.master.title(strFormTitle)
        except:
            messagebox.showwarning("Window Error", "setTitle Failed")            


#// ----------------------------------------------------------------------------
#// ------------------------------------- Method Definitions -------------------
    def GenericMethod(self):
        """
            What the method does
            Arguments:
            Specifics:
        """
        try:
            print ("hi there, everyone!")
        except:
            messagebox.showwarning("Method Error", "GenericMethod Failed")

#// -------------------------------------------------------------------------------------
#// ------------------------------------- Internal Method Definitions -------------------
    def _CreateWidgets(self):
        """
            This intialises and displays the windows widgets
            Arguments:
            Specifics:
        """
        try:
            #-------------------------- finally setup any application specific attributes -------------------------------------------------------------------
            self._CreateWidgetsOilDistribution()
            self._CreateWidgetsNumberOfRuns()
            self._CreateWidgetsResultsFileName()

            self._CreateWidgetsAgentsMatrixLabels()
            self._CreateWidgetsAgentsOptimistic()
            self._CreateWidgetsAgentsPessimistic()
            self._CreateWidgetsAgentsStubborn()
            self._CreateWidgetsAgentsOpportunistic()
            self._CreateWidgetsAgentsNeutral()

            self._CreateWidgetsButtons()

        #// Custom Class Error's first
        except ReynoldsWindowCreateWidgetsError as AnError:
            raise ReynoldsWindowCreateWidgetsError(AnError)
        except:
            raise ReynoldsWindowCreateWidgetsError("_CreateWidgets Failed")
            messagebox.showwarning("Internal Method Error", "_CreateWidgets Failed")

    def _CreateWidgetsButtons(self):
        """
            This intialises and displays the windows widgets
            Arguments:
            Specifics:
        """
        try:
            #-------------------------- finally setup any application specific attributes -------------------------------------------------------------------
            self.btnCommenceExperiment = Button(self)
            self.btnCommenceExperiment["text"] = "Commence Experiment"
            self.btnCommenceExperiment["command"] =  self._CommenceExperiment
            self.btnCommenceExperiment.grid(row=0, column=2, sticky=E+W)

##            self.btnExit = Button(self)
##            self.btnExit["text"] = "QUIT"
##            self.btnExit["command"] =  self._CloseWindow
##            self.btnExit.grid(row=0, column=3, sticky=E+W)

        #// Custom Class Error's first
        except:
            raise ReynoldsWindowCreateWidgetsError("_CreateWidgetsButtons Failed")
            messagebox.showwarning("Internal Method Error", "_CreateWidgetsButtons Failed")

    def _CreateWidgetsOilDistribution(self):
        """
            This intialises and displays the Oil distribution widgets
            Arguments:
            Specifics:
        """
        try:

            Label(self, text="Oil Distributions").grid(row=0, column=0)
            self.lboxOilDistributions = Listbox(self)
            self.lboxOilDistributions.grid(row=0, column=1)
            self.lboxOilDistributions.insert(END, "Reynolds")
            self.lboxOilDistributions.insert(END, "Uniform")
            self.lboxOilDistributions.insert(END, "LinearShallow")
            self.lboxOilDistributions.insert(END, "LinearSteep")
            
        #// Custom Class Error's first
        except:
            raise ReynoldsWindowCreateWidgetsError("_CreateWidgetsOilDistribution Failed")
            messagebox.showwarning("Internal Method Error", "_CreateWidgetsOilDistribution Failed")

    def _CreateWidgetsNumberOfRuns(self):
        """
            This intialises and displays the Number of runs widgets
            Arguments:
            Specifics:
        """
        try:

            Label(self, text="Number Of Runs").grid(row=1, column=0)
            self.NumberOfRuns = StringVar()
            self.NumberOfRuns.set("1")
            self.txtNumberOfRuns = Entry(self, textvariable=self.NumberOfRuns)
            self.txtNumberOfRuns.grid(row=1, column=1)
            
        #// Custom Class Error's first
        except:
            raise ReynoldsWindowCreateWidgetsError("_CreateWidgetsNumberOfRuns Failed")
            messagebox.showwarning("Internal Method Error", "_CreateWidgetsNumberOfRuns Failed")

    def _CreateWidgetsResultsFileName(self):
        """
            This intialises and displays the results file name widgets
            Arguments:
            Specifics:
        """
        try:

            Label(self, text="Results File Name").grid(row=1, column=2)
            self.ResultsFileName = StringVar()
            self.ResultsFileName.set("results1.csv")
            self.txtResultsFileName = Entry(self, textvariable=self.ResultsFileName)
            self.txtResultsFileName.grid(row=1, column=3)

        #// Custom Class Error's first
        except:
            raise ReynoldsWindowCreateWidgetsError("_CreateWidgetsResultsFileName Failed")
            messagebox.showwarning("Internal Method Error", "_CreateWidgetsResultsFileName Failed")

    def _CreateWidgetsAgentsMatrixLabels(self):
        """
            This intialises and displays the labels for the agents matrix
            Arguments:
            Specifics:
        """
        try:

            LabelFont = tkFont.Font(weight='bold')
            Label(self, text="Agent Type", font=LabelFont, fg="orange").grid(row=3, column=0)
            Label(self, text="Optimism Level", font=LabelFont, fg="orange").grid(row=3, column=1)
            Label(self, text="Pessimism Level", font=LabelFont, fg="orange").grid(row=3, column=2)
            Label(self, text="Number of Agents", font=LabelFont, fg="orange").grid(row=3, column=3)

            Label(self, text="Optimistic", font=LabelFont, fg="red").grid(row=4, column=0)
            Label(self, text="Pessimistic", font=LabelFont, fg="green").grid(row=5, column=0)
            Label(self, text="Stubborn", font=LabelFont, fg="blue").grid(row=6, column=0)
            Label(self, text="Opportunistic", font=LabelFont, fg="brown").grid(row=7, column=0)
            Label(self, text="Neutral", font=LabelFont, fg="purple").grid(row=8, column=0)

        #// Custom Class Error's first
        except:
            raise ReynoldsWindowCreateWidgetsError("_CreateWidgetsAgentsMatrixLabels Failed")
            messagebox.showwarning("Internal Method Error", "_CreateWidgetsAgentsMatrixLabels Failed")

    def _CreateWidgetsAgentsOptimistic(self):
        """
            This intialises and displays the optimistic agent's widgets
            Arguments:
            Specifics:
        """
        try:

            self.OptimisticOptimism = StringVar()
            self.OptimisticOptimism.set("10")
            self.txtOptimisticOptimism = Entry(self, textvariable=self.OptimisticOptimism)
            self.txtOptimisticOptimism.grid(row=4, column=1)
            self.OptimisticPessimism = StringVar()
            self.OptimisticPessimism.set("5.625")
            self.txtOptimisticPessimism = Entry(self, textvariable=self.OptimisticPessimism)
            self.txtOptimisticPessimism.grid(row=4, column=2)
            self.NumberOfOptimists = StringVar()
            self.NumberOfOptimists.set("0")
            self.txtNumberOfOptimists = Entry(self, textvariable=self.NumberOfOptimists)
            self.txtNumberOfOptimists.grid(row=4, column=3)

        #// Custom Class Error's first
        except:
            raise ReynoldsWindowCreateWidgetsError("_CreateWidgetsAgentsOptimistic Failed")
            messagebox.showwarning("Internal Method Error", "_CreateWidgetsAgentsOptimistic Failed")

    def _CreateWidgetsAgentsPessimistic(self):
        """
            This intialises and displays the pessimistic agent's widgets
            Arguments:
            Specifics:
        """
        try:

            self.PessimisticOptimism = StringVar()
            self.PessimisticOptimism.set("20")
            self.txtPessimisticOptimism = Entry(self, textvariable=self.PessimisticOptimism)
            self.txtPessimisticOptimism.grid(row=5, column=1)
            self.PessimisticPessimism = StringVar()
            self.PessimisticPessimism.set("50")
            self.txtPessimisticPessimism = Entry(self, textvariable=self.PessimisticPessimism)
            self.txtPessimisticPessimism.grid(row=5, column=2)
            self.NumberOfPessimists = StringVar()
            self.NumberOfPessimists.set("0")
            self.txtNumberOfPessimists = Entry(self, textvariable=self.NumberOfPessimists)
            self.txtNumberOfPessimists.grid(row=5, column=3)

        #// Custom Class Error's first
        except:
            raise ReynoldsWindowCreateWidgetsError("_CreateWidgetsAgentsPessimistic Failed")
            messagebox.showwarning("Internal Method Error", "_CreateWidgetsAgentsPessimistic Failed")

    def _CreateWidgetsAgentsStubborn(self):
        """
            This intialises and displays the stubborn agent's widgets
            Arguments:
            Specifics:
        """
        try:

            self.StubbornOptimism = StringVar()
            self.StubbornOptimism.set("56.25")
            self.txtStubbornOptimism = Entry(self, textvariable=self.StubbornOptimism)
            self.txtStubbornOptimism.grid(row=6, column=1)
            self.StubbornPessimism = StringVar()
            self.StubbornPessimism.set("100")
            self.txtStubbornPessimism = Entry(self, textvariable=self.StubbornPessimism)
            self.txtStubbornPessimism.grid(row=6, column=2)
            self.NumberOfStubborn = StringVar()
            self.NumberOfStubborn.set("0")
            self.txtNumberOfStubborn = Entry(self, textvariable=self.NumberOfStubborn)
            self.txtNumberOfStubborn.grid(row=6, column=3)

        #// Custom Class Error's first
        except:
            raise ReynoldsWindowCreateWidgetsError("_CreateWidgetsAgentsStubborn Failed")
            messagebox.showwarning("Internal Method Error", "_CreateWidgetsAgentsStubborn Failed")

    def _CreateWidgetsAgentsOpportunistic(self):
        """
            This intialises and displays the opportunistic agent's widgets
            Arguments:
            Specifics:
        """
        try:

            self.OpportunisticOptimism = StringVar()
            self.OpportunisticOptimism.set("5.625")
            self.txtOpportunisticOptimism = Entry(self, textvariable=self.OpportunisticOptimism)
            self.txtOpportunisticOptimism.grid(row=7, column=1)
            self.OpportunisticPessimism = StringVar()
            self.OpportunisticPessimism.set("10")
            self.txtOpportunisticPessimism = Entry(self, textvariable=self.OpportunisticPessimism)
            self.txtOpportunisticPessimism.grid(row=7, column=2)
            self.NumberOfOpportunistic = StringVar()
            self.NumberOfOpportunistic.set("0")
            self.txtNumberOfOpportunistic = Entry(self, textvariable=self.NumberOfOpportunistic)
            self.txtNumberOfOpportunistic.grid(row=7, column=3)

        except:
            raise ReynoldsWindowCreateWidgetsError("_CreateWidgetsAgentsOpportunistic Failed")
            messagebox.showwarning("Internal Method Error", "_CreateWidgetsAgentsOpportunistic Failed")

    def _CreateWidgetsAgentsNeutral(self):
        """
            This intialises and displays the neutral agent's widgets
            Arguments:
            Specifics:
        """
        try:

            self.NeutralOptimism = StringVar()
            self.NeutralOptimism.set("10")
            self.txtNeutralOptimism = Entry(self, textvariable=self.NeutralOptimism)
            self.txtNeutralOptimism.grid(row=8, column=1)
            self.NeutralPessimism = StringVar()
            self.NeutralPessimism.set("10")
            self.txtNeutralPessimism = Entry(self, textvariable=self.NeutralPessimism)
            self.txtNeutralPessimism.grid(row=8, column=2)
            self.NumberOfNeutral = StringVar()
            self.NumberOfNeutral.set("0")
            self.txtNumberOfNeutral = Entry(self, textvariable=self.NumberOfNeutral)
            self.txtNumberOfNeutral.grid(row=8, column=3)

        #// Custom Class Error's first
        except:
            raise ReynoldsWindowCreateWidgetsError("_CreateWidgetsAgentsNeutral Failed")
            messagebox.showwarning("Internal Method Error", "_CreateWidgetsAgentsNeutral Failed")

    def _CloseWindow(self):
        """
            This intialises and displays the windows widgets
            Arguments:
            Specifics:
        """
        try:

            self.quit()


        #// Custom Class Error's first
        except:
            messagebox.showwarning("Internal Method Error", "_CloseWindow Failed")
            raise ReynoldsWindowButtonError("_CloseWindow Failed")

    def _CommenceExperiment(self):
        """
            Arguments:
            Specifics:
        """
        try:
            print "Commencing Experiment"
            NumRuns = eval(self.NumberOfRuns.get())
            OilDistribution = self.lboxOilDistributions.get(ACTIVE)
            ResultsFileName = self.ResultsFileName.get()
            self._CreateListOfAgents()
            print "Number of Runs: ", NumRuns, " Oil Distribution: ", OilDistribution, " Results Filename: ", ResultsFileName, " Agent Data: ", self.AgentsData
            CurrentExperiment = clReynoldsExperiment(NumRuns, OilDistribution, ResultsFileName, self.AgentsData)

        #// Custom Class Error's first
        except ReynoldsWindowMethodError as AnError:
            raise ReynoldsWindowMethodError(AnError)
        except:
            messagebox.showwarning("Internal Method Error", "_CommenceExperiment Failed")
            raise ReynoldsWindowButtonError("_CommenceExperiment Failed")

    def _CreateListOfAgents(self):
        """

            Arguments:
            Specifics:
        """
        try:
            self.AgentsData = []
            NumberOfOptimists, NumberOfPessimists, NumberOfStubborn, NumberOfOpportunists, NumberOfNeutrals = self._GetNumbersOfAgents()
            
            if NumberOfOptimists > 0: self._CreateListOfOptimisticAgents(NumberOfOptimists)
            if NumberOfPessimists > 0: self._CreateListOfPessimisticAgents(NumberOfPessimists)
            if NumberOfStubborn > 0: self._CreateListOfStubbornAgents(NumberOfStubborn)
            if NumberOfOpportunists > 0: self._CreateListOfOpportunisticAgents(NumberOfOpportunists)
            if NumberOfNeutrals > 0: self._CreateListOfNeutralAgents(NumberOfNeutrals)

        #// Custom Class Error's first
        except ReynoldsWindowMethodError as AnError:
            raise ReynoldsWindowMethodError(AnError)
        except:
            messagebox.showwarning("Internal Method Error", "_CreateListOfAgents Failed")
            raise ReynoldsWindowMethodError("_CreateListOfAgents Failed")

    def _GetNumbersOfAgents(self):
        """

            Arguments:
            Specifics:
        """
        try:
            NumberOfOptimists = eval(self.NumberOfOptimists.get())
            NumberOfPessimists = eval(self.NumberOfPessimists.get())
            NumberOfStubborn = eval(self.NumberOfStubborn.get())
            NumberOfOpportunists = eval(self.NumberOfOpportunistic.get())
            NumberOfNeutrals = eval(self.NumberOfNeutral.get())
            return NumberOfOptimists, NumberOfPessimists, NumberOfStubborn, NumberOfOpportunists, NumberOfNeutrals

        #// Custom Class Error's first
        except:
            messagebox.showwarning("Internal Method Error", "_GetNumbersOfAgents Failed")
            raise ReynoldsWindowMethodError("_GetNumbersOfAgents Failed")

    def _CreateListOfOptimisticAgents(self, NumberOfOptimists):
        """

            Arguments:
            Specifics:
        """
        try:
            OptimisticAgentData = []
            OptimistsOptimismLevel = eval(self.OptimisticOptimism.get())
            OptimistsPessimismLevel = eval(self.OptimisticPessimism.get())
            
            if NumberOfOptimists:
                OptimisticAgentData = [('Optimistic', OptimistsOptimismLevel, OptimistsPessimismLevel) for A in range(NumberOfOptimists)]
                self.AgentsData.extend(OptimisticAgentData)

        #// Custom Class Error's first
        except:
            messagebox.showwarning("Internal Method Error", "_CreateListOfOptimisticAgents Failed")
            raise ReynoldsWindowMethodError("_CreateListOfOptimisticAgents Failed")

    def _CreateListOfPessimisticAgents(self, NumberOfPessimists):
        """

            Arguments:
            Specifics:
        """
        try:
            PessimisticAgentData = []
            PessimistsOptimismLevel = eval(self.PessimisticOptimism.get())
            PessimistsPessimismLevel = eval(self.PessimisticPessimism.get())
            
            if NumberOfPessimists:
                PessimisticAgentData = [('Pessimistic', PessimistsOptimismLevel, PessimistsPessimismLevel) for A in range(NumberOfPessimists)]
                self.AgentsData.extend(PessimisticAgentData)

        #// Custom Class Error's first
        except:
            messagebox.showwarning("Internal Method Error", "_CreateListOfPessimisticAgents Failed")
            raise ReynoldsWindowMethodError("_CreateListOfPessimisticAgents Failed")

    def _CreateListOfStubbornAgents(self, NumberOfStubborn):
        """

            Arguments:
            Specifics:
        """
        try:
            StubbornAgentData = []
            StubbornOptimismLevel = eval(self.StubbornOptimism.get())
            StubbornPessimismLevel = eval(self.StubbornPessimism.get())
            
            if NumberOfStubborn:
                StubbornAgentData = [('Stubborn', StubbornOptimismLevel, StubbornPessimismLevel) for A in range(NumberOfStubborn)]
                self.AgentsData.extend(StubbornAgentData)

        #// Custom Class Error's first
        except:
            messagebox.showwarning("Internal Method Error", "_CreateListOfStubbornAgents Failed")
            raise ReynoldsWindowMethodError("_CreateListOfStubbornAgents Failed")

    def _CreateListOfOpportunisticAgents(self, NumberOfOpportunists):
        """

            Arguments:
            Specifics:
        """
        try:
            OpportunisticAgentData = []
            OpportunisticOptimismLevel = eval(self.OpportunisticOptimism.get())
            OpportunisticPessimismLevel = eval(self.OpportunisticPessimism.get())
            
            if NumberOfOpportunists:
                OpportunisticAgentData = [('Opportunistic', OpportunisticOptimismLevel, OpportunisticPessimismLevel) for A in range(NumberOfOpportunists)]
                self.AgentsData.extend(OpportunisticAgentData)

        #// Custom Class Error's first
        except:
            messagebox.showwarning("Internal Method Error", "_CreateListOfOpportunisticAgents Failed")
            raise ReynoldsWindowMethodError("_CreateListOfOpportunisticAgents Failed")

    def _CreateListOfNeutralAgents(self, NumberOfNeutrals):
        """

            Arguments:
            Specifics:
        """
        try:
            NeutralAgentData = []
            NeutralOptimismLevel = eval(self.NeutralOptimism.get())
            NeutralPessimismLevel = eval(self.NeutralPessimism.get())
            
            if NumberOfNeutrals:
                NeutralAgentData = [('Neutral', NeutralOptimismLevel, NeutralPessimismLevel) for A in range(NumberOfNeutrals)]
                self.AgentsData.extend(NeutralAgentData)

        #// Custom Class Error's first
        except:
            messagebox.showwarning("Internal Method Error", "_CreateListOfNeutralAgents Failed")
            raise ReynoldsWindowMethodError("_CreateListOfNeutralAgents Failed")

#// ---------------------------------------------------------------------------
#// ------------------------------------- Exception Class Definitions ---------
#// ---------------------------------------------------------------------------

class ReynoldsWindowError(Exception): pass
class ReynoldsWindowCreateWidgetsError(Exception): pass
class ReynoldsWindowButtonError(Exception): pass
class ReynoldsWindowMethodError(Exception): pass

