import configparser
import snipeapi
import pdf_maker

# Import configuration file with secrets
config = configparser.ConfigParser()
config.read('config.ini')

'''
SnipeIT API information
'''
server = "https://inventory.intinc.com/api/v1/"
token = config['snipeit']['api_key']

headers = {
            'authorization': "Bearer " + token,
            'accept': "application/json",
            'content-type': "application/json"
}

query = input("User to search for: ")
user_name, selected_assets = snipeapi.assetProcess(server, token, headers, query)
pdf_maker.create_pdf(user_name, selected_assets)