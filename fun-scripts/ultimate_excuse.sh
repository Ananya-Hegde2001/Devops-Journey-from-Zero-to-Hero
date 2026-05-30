
#!/bin/bash

# Ultimate excuse generator

excuses=(
    "My dog ate my code."
    "I thought I was working on the main branch."
    "It worked on my machine."
    "I was abducted by aliens."
    "I was under the influence of caffeine."
)

# Pick a random excuse
RANDOM=$$$(date +%s)
echo ${excuses[$RANDOM % ${#excuses[@]}]}