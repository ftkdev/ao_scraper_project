import scrapy
from scrapy.item import Field


class AustralianOpenItem(scrapy.Item):
    tournament = Field()
    tournament_phase = Field()
    calendar_year = Field()
    player1_name = Field()
    player1_surname = Field()
    player1_country = Field()
    player1_seed = Field()
    player1_1st_set = Field()
    player1_2st_set = Field()
    player1_3rd_set = Field()
    player1_4th_set = Field()
    player1_5th_set = Field()
    p1_total_points_won = Field()
    p1_total_games_won = Field()
    p1_max_points_row = Field()
    p1_max_games_row = Field()
    p1_tiebreaks_won = Field()
    p1_servgames_won = Field()
    p1_aces = Field()
    p1_doublefaults = Field()
    p1_1stserve_success = Field()
    p1_1stserve_pwon = Field()
    p1_2ndserve_pwon = Field()
    p1_breakpoints_won = Field()
