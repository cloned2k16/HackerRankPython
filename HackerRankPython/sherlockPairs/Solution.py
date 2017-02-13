from  SolutionBase import SolutionBase

class                                   SherlockPairs               (SolutionBase)                  :

    """just an HackerRank Solution"""

    def                                 getPairs                    (th, a)                         :
        sum = 0
        sz  = len(a)
        i =1
        while (i < sz):
            c   = 1
            while (i < sz and a[i] == a[i-1]):
                c+=1
                i+=1
            sum += (c * (c - 1))
            i+=1
        return sum

    def                                 Solution                    (th, input)                     :
        lines = input.splitlines()
        nT=int(lines[0])
        for tn in range(nT):
            ln=tn*2+1
            N=int(lines[ln])
            A=[int(x) for x in lines[ln+1].split(' ')]
            A=sorted(A)
            r=th.getPairs(A)
            print r

