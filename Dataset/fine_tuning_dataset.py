import pandas as pd

# Assuming your dataset is in a CSV file called 'wellbeing_data.csv'
# Load your dataset into a pandas DataFrame
df = pd.read_csv('wellbeing_synthetic_data.csv')

# Define the columns for each wellbeing category
physical_columns = ['Sleep_Hours', 'HeartRate_BPM', 'Exercise_Hours', 'DietQuality', 'CaloricIntake', 'Weight_kg', 'BodyFat_Percentage']
mental_columns = ['Focus', 'Fatigue', 'Productivity', 'Motivation', 'Energy']
emotional_columns = ['Mood', 'PositiveEmotions', 'FacialExpressionIntensity']
spiritual_columns = ['Purpose', 'LifeGoals', 'LifeSatisfaction']

# Step 1: Calculate the raw scores for each category for every person
df['Score_Physical'] = df[physical_columns].sum(axis=1)
df['Score_Mental'] = df[mental_columns].sum(axis=1)
df['Score_Emotional'] = df[emotional_columns].sum(axis=1)
df['Score_Spiritual'] = df[spiritual_columns].sum(axis=1)

# Step 2: Calculate the total score for each person (sum of all categories)
df['Total_Score'] = df[['Score_Physical', 'Score_Mental', 'Score_Emotional', 'Score_Spiritual']].sum(axis=1)

# Step 3: Calculate the percentage for each category
df['Percentage_Physical'] = (df['Score_Physical'] / df['Total_Score']) * 100
df['Percentage_Mental'] = (df['Score_Mental'] / df['Total_Score']) * 100
df['Percentage_Emotional'] = (df['Score_Emotional'] / df['Total_Score']) * 100
df['Percentage_Spiritual'] = (df['Score_Spiritual'] / df['Total_Score']) * 100

# Step 4: Optionally, drop the raw score columns to leave just the percentages
df = df.drop(columns=['Score_Physical', 'Score_Mental', 'Score_Emotional', 'Score_Spiritual', 'Total_Score'])

# Step 5: Display the first few rows of the new DataFrame
print(df.head())

# Step 6: Save the updated dataframe to a new CSV file
df.to_csv('wellbeing_percentages.csv', index=False)



import json

# Load the wellbeing data (assuming it's in a CSV called 'wellbeing_percentages.csv')
df = pd.read_csv('wellbeing_percentages.csv')

# Prepare the fine-tuning data in prompt-completion format
fine_tuning_data = []

for index, row in df.iterrows():
    # Prepare the prompt (person's data)
    prompt = f"Person {row['PersonID']}'s data: Sleep Hours = {row['Sleep_Hours']}, Heart Rate = {row['HeartRate_BPM']}, Exercise Hours = {row['Exercise_Hours']}, " \
             f"Diet Quality = {row['DietQuality']}, Caloric Intake = {row['CaloricIntake']}, Weight = {row['Weight_kg']}, Body Fat Percentage = {row['BodyFat_Percentage']}, " \
             f"Focus = {row['Focus']}, Fatigue = {row['Fatigue']}, Productivity = {row['Productivity']}, Motivation = {row['Motivation']}, " \
             f"Energy = {row['Energy']}, Mood = {row['Mood']}, Positive Emotions = {row['PositiveEmotions']}, Facial Expression Intensity = {row['FacialExpressionIntensity']}, " \
             f"Purpose = {row['Purpose']}, Life Goals = {row['LifeGoals']}, Life Satisfaction = {row['LifeSatisfaction']}"

    # Prepare the completion (percentage breakdown)
    completion = f"{{'physical_body': {row['Percentage_Physical']}, 'mental_mind': {row['Percentage_Mental']}, 'emotional_heart': {row['Percentage_Emotional']}, 'spiritual_soul': {row['Percentage_Spiritual']}}}"

    fine_tuning_data.append({"prompt": prompt, "completion": completion})

# Save the fine-tuning data in JSONL format
with open("fine_tuning_data.jsonl", "w") as f:
    for item in fine_tuning_data:
        f.write(json.dumps(item) + "\n")

print("Fine-tuning data saved in 'fine_tuning_data.jsonl'")