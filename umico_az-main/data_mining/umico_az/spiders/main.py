import re

import scrapy


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["umico.az"]
    start_urls = ["https://umico.az/mega-discounts"]

    def parse(self, response):
        for page_number in range(1, 2374 + 1):
            page_url = f"https://umico.az/mega-discounts?page={page_number}"
            yield scrapy.Request(url=page_url, callback=self.parse_page)

    def parse_page(self, response):

        products = response.css('div.MPProduct-Content')
        for product in products:
            url = product.css('div.MPProduct-Content a::attr(href)').get()
            title = product.css('span.MPTitle::text').get()
            seller = product.css("span.MPProductItem-Seller span:nth-child(2)::text").get()
            discount_percentage = ''.join(
                filter(str.isdigit, product.css('div.MPProductItem-Discount::text').get()))
            discounted_price = product.css(
                'span.MPPrice-Discounted-Price span[data-info="item-desc-price-new"]::text').get()
            discounted_price = discounted_price.replace('₼', '').replace(' ', '').strip()
            real_price = product.css(
                'span.MPPrice-Discounted-Price span[data-info="item-desc-price-old"]::text').get()
            real_price = real_price.replace('₼', '').replace(' ', '').strip()
            monthly_payment = product.css('div.MPInstallment span::text').get()
            if monthly_payment is not None:
                monthly_payment = monthly_payment.strip()

                # Use regex to extract the amount and duration
                match = re.match(r'([\d.]+) ₼ x (\d+) ay', monthly_payment)
                if match:
                    monthly_payment_amount = match.group(1)
                    loan_duration = match.group(2)
                else:
                    monthly_payment_amount = None
                    loan_duration = None
            else:
                monthly_payment_amount = None
                loan_duration = None

            yield {
                'url': f'www.umico.az{url}',
                'title': title,
                'seller': seller,
                'discount_percentage': discount_percentage,
                'discounted_price': discounted_price,
                'real_price': real_price,
                'monthly_payment_amount': monthly_payment_amount,
                'loan_duration': loan_duration,
            }
