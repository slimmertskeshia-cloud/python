# Importing the hotdog module
import hotdog  

# Calling the make_hotdog function from the hotdog module
# Making a 16-size hotdog with mustard
hotdog.make_hotdog(16, 'mustard')  

# Making a 12-size hotdog with russian sauce, onions, and extra cheese
hotdog.make_hotdog(12, 'russian sauce', 'onions', 'extra cheese')  

#####################################################################################
# Importing only the function we want to use

from hotdog import make_hotdog  

# Calling the function directly
make_hotdog(16, 'mustard')  
make_hotdog(12, 'russian sauce', 'onions', 'extra cheese')  

#############################################################################################
# Giving the function an alias

from hotdog import make_hotdog as mh  

mh(16, 'mustard')
mh(12, 'russian sauce', 'onions', 'extra cheese')

##############################################################################################
# Giving the module an alias

import hotdog as h  

h.make_hotdog(16, 'mustard')
h.make_hotdog(12, 'russian sauce', 'onions', 'extra cheese')

#############################################################################################
# Importing functions from multiple modules

from hotdog import make_hotdog
from makeHotdog import make_hotdog2

make_hotdog(16, 'mustard')
make_hotdog(12, 'russian sauce', 'onions', 'extra cheese')

make_hotdog2(18, 'cheese')
make_hotdog2(15, 'russian sauce', 'onions', 'extra cheese')