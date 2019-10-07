from pprint import pprint
import requests,json 

def assetProcess(server,token,headers,query):
    user_name, id_selection = searchUsers(server,token,headers,query)
    print(id_selection)
    asset_list = getUserAssets(server,token,headers,id_selection)
    return user_name, asset_list

def searchUsers(server,token,headers,query):
    api_endpoint = "users"
    querystring = {"search":query,"offset":"0","sort":"id","order":"asc"}
    response = requests.request("GET", server + api_endpoint, headers=headers, params=querystring)
    data = json.loads(response.text)
    search_results = []
    print('')
   
    for entry in data['rows']:
#        search_results.append([{"id":entry['id']}, {"name":entry['name']}, {"email":entry['email']}, {"asset count":entry['assets_count']}])
        search_results.append({str(entry['id']):[str(entry['name']), str(entry['email']), str(entry['assets_count'])]})
    if len(search_results) == 0:
        print("No results.")
        quit()
    elif len(search_results) == 1:
        print(str(len(search_results)) + " result:")
    else:
        print(str(len(search_results)) + " results:")
    
    print('')

    for result in search_results:
        for k,v in result.items():
            print("id: " + k)
            print("name: " + v[0])
            if v[1] == '':
                print("email: n/a")
            else:
                print("email: " + v[1])
            print("assets: " + v[2])
            print('')

    while True:
        selection = input("Please input the ID of the user you want assets for: ")
        for result in search_results:
            for k,v in result.items():
                if selection == k:
                    return v[0], k
        else:
            print("Invalid selection.")
            continue

def getUserAssets(server,token,headers,id_selection):
    assigned_assets = []
    selected_assets = []
    api_endpoint = "users/%s/assets" % id_selection
    response = requests.request("GET", server + api_endpoint, headers=headers)
    data = json.loads(response.text)
    # pprint(data)
    for entry in data['rows']:
        assigned_assets.append({str(entry['asset_tag']): [str(entry['category']['name']), str(entry['serial']), str(entry['manufacturer']['name']), str(entry['model']['name'])]})
    
    if len(assigned_assets) == 1:
        print('')
        print(str(len(assigned_assets)) + " asset found:\n")
    else:
        print('')
        print(str(len(assigned_assets)) + " assets found:\n")
    
    for asset in assigned_assets:
        for k,v in asset.items():
            print("Device type: %s" % v[0])
            print("Device manufacturer: %s" % v[2])
            print("Device model: %s" % v[3])
            print("Device serial: %s" % v[1])
            print("Device asset tag: %s" % k)
            print('')
            while True:
                selection = input("Add device to Asset Acceptance Form? (y/n)\n> ")
                if selection == "y":
                    selected_assets.append(asset)
                    print('')
                    break
                elif selection == "n":
                    print('')
                    break
                else:
                    print("Please make a valid selection.\n")
                    continue
    
    return selected_assets

#assetProcess()
