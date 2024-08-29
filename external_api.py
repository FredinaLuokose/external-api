import xmlrpc.client
url = 'http://localhost:8064'
db = 'test1'
username = 'admin'
password = 'admin'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

#authentication
uid = common.authenticate(db, username, password, {})
if uid:
   print("authentication success")
else:
    print("authentication failed")
    
    #search method
    
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
partners =models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]],{'limit':5})

print("......>",partners)

#read method

partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners],{'fields': ['name', 'country_id', 'name']})
print("......>",partner_rec)

#search count method
partners_count =models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
print("......>",partners_count)


#searchread method
record = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'id']})
print("......>",record)

# Create a new record
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner"}])
print(id)

# Update the record
models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {'name': "Newer partner"}])
write_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [[id], ['display_name']])
print(write_rec)

# Delete the record
models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
del_rec = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['id', '=', id]]])
print(del_rec)

