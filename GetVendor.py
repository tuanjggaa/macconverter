from mac_vendor_lookup import MacLookup

with open('vendor.txt','w') as f:
    f.close()

vendorlist = list()
with open('Mac2.txt','r') as file:
   mylist = file.read().splitlines()
   for x in mylist:
        p=(MacLookup().lookup(x))+'\n'
        vendorlist.append(p)
with open('vendor.txt','a')  as f:
    for x in vendorlist:
        f.write(x)
