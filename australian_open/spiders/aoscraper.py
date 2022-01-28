import  australian_open.xplist as xp
import scrapy
from australian_open.items import AustralianOpenItem
from scrapy.loader import ItemLoader

class AoscraperSpider(scrapy.Spider):
    name = 'aoscraper'
    # allowed_domains = ['tennis.com/tournaments/sr-tournament-2565-australian-open/']
    page_start = 'https://www.tennis.com/tournaments/sr-tournament-2565-australian-open/library/sr-tournament-2567/{}'
    year_start = 2022
    tournament_code = page_start.split('/')[4].split('-')[2]
    start_urls = [
            page_start.format(year_start)
            ]

    def parse(self, response):
        game_details_list = response.xpath(xp.game_details_list_xpath)
        for game in game_details_list:
            l = ItemLoader(item=AustralianOpenItem(), selector=game)
            l.add_xpath('tournament_phase', xp.tournament_phase_xpath)
            l.add_value('calendar_year', self.year_start)
            l.add_value('tournament', self.tournament_code)

            # Access the detail page to scrape game information
            game_href= game.xpath(xp.game_href_xpath).get()
            yield response.follow(url=game_href, meta={'item' : l.load_item()},
                    callback=self.parse_game, dont_filter=True)

        # Iteration over the years
        if self.year_start > 2015:
            self.year_start -= 1
            yield response.follow(url=self.page_start.format(self.year_start),
                    callback=self.parse, dont_filter=True)

    # Scrape the stats from the detail page
    def parse_game(self, response):
        l = ItemLoader(item=response.meta['item'], selector=response)

        #Parse player1 data
        l.add_xpath('player1_name', xp.player1_name_xpath)
        l.add_xpath('player1_surname', xp.player1_surname_xpath)
        l.add_xpath('player1_country', xp.player1_country_xpath)
        l.add_xpath('player1_seed', xp.player1_seed_xpath)
        l.add_xpath('player1_total_sets', xp.player1_total_sets_xpath)
        l.add_xpath('p1_total_points_won', xp.p1_total_points_won_xpath)
        l.add_xpath('p1_total_games_won', xp.p1_total_games_won_xpath)
        l.add_xpath('p1_max_points_row', xp.p1_max_points_row_xpath)
        l.add_xpath('p1_max_games_row', xp.p1_max_games_row_xpath)
        l.add_xpath('p1_tiebreaks_won', xp.p1_tiebreaks_won_xpath)
        l.add_xpath('p1_servgames_won', xp.p1_servgames_won_xpath)
        l.add_xpath('p1_aces', xp.p1_aces_xpath)
        l.add_xpath('p1_doublefaults', xp.p1_doublefaults_xpath)
        l.add_xpath('p1_1stserve_success', xp.p1_1stserve_success_xpath)
        l.add_xpath('p1_1stserve_pwon', xp.p1_1stserve_pwon_xpath)
        l.add_xpath('p1_2ndserve_pwon', xp.p1_2ndserve_pwon_xpath)
        l.add_xpath('p1_breakpoints_won', xp.p1_breakpoints_won_xpath)

        p1_sets_list = response.xpath(xp.p1_sets_list_xpath).getall()
        try:
            l.add_value('player1_1st_set', p1_sets_list[0])
        except:
            l.add_value('player1_1st_set', '0')
        try:
            l.add_value('player1_2nd_set', p1_sets_list[1])
        except:
            l.add_value('player1_2nd_set', '0')
        try:
            l.add_value('player1_3rd_set', p1_sets_list[2])
        except:
            l.add_value('player1_3rd_set', '0')
        try:
            l.add_value('player1_4th_set', p1_sets_list[3])
        except:
            l.add_value('player1_4th_set', '0')
        try:
            l.add_value('player1_5th_set', p1_sets_list[4])
        except:
            l.add_value('player1_5th_set', '0')

        #Parse player2 data
        l.add_xpath('player2_name', xp.player2_name_xpath)
        l.add_xpath('player2_surname', xp.player2_surname_xpath)
        l.add_xpath('player2_country', xp.player2_country_xpath)
        l.add_xpath('player2_seed', xp.player2_seed_xpath)
        l.add_xpath('player2_total_sets', xp.player2_total_sets_xpath)
        l.add_xpath('p2_total_points_won', xp.p2_total_points_won_xpath)
        l.add_xpath('p2_total_games_won', xp.p2_total_games_won_xpath)
        l.add_xpath('p2_max_points_row', xp.p2_max_points_row_xpath)
        l.add_xpath('p2_max_games_row', xp.p2_max_games_row_xpath)
        l.add_xpath('p2_tiebreaks_won', xp.p2_tiebreaks_won_xpath)
        l.add_xpath('p2_servgames_won', xp.p2_servgames_won_xpath)
        l.add_xpath('p2_aces', xp.p2_aces_xpath)
        l.add_xpath('p2_doublefaults', xp.p2_doublefaults_xpath)
        l.add_xpath('p2_1stserve_success', xp.p2_1stserve_success_xpath)
        l.add_xpath('p2_1stserve_pwon', xp.p2_1stserve_pwon_xpath)
        l.add_xpath('p2_2ndserve_pwon', xp.p2_2ndserve_pwon_xpath)
        l.add_xpath('p2_breakpoints_won', xp.p2_breakpoints_won_xpath)

        p2_sets_list = response.xpath(xp.p2_sets_list_xpath).getall()
        try:
            l.add_value('player2_1st_set', p2_sets_list[0])
        except:
            l.add_value('player2_1st_set', '0')
        try:
            l.add_value('player2_2nd_set', p2_sets_list[1])
        except:
            l.add_value('player2_2nd_set', '0')
        try:
            l.add_value('player2_3rd_set', p2_sets_list[2])
        except:
            l.add_value('player2_3rd_set', '0')
        try:
            l.add_value('player2_4th_set', p2_sets_list[3])
        except:
            l.add_value('player2_4th_set', '0')
        try:
            l.add_value('player2_5th_set', p2_sets_list[4])
        except:
            l.add_value('player2_5th_set', '0')
        yield l.load_item()

