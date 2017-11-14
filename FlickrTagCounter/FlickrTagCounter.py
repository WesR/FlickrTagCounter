import json, requests

'''
    An example of fetching data from flickrs api
    and then grabbing the number of images with 
    the tag specified
'''


key = ''
rest_url = 'https://api.flickr.com/services/rest/'

def image_count(page):
    return page['photos']['total']

def get_page(tags, page=1, per_page = 100):
    #Max per page = 500
    params = {'api_key': key,
              'tags' : tags,
              'media': 'photos',
              'page': page,
              'per_page' : per_page,
              'content_type': '1', #We only want pixs
              'sort': 'relevance',
              'method': 'flickr.photos.search',
              'format': 'json'}

    r = requests.get(rest_url, params).text[14:-1]#We have to strip off some stuff
    return json.loads(r)#We are returning a dict

def main():
    tag = 'cyberpunk'

    imageCount = image_count(get_page(tag))

    print("Images with tag " + tag + ":" + imageCount)


if __name__ == "__main__":
    main()