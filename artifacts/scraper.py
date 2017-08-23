from pprint import pprint
import trello
from trello import board
from trello import TrelloClient

client = TrelloClient(
        api_key='4de1136340ee5e550eb5431d70bf7f9d',
        api_secret='cb15abc1ced2884742c39892084f7bc6cfcb10d21e0cf79eb6810219f29f99fa',
        token='e7901b564e7f67d2f2c549f7c814b01c925a6dc94bf5b357b317bf88cd07fda5',
        token_secret='')

team = client.get_organization('erochefoucauld')
boards = team.get_boards(0)
board = boards[2]

lists = board.all_lists();

for l in lists:
    print(l.list_cards())
