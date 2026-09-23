"""
Teams Bulk Member Adder
Entry point for the application.
"""

import sys
import os

# Add package root to sys.path if running as script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.app import TeamsMemberAdderApp

def main():
    app = TeamsMemberAdderApp()
    app.mainloop()

if __name__ == "__main__":
    main()
