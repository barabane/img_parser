def photo_handler(photo):
    max_size = {'width': 0}

    for size in photo['photo']['sizes']:
        if max_size['width'] < size['width']:
            max_size = size
    return max_size['url']
