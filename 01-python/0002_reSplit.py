regex_pattern = r"[.,]"	# Do not delete 'r'.
# use re.split() to seperate all of the , and . symbols in the input
import re
print("\n".join(re.split(regex_pattern, input())))

