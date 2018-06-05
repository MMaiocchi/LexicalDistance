import editdistance
import re
fileOut = open("map_results.gexf", "w", encoding="utf-8")
fileIn = open("YourInputFile.txt", "r", encoding="utf-8")

print ("This script generates a network map of lexemes, conceived as nodes linked to one another according to their similarity.")
print ("For best results, it is advisable to restrict the domain to homogenous semantic classes, such as for instance personal names.")
print ("Input file must contain the list of lexemes to be analysed, one lexeme per line.")

var = fileIn.readlines()
fileIn.close()

####NETWORK MAP##############################################################
fileOut.write ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
fileOut.write ("<gexf xmlns=\"http://www.gexf.net/1.1draft\"\n")
fileOut.write ("    xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\n")
fileOut.write ("    xsi:schemaLocation=\"http://www.gexf.net/1.1draft http://www.gexf.net/1.1draft/gexf.xsd\"    version=\"1.1\">\n")
fileOut.write ("    <graph mode=\"static\" defaultedgetype=\"undirected\">\n")
fileOut.write ("<nodes>\n")

myid = 0
for word in var:
    #print (word)
    word = word.rstrip()
    word.replace("<", "‹") # < and > are reserved symbols in XML as well as in GEFX(output)
    word.replace (">", "›")
    
    fileOut.write('\t\t<node id=\"' + str(myid) + '\" label=\"' + word + '\" />"\n')
    
    word = re.sub('\d+', '', word) #remove numbers
    word = re.sub('[DINGIR=-]', '', word)
    
    myid = myid + 1


fileOut.write ("</nodes>\n")
fileOut.write  ("<edges>\n")


for n in range (myid - 1):
    #print ('n is ' + str (n))
    for m in range(n + 1, myid - 1):
        #print ("\t m is" + str(m))
        dist = editdistance.eval(var[n], var[m])
        edgeWeight = 4 - dist
        if dist < 3:
            var[n] = var[n].rstrip()
            var[m] = var[m].rstrip()
            fileOut.write ('\t<edge id=\"' + var[n] + '_' + var[m] + '\" source=\"' + str(n) + '\" target=\"' + str(m) +'\" weight=\"' + str(edgeWeight) + '\"/>"\n')

fileOut.write ("</edges>\n");
fileOut.write ("</graph>\n");
fileOut.write ("</gexf>\n");
fileOut.close()

print ("\nDone, check current directory for map_results.gexf\n\nCode by Massimo Maiocchi 2014.")



#print ("editdistance banana vs bahama", editdistance.eval('banana', 'bahama'))