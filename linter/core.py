# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re

class BranchLinter:
    # Convention: type/description or type/issue-description
    # Types: feature, bugfix, hotfix, release, chore, docs, test
    # Regex: ^(feature|bugfix|hotfix|release|chore|docs|test)/[a-z0-9-]+$
    
    STANDARD_PATTERN = re.compile(r'^(feature|bugfix|hotfix|release|chore|docs|test)\/[a-z0-9-]+$')

    @staticmethod
    def validate(branch_name):
        branch_name = branch_name.strip()
        
        # Always allow main, master, develop
        if branch_name in ['main', 'master', 'develop', 'staging']:
            return True, None
            
        if BranchLinter.STANDARD_PATTERN.match(branch_name):
            return True, None
            
        return False, "Branch name does not follow convention 'type/description' (e.g. feature/add-login)"

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
