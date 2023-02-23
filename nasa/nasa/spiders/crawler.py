from pathlib import Path
import os

import json
import scrapy
from bs4 import BeautifulSoup


image_folder = "D:/Data/nasa/images"
meta_folder = "D:/Data/nasa/meta"


# TODO change timeout to longer than 180 seconds, change download warn size and max size to be ~2 gb
class NasaImageSpider(scrapy.Spider):
    name = "nasa"
    start_urls = [
        # filtered by "observations" and by "fine" quality & minimum resolution "400x300"
        f"https://esahubble.org/images/{file.stem}/"
        for file in Path(image_folder).glob("*.tif")
        # f"https://esahubble.org/images/heic0918b/"
    ]
    custom_settings = {
        "DOWNLOAD_TIMEOUT": 3000,
        "DOWNLOAD_MAXSIZE": 0,
        "DOWNLOAD_WARNSIZE": 0,
    }

    def clean(self, items):
        lines = []
        for item in items:
            soup = BeautifulSoup(item, features="lxml")
            # remove non-breaking spaces
            text = soup.get_text().replace("\xa0", " ").strip()
            if text.startswith('"') and text.endswith('"'):
                return text[1:-1]
            if text:
                lines.append(text)
        cleaned_text = " ".join(lines)
        return cleaned_text

    def parse(self, response):
        title = response.xpath(
            '//div[@class="col-md-9 left-column"]/h1/text()'
        ).extract()
        title = self.clean(title)
        description = response.xpath('//div[@class="col-md-9 left-column"]/p').extract()
        description = self.clean(description)
        credits = response.xpath('//div[@class="credit"]/p').extract()
        credits = self.clean(credits)
        meta_names = response.xpath('//td[@class="title"]/text()').extract()
        meta_names = [name[:-1].strip() for name in meta_names]
        meta_values = response.xpath('//td[not(@class="title")]').extract()

        meta = {}
        for name, value in zip(meta_names, meta_values):
            meta[name] = self.clean([value])
        data = {
            "id": meta["Id"],
            "title": title,
            "description": description,
            "credits": credits,
            "url": response.url,
            "meta": meta,
        }
        with open(os.path.join(meta_folder, f"{data['id']}.json"), "w") as f:
            json.dump(data, f)
