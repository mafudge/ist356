import requests 
import requests_cache as rq

texts = [
    "I love IST356. It is the best course I've ever taken.", 
    "I hate the New York Giants.",
    "I love IST356. It is the best course I've ever taken.", 
    "I don't like the New York Giants."
]

cache = rq.clear_cache('sentiment.pkl')
apikey = "ea044c96950db6cc0fab7ae1"
headers = { 'x-api-key': apikey }
url = "https://cent.ischool-iot.net/api/azure/sentiment"
for text in texts:
    if text in cache:
        results = cache[text]
        from_cache = "CACHED"
    else:
        data = { 'text': text }
        response = requests.post(url, headers=headers, data=data)
        results = response.json()
        cache[text] = results
        rq.save_cache(cache, 'sentiment.pkl')
        from_cache = "NOT CACHED"

    sentiment = results['results']['documents'][0]['sentiment']
    print(text, sentiment, from_cache)