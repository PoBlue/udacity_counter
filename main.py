# -*- coding:utf-8 -*-
"""
main center
"""
from review_counter import ReviewCounter
from froum_counter import FroumCounter
from base_class import StoreData
from clint.arguments import Args

args = Args()


class CmdInterface():
    """
    class that handle command
    """

    def __init__(self):
        self.token = ''
        self.forum_url = ''
        self.chrome_path = ''
        self.review_counter = None
        self.forum_counter = None
        self.data_file = 'data.pkl'
        self.store_data = StoreData(self.data_file)
        self.load_data()
        self.init_counter()

    def init_counter(self):
        """
        init counter
        """
        if self.token != '':
            self.review_counter = ReviewCounter(self.token)
        if self.forum_url != '' and self.chrome_path != '':
            self.forum_counter = FroumCounter(self.forum_url, self.chrome_path)
        else:
            print("set token/forum_url/chrome_path")

    def save_data(self):
        """
        save data to data file
        """
        d = {"token": self.token,
             "forum_url": self.forum_url,
             "chrome_path": self.chrome_path}
        self.store_data.save_data(d)

    def load_data(self):
        """
        load data from data file
        """
        default_data = {"token": self.token,
                        "forum_url": self.forum_url,
                        "chrome_path": self.chrome_path}
        data = self.store_data.load_data(default_data)
        if data is not None:
            self.token = data["token"]
            self.forum_url = data["forum_url"]
            self.chrome_path = data["chrome_path"]

    def cli_handler(self):
        """
        command line handler
        """
        flag_args = args.grouped
        print(flag_args)
        cmd = flag_args['_']
        if '-token' in flag_args:
            self.token = flag_args['-token'][0]
        if '-forum_url' in flag_args:
            self.forum_url = flag_args['-forum_url'][0]
        if '-chrome_path' in flag_args:
            self.chrome_path = flag_args['-chrome_path'][0]
        if len(cmd) > 0:
            command = cmd[0]
            if command == 'froum':
                num_of_days = 0
                if '-n' in flag_args:
                    num_of_days = int(flag_args['-n'][0])
                    print(self.forum_counter.get_money_day(num_of_days))
                if '-m' in flag_args:
                    print(self.forum_counter.get_money_month())
                if '-set' in flag_args:
                    print('add data succesful')
                    count = int(flag_args['-set'][0])
                    year = int(flag_args['-set'][1])
                    month = int(flag_args['-set'][2])
                    day = int(flag_args['-set'][3])
                    self.forum_counter.add_count_day(count, year, month, day)
            if command == 'review':
                if '-n' in flag_args:
                    num_of_days = int(flag_args['-n'][0])
                    print(self.review_counter.get_money_today(num_of_days))
                if '-m' in flag_args:
                    num_of_monthes = int(flag_args['-m'][0])
                    print(self.review_counter.get_money_month(num_of_monthes))
            if command == 'help':
                print("""
                    [froum] to show froum money
                        [-m] get moneny this month
                        [-n] get money days ago
                        [-set count year month day] set count on day month in year
                    [review] to show review money
                        [-m number] from number monthes ago
                        [-n number] from number days ago]
                    [show] to show the setting
                    [-chrome_path] to set chrome path
                    [-forum_url] to set froum url
                    [-token] to set review token
                """)
            if command == 'show':
                print("token: {0}\nforum_url: {1}\nchrome_path: {2}"
                      .format(self.token,
                              self.forum_url,
                              self.chrome_path))
        self.save_data()


cmd_interface = CmdInterface()
cmd_interface.cli_handler()
