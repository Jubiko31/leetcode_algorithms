# ===========Tenth Line================
#
# ? Given a text file file.txt, print just the 10th line of the file.
# TODO Your script should output the tenth line, which is:
# ```Line 10```
#

#!/bin/bash
OUTPUT=$(sed "10q;d" file.txt)
if [[ -n "$OUTPUT" ]]
then
    echo "$OUTPUT"
else
    echo "Line not found."
fi

# Runtime: 10% | Memory: 69.70%
