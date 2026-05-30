#!/bin/bash

# Fun Linux commands to lighten up your terminal sessions

# Make it rain
yes "Make it rain!" | head -n 10

# Create a file with a funny name
touch "this_is_not_a_virus.sh"

# Display a random Chuck Norris joke
curl -s http://api.icndb.com/jokes/random | jq '.value.joke'

# Play Star Wars in ASCII
telnet towel.blinkenlights.nl
