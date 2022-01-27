import scrapy
from ..items import AustralianOpenItem
from scrapy.loader import ItemLoader

class AoscraperSpider(scrapy.Spider):
    name = 'aoscraper'
    allowed_domains = ['tennis.com/tournaments/sr-tournament-2565-australian-open/']
    start_urls = ['http://tennis.com/tournaments/sr-tournament-2565-australian-open//']

    def parse(self, response):
        game_details_list = response.xpath("//div[@class='rounded']/div[@class=\
                'mb-3 recipe-card recipe-card-with-hover']")

        for game in game_details_list:
            l = ItemLoader(item=AustralianOpenItem(), selector=game)
            l.add_xpath('tournament_phase', "")
            l.add_value('calendar_year',"")

            # Access the detail page to scrape game information
            game_href= response.xpath("").get()
            yield response.follow(url=game_href, meta={'item' : l.load_item()},
                    callback=self.parse_game, dont_filter=True)


    # Scrape the ingredients from the detail page
    def parse_game(self, response):
        l = ItemLoader(item=response.meta['item'], selector=response)

        #Parse player1 data
        l.add_xpath('player1_name',"xpathss")
        l.add_xpath('player1_surname',"xpathss")
        l.add_xpath('player1_country',"xpathss")
        l.add_xpath('player1_seed',"xpathss")
        l.add_xpath('player1_1st_set',"xpathss")
        l.add_xpath('player1_2st_set',"xpathss")
        l.add_xpath('player1_3rd_set',"xpathss")
        l.add_xpath('player1_4th_set',"xpathss")
        l.add_xpath('player1_5th_set',"xpathss")
        l.add_xpath('p1_total_points_won',"xpathss")
        l.add_xpath('p1_total_games_won',"xpathss")
        l.add_xpath('p1_max_points_row',"xpathss")
        l.add_xpath('p1_max_games_row',"xpathss")
        l.add_xpath('p1_tiebreaks_won',"xpathss")
        l.add_xpath('p1_servgames_won',"xpathss")
        l.add_xpath('p1_aces',"xpathss")
        l.add_xpath('p1_doublefaults',"xpathss")
        l.add_xpath('p1_1stserve_success',"xpathss")
        l.add_xpath('p1_1stserve_pwon',"xpathss")
        l.add_xpath('p1_2ndserve_pwon',"xpathss")
        l.add_xpath('p1_breakpoints_won',"xpathss")
        yield l.load_item()

