"""
    ReynoldsSpade.py - This is the application main file that provides Access
                       to the Reynolds oil exploration game.
"""

#// --------------------------------------------------------------------------
#// ------------------------------------- Modules/Packages to be imported ----
#// --------------------------------------------------------------------------
from Tkinter import *
import tkMessageBox as messagebox

#// --------------------------------------------------------------------------
#// ------------------------------------- Class Modules to be imported -------
#// --------------------------------------------------------------------------

#// --------------------------------------------------------------------------
#// ------------------------------------- Form Modules to be AgentDataimported --------
#// --------------------------------------------------------------------------
from ReynoldsWindow import frmApplicationWindow

#// ---------------------------------------------------------------------------
#// ------------------------------------- Class Definitions -------------------
#// ---------------------------------------------------------------------------


#// ------------------------------------------------------------------------------
#// ------------------------------------- Main Body ------------------------------
#// ------------------------------------------------------------------------------

def main():
    try:

        #// Create an instance of the Application class (thought of as a window) called App
        GUIsession = Tk()
        instApp = frmApplicationWindow(GUIsession)
        instApp.setTitle("Reynold's SPADE")

        instApp.mainloop()
    except:
        exc_type, exc_value = sys.exc_info()[:2]
        strErrorMessage = exc_type.__name__ + ": " + str(exc_value)
        messagebox.showwarning("Application Error", strErrorMessage)
        GUIsession.destroy()

if __name__ == "__main__":
    main()
