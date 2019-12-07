import json
import codecs


class JsonCreator:
    def __init__(self, ratio):
        self.ratio = ratio

        path = '/home/ivan/rosbank_hackaton/rosbankhack/django_projects/ros_bank_17/mobile_bank/json_for_offers/json_for_offers/'
        self.low_coaf_json = json.load(codecs.open(path + 'low_coaf_offers.json', 'r', 'utf-8-sig'))
        self.medium_coaf_json = json.load(codecs.open(path + 'medium_coaf_offers.json', 'r', 'utf-8-sig'))
        self.high_coaf_json = json.load(codecs.open(path + 'high_coaf_offers.json', 'r', 'utf-8-sig'))

        self.correct_json = self.get_offers()

    def get_offers(self):
        offers = None
        if self.ratio < 1:
            offers = self.low_coaf_json
        elif self.ratio < 3:
            offers = self.medium_coaf_json
        elif self.ratio < 6:
            offers = self.high_coaf_json

        return offers
