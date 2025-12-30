# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os
import subprocess

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from linter.core import BranchLinter

def get_current_branch():
    try:
        # Use git cli to get current branch
        result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description="Git Branch Naming Convention Linter")
    parser.add_argument("branch", help="Branch name to check (optional, defaults to current git branch)", nargs='?')
    
    args = parser.parse_args()
    
    branch = args.branch
    if not branch:
        branch = get_current_branch()
        if not branch:
            print("Error: Could not detect current branch and no argument provided.")
            print("Usage: python run_linter.py [branch_name]")
            sys.exit(1)
            
    is_valid, error = BranchLinter.validate(branch)
    
    if is_valid:
        print(f"Branch '{branch}' is valid.")
        sys.exit(0)
    else:
        print(f"Error: Branch '{branch}' is invalid.")
        print(f"Reason: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
