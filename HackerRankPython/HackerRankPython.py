import      sys

from        sherlockPairs.Solution      import  SherlockPairs
from        utils.strings.Strings       import  format              as      _fmt


    
def                                     doTest                      (input)                         :
    obj = SherlockPairs()
    obj.Solution(input)
     

# interactive
try:
    input=''
    done=False
    while (not done):
        line=raw_input()
        if (line == '\4'):                                                                          #   EOT (ctrl+D)
            break
        input+=line+"\n"
    doTest ( input )

except ValueError as e:
    print _fmt("Error: {}",e.message)

