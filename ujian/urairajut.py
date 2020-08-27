def string_splosion(str):
      s='';
  for x in range (len(str)): #menggunakan len untuk stringnya (menggunakan fungsi loop)
    for y in range (x): #pada range x
      s = s +str[y]; #setiap kata akan selalu bertambah sesuai dengan str yang di tuju
    s =s + str[x];
  return s;

#print(string_splosion('Code'));
#print(string_splosion('python'));
print(string_splosion('purwadhika'));

