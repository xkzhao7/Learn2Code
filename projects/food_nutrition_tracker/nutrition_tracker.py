import pandas as pd
from utils.string_manipulation import str_to_float
import datetime

class NutritionTracker:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.last_log_date = datetime.date.today()
        self._create_nutrition_goals()
        self.today_nutrition_goals = self.nutrition_goals
    def get_nutrition_goals(self):
        for key in self.nutrition_goals:
            print(key + ": " + str(self.nutrition_goals[key]))
    def get_today_nutrition_goals(self):
        self._reset_if_new_day()
        finished_goals = []
        for key in self.today_nutrition_goals:
            if isinstance(self.today_nutrition_goals[key], (int, float)):
                if self.today_nutrition_goals[key] < 0:
                    finished_goals.append(key)
                else:
                    print(key + ": " + str(self.today_nutrition_goals[key]))
            else:
                if str_to_float(self.today_nutrition_goals[key]) < 0:
                    finished_goals.append(key)
                else:
                    print(key + ": " + self.today_nutrition_goals[key])
        x = ", ".join(finished_goals)
        print("Finished requirements: " + x)
        print("Keep up the good work!")
    def eat(self, food, weight):
        self._reset_if_new_day()
        log_file = self.name + "_food_log.txt"
        self.food_nutrition_df = pd.read_csv("./projects/food_nutrition_tracker/food_nutrition_df.csv", comment = "#")
        self.food_nutrition_df.set_index(self.food_nutrition_df.columns[0], inplace=True)
        for column_name, value in self.food_nutrition_df.loc[food].items():
            if isinstance(self.today_nutrition_goals[column_name], (int, float)):
                self.today_nutrition_goals[column_name] = self.today_nutrition_goals[column_name] - (value * weight / 100)
            else:
                self.today_nutrition_goals[column_name] = str_to_float(self.today_nutrition_goals[column_name]) - (value * weight / 100)
    def _reset_if_new_day(self):
        if datetime.date.today() != self.last_log_date:
            self.today_nutrition_goals = self.nutrition_goals.copy()
            self.last_log_date = datetime.date.today()
    def _create_nutrition_goals(self):
        self.nutrition_goals = {}
        self.nutrition_goals_df = pd.read_csv("./projects/food_nutrition_tracker/nutrition_goals_df.csv", comment = "#")
        self.nutrition_goals_df.set_index(self.nutrition_goals_df.columns[0], inplace=True)
        if self.age < 4:
            category = "3"
        elif self.age < 9:
            category = f"{self.sex}4"
        elif self.age < 14:
            category = f"{self.sex}9"
        elif self.age < 19:
            category = f"{self.sex}14"
        elif self.age < 31:
            category = f"{self.sex}19"
        elif self.age < 51:
            category = f"{self.sex}31"
        else:
            category = f"{sex}51"
        for row_name, value in self.nutrition_goals_df[category].items():
                self.nutrition_goals[row_name] = value
if __name__ == "__main__":
    feifei = NutritionTracker("feifei", "m", 4)
    feifei.get_nutrition_goals()

    print("")
    feifei.eat("apple", 150)
    feifei.eat("broccoli", 100)
    feifei.get_today_nutrition_goals()