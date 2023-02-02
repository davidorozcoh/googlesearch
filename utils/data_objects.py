dataElements = {

    # dataElement googletest

    "homepage": {
        "url": "https://www.google.com.co/",
        "field": {
            "name": "q",
            "xpath": "//*[contains(@id,'search')]",
            "selector": "name",
        },
        "search": {
            "class_name": "search",
            "xpath": "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[6]/center/input[1]",
            "selector": "xpath",
        },
        "result": {
            "class_name": "result",
            "xpath": "//*[@id=tads]/div/div/div/div/div[1]/a/div[1]/span",
            "selector": "xpath"
        },
        "link_text": {
            "class_name": "link_result",
            "xpath": "//article[@id='post-4889']/div/div/div/div/div/div/div/div/p",
            "selector": "xpath"
        }

    }
}
