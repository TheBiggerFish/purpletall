import requests,json

#print(json.loads(requests.get('http://purpletall.cs.longwood.edu:5000/login?user=TheBiggerFish').text))
#print(requests.get('http://purpletall.cs.longwood.edu:5000/1/add?name={Bug1}&desc={This%20bug%20is%20in%20controller}&time={2019-05-1}&bug={true}').text)
#print(requests.get('http://purpletall.cs.longwood.edu:5000/login?user={TheBiggerFish}').text)
#print(requests.get('http://purpletall.cs.longwood.edu:5000/projlist').text)
#print(requests.get('http://purpletall.cs.longwood.edu:5000/2/addcol?name={TEST2}').text)
#print(requests.get('http://purpletall.cs.longwood.edu:5000/2/delcol?name={TEST2}').text)
#print(requests.get('http://purpletall.cs.longwood.edu:5000/git').text)
#print(requests.get('http://purpletall.cs.longwood.edu:5000/2/rename?id=5&name={TESTING}').text)
print(requests.get('http://purpletall.cs.longwood.edu:5000/ping?user=2&rcvr={haddockcl}&msg={This%20is%20a%20ping}').text)
#obj = json.loads(json_string)
#print(obj)
#print(obj['metadata']['stages']['1'])
#print(obj['stages']['0'][0]['name'])
#obj[stages][which stage][which task in stage][which item in task]
