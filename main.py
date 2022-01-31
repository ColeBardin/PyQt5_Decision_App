import sys
from PyQtResWindow import *

# Main body function
def main():
    # Crate PyQt Application
    app = QApplication(sys.argv)
    # Set style to be 'fusion'
    app.setStyle("fusion")
    # Create main window of PyQtLayout class
    window = PyQtResWindow()
    # Display window
    window.show()
    # Close window when python program is closed
    sys.exit(app.exec_())

if __name__ == "__main__":
    # Call upon main function
    main()