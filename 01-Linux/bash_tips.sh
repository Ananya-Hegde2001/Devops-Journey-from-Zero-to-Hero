#!/bin/bash

# Bash tips and tricks

echo "Here are some useful bash tips and tricks!"

# 1. Using variables
name="Alice"
echo "Hello, $name!"    

# 2. Command substitution
today=$(date +%F)
echo "Today's date is $today"

# 3. Exit codes
ls /tmp
echo "Last command exit code: $?"

# 4. Pipes and redirection
ps aux | grep ssh
echo "DevOps notes" > notes.txt
echo "More notes" >> notes.txt

# 5. Simple loop
for file in /etc/*.conf; do
	echo "Found config: $file"
done

# 6. Function example
greet() {
	echo "Hello from Bash, $1!"
}

greet "DevOps engineer"

# 7. Safer script options for real automation
set -o errexit
set -o nounset
set -o pipefail

# 8. Cleanup handler pattern
cleanup() {
	echo "Cleaning up temporary files"
}

trap cleanup EXIT