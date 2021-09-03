import json

yazi={"Staj yeri":"Bursa Teknik Universitesi"}

with open("kisi.json","w") as f:

    json.dump(yazi,f)

