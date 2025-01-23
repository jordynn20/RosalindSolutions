#code to identify the GC content of a string (decimal)
string.count('G' and 'C')/len(string)

#code to identify the GC content of a string (percent)
(string.count('G' and 'C')/len(string))*100

#function for this
def GC_content(string): 
  return string.count('G' and 'C')/len(string)

