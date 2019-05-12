# Import Custom-made modules, and Python modules
import sys
class_path = "C:/Users/Nick Kane/Dropbox/Work/Projects/Personal Projects/Fantasy Stats/Classes" # File path holding Upload CMS program
sys.path.insert(0, class_path)

from Employee import Employee


# Program
joe = Employee("Joe", 10000)
joe.displayEmployee()