i = input()
while (i != 0):
        c = raw_input()
        coordsI = c.split(" ")
  
  
        for a in xrange(i):
            d = raw_input()
            coordsF = d.split(" ")
             
            if( float(coordsF[0]) == float(coordsI[0]) or float(coordsF[1]) == float(coordsI[1]) ):
                print "divisa"
                continue  
            if ( int(coordsF[0]) > int(coordsI[0]) ):
                if ( int(coordsF[1]) > int(coordsI[1]) ):
                    print "NE"
                else:
                    print "SE"
            else:
                if (int(coordsF[1]) > int(coordsI[1]) ):
                    print "NO"
                else:
                    print "SO"
      
        i = input()
        i = int(i)
