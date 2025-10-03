import pandas as pd
import matplotlib.pyplot as ragul
rk = pd.read_csv('gender_submission.csv')
print(rk)
Total_Pass = rk["Survived"].value_counts()
total = len(rk)
non_survivors = Total_Pass[0]  # Assuming 0 = non-survivors
survivors = Total_Pass[1]
print(f"Total survivors:{survivors}")
print(f"Total Non survivors:{non_survivors}")
per = (survivors / total) * 100
print(f"Percentage of Survivors is: {per:.2f}%")
per = (non_survivors / total) * 100
print(f"Percentage of Non-Survivors is: {per:.2f}%")
Total_Pass.plot(kind='bar', color=["yellow", "black"])
ragul.xlabel("Status (0 = Non Survived, 1 = survived)")
ragul.ylabel("Number of People")
ragul.title("Survived vs Non Survived")
ragul.xticks(rotation=0)
ragul.show()