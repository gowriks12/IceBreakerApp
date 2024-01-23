import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    Manually scrape information from LinkedIn Profile
    :param linkedin_profile_url:
    :return: data
    """
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    # api_endpoint = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    # header_dic = {"Authorization": f'Bearer {os.environ.get("sPPSRlfhpzRK3y5lTSl38w")}'}
    # header_dic = {"Authorization": "Bearer " + "sPPSRlfhpzRK3y5lTSl38w"}
    #
    # response = requests.get(
    #     api_endpoint,
    #     params={"linkedin_profile_url": linkedin_profile_url},
    #     headers=header_dic,
    # )
    gist_response = requests.get(
        "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    )
    data = gist_response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
    # pass
