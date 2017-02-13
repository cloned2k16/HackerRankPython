import      sys

from        sherlockPairs.Solution              import  SherlockPairs
from        sherlockPermutations.Solution       import  SherlockPermutations

from        utils.strings.Strings               import  format              as      _fmt


# interactive mode
def                                     testInteractive             (clssName)                      :
    try:
        input=''
        done=False
        while (not done):
            line=raw_input()
            if (line == '\4'):                                                                      #   EOT (ctrl+D)
                break
            input+=line+"\n"
        obj = SherlockPairs()
        obj.Solution(input)
    except ValueError as e:
        print _fmt("Error: {}",e)


def                                     doTests                     (clss, tstList)                 :
    try:
        obj = clss()
        for tn in tstList:
            NN          = str(tn).zfill(2)
            cName       = obj.getName()
            fName       = cName+'/input'+NN+'.txt'
            fIn         = open(fName)
            data=fIn.read()
            fIn.close()
            old_stdout  = sys.stdout
            rName       = 'res'+NN+'.txt'
            fRes        = open(rName, 'w')
            sys.stdout  = fRes
            obj.Solution(data)
            sys.stdout  = old_stdout
            fRes.close()
            fOut        = open(cName+'/output'+NN+'.txt')
            fRes        = open(rName)
            res         = fRes.read()
            out         = fOut.read()
            resLines    = res.splitlines()
            outLines    = out.splitlines()
            resLen      = len(resLines)
            outLen      = len(outLines)
            if (resLen != outLen):
                print (_fmt('ERROR out lines: {} res lines: {}',outLen,resLen)) 
            haveErrors=False
            for l in range(resLen):
                if (resLines[l] != outLines[l]):
                    print (_fmt('ERROR at line: {}',l+1))
                    haveErrors=True
            if (not haveErrors):
                print (_fmt('{} :: test [{}] SUCCESS!',cName,NN));


    except Exception as e: 
        print _fmt("Error: {}",e)


def                                     testBoundle                 ()                              :
    doTests ( SherlockPairs             , [ 0 , 3]);    
    doTests ( SherlockPermutations      , [ 0 ]);


testBoundle()