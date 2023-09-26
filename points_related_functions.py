class Deck:
    def check_points(self):
        final_points = 0
        self.players_points = []
        for players_deck in self.players_cards_list:
            for card in players_deck:
                if card[0] == 'Wild' or card[0] == '+4':
                    final_points+=50
                elif card[0] in ('+2','Skip','Reverse'):
                    final_points+=20
                elif card[0] in ('0','1','2','3','4','5','6','7','8','9'):
                    final_points+= int(card[0])
            self.players_points.append(final_points)
            final_points = 0
        return self.players_points

    def order_of_players(self):
        lowest = min(self.players_points)
        highest = max(self.players_points)
        print(lowest)
        print(highest)
        list_of_players=[1,2,3,4]
        print(self.players_points)
        removed =[]
        for i in range(4):
            if self.players_points[i] == lowest:
                self.winner_name = self.player_name_list[i]
                print(self.winner_name)
                list_of_players.remove(i+1)
            if self.players_points[i] == highest:
                self.fourth = self.player_name_list[i]
                print(f"fourth is {self.fourth}")
                if self.players_points[i] not in removed:
                    list_of_players.remove(i+1)
                removed.append(highest)

        c1 = list_of_players[0]
        d1 = list_of_players[1]
        if self.players_points[c1-1]<self.players_points[d1-1]:
            self.third = self.player_name_list[d1-1]
            self.second = self.player_name_list[c1-1]
        else:
            self.third = self.player_name_list[c1-1]
            self.second = self.player_name_list[d1-1]
        self.orders = []
        self.orders.append(self.winner_name)
        self.orders.append(self.second)
        self.orders.append(self.third)
        self.orders.append(self.fourth)
        return self.orders

    def scoreboard(self):
        self.final_player_points = sorted(self.players_points)
        for i in range(4):
            self.scoreboard_dic[self.orders[i]] = self.final_player_points[i]
        return self.scoreboard_dic