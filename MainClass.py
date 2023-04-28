import random


class RandomGen():
    def __init__(self, min_l, max_l, pop, list):
        self.input_list = list
        self.alf_dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        self.dict_gen_words = {}
        self.dict_2 = {}
        self.dict_3 = {}
        self.sort_dict = {}

        self.min_l = min_l
        self.max_l = max_l
        self.pop = pop

    def FitScore_Func(self, dict):
        for i in dict:
            score = 0.0
            d_2 = []
            d_3 = []

            l = len(i)
            n_kol = 2
            n = 0
            for i2 in range(0, l - 1):
                if n + n_kol == l + 1:
                    break
                n_gramm = i[n:n + n_kol]
                d_2.append(n_gramm)
                n += 1

            l = len(i)
            n_kol = 3
            n = 0
            for i2 in range(0, l - 1):
                if n + n_kol == l + 1:
                    break
                n_gramm = i[n:n + n_kol]
                d_3.append(n_gramm)
                n += 1

            for i2 in d_2:
                if i2 in self.dict_2:
                    score += self.dict_2[i2] / 10

            for i2 in d_3:
                if i2 in self.dict_3:
                    score += self.dict_3[i2] / 10

            dict[i] = score

    def Start(self):
        # Fit 2
        for i in self.input_list:
            l = len(i)
            n_kol = 2
            n = 0
            for i2 in range(0, l - 1):
                if n + n_kol == l + 1:
                    break
                n_gramm = i[n:n + n_kol]
                if n_gramm in self.dict_2:
                    self.dict_2[n_gramm] += 1
                else:
                    self.dict_2[n_gramm] = 1
                n += 1

        # Fit 3
        for i in self.input_list:
            l = len(i)
            n_kol = 3
            n = 0
            for i2 in range(0, l - 1):
                if n + n_kol == l + 1:
                    break
                n_gramm = i[n:n + n_kol]
                if n_gramm in self.dict_3:
                    self.dict_3[n_gramm] += 1
                else:
                    self.dict_3[n_gramm] = 1
                n += 1

        # Random Word's
        for i in range(self.pop):
            word = ''
            for i2 in range(random.randint(int(self.min_l), int(self.max_l))):
                word += random.choice(self.alf_dict)
            self.dict_gen_words[word] = 0

        # Scores
        self.FitScore_Func(self.dict_gen_words)

        # Sorted
        self.sort_dict = dict(sorted(self.dict_gen_words.items(), reverse=True, key=lambda item: item[1]))

    def Population(self):
        for i in range(1):
            # 100 words
            for k, i in enumerate(self.sort_dict, start=1):
                self.dict_gen_words[i] = self.sort_dict[i]
                if k == 100:
                    break
            dict_100_word = list(self.dict_gen_words)
            dict_gen_words = {}
            for i in range(2000):
                outpurt_word = ''
                first_word = random.choice(dict_100_word)
                second_word = random.choice(dict_100_word)

                l = random.randint(self.min_l, self.max_l)
                first_split = random.randint(1, l - 2)
                second_split = l - first_split

                dict_gen_words[first_word[:first_split] + second_word[-second_split:]] = 0
            self.FitScore_Func(dict_gen_words)
            sort_dict = dict(sorted(dict_gen_words.items(), reverse=True, key=lambda item: item[1]))
            return sort_dict