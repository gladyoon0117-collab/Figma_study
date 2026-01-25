import requests
def search_music(artist_name):
    url = f"https://itunes.apple.com/search?term={artist_name}&entity=song&limit=3"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        
        print(f"\n[호텔 시스템] 고객님 맞춤의 '{artist_name}' 데이터를 불러왔습니다.")
        print("="*50)
        
        for song in results:
            track_name = song.get('trackName')     
            album_name = song.get('collectionName')
            image_url = song.get('artworkUrl100') 
            
            print(f"곡명: {track_name}")
            print(f"앨범: {album_name}")
            print(f"이미지: {image_url}")
            print("-" * 50)
    else:
        print("API 통신 에러: 데이터를 불러올 수 없습니다.")
search_music("xdinary heroes")
