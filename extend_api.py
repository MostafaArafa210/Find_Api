import re
args = ['extender, callbacks, helpers, toolFlag, messageIsRequest, messageInfo, macroItems']

keys = {'apikey', 'api_key', 'APIKEY', "API_KEY", '@yopmail', 'database', 'DATABASE',
        'DATABASES', 'databases', 'databaseUrl', 'accessToken', 'accessTokens', 'Bearer', 'bearer'}
for key in keys:
    p = key + ':'+'\d\w'
if not messageIsRequest:
    response = messageInfo.getResponse()
    matches = re.findall(p, response)
    for match in matches:
        print(match)
