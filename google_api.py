from googleapiclient.discovery import build

def getImageUrl(api_key, cse_key, search_word, page_limit):

    service = build("customsearch", "v1", developerKey=api_key, cache_discovery=False)
    page_limit = page_limit
    startIndex = 1
    response = []

    img_list = []

    for nPage in range(0, page_limit):
        print("Reading page number:", nPage + 1)

        try:
            response.append(
                service.cse()
                .list(
                    q=search_word,  # Search words
                    cx=cse_key,  # custom search engine key
                    lr="lang_ja",  # Search language
                    num=10,  # Number of images obtained by one request (Max 10)
                    start=startIndex,
                    searchType="image",  # search for images
                )
                .execute()
            )

            startIndex = (
                response[nPage].get("queries").get("nextPage")[0].get("startIndex")
            )

        except Exception as e:
            print(e)

    for one_res in range(len(response)):
        if len(response[one_res]["items"]) > 0:
            for i in range(len(response[one_res]["items"])):
                img_list.append(response[one_res]["items"][i]["link"])

    return img_list

if __name__ == "__main__":
    # -------------- Parameter and Path Settings -------------- #
    API_KEY = "AIzaSyBRgWX8460TpSK0OszHvVLtmM34S2fDRwo"
    CUSTOM_SEARCH_ENGINE = "b382b10e1bccd60e1"

    page_limit = 1
    search_word = "あんぱんまん"

    img_list = getImageUrl(API_KEY, CUSTOM_SEARCH_ENGINE, search_word, page_limit)
