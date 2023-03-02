import requests

API_POST_URL = 'https://pastebin.com/api/api_post.php'
DEVELOPER_API_KEY = '43m_lX1w2zvBA4dC0vbYqa5BVd7O1ElA'

def main():
    post_new_paste('Whatever paste', 'a bunch of crap')

def post_new_paste(title, body_text, expiration='10M', listed=True):

    params = {
        'api_dev_key' : DEVELOPER_API_KEY,
        'api_option' : 'paste',
        'api_paste_code' : body_text,
        'api_paste_name' : title,
        'api_paste_expire_date' : expiration,
        'api_paste_private' : 0 if listed else 1
    }

    print("Posting new paste to PasteBin", end='')
    resp_msg = requests.post(API_POST_URL, data=params)

    if resp_msg.ok:
        print(' success')
        return resp_msg.text
    else:
        print('failure')
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        return None


if __name__=="__main__":
    main()