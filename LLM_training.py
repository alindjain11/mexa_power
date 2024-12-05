# Load the fine-tuning data (your JSON file)
with open('fine_tuning_data.jsonl', 'r') as f:
    fine_tuning_data = [json.loads(line) for line in f]

# Iterate over the JSON data and use each prompt to generate a response
for entry in fine_tuning_data:
    prompt = entry['prompt']
    expected_completion = entry['completion']

    # Generate a response from Gemini using the prompt
    response = model.generate_content(prompt)

    # Print the output and compare with expected completion
    print(f"Input Prompt: {prompt}")
    print(f"Expected Completion: {expected_completion}")
    print(f"Generated Response: {response.text}")
    print("-" * 80)
    
    

    
    #Generating truly representative synthetic data requires sophisticated statistical modeling to capture correlations between variables and accurately reflect the distributions seen in real-world populations with sleep deprivation, burnout risk, and mental illness risk. The data below is a simplified example and should not be used for any clinical or research purposes. It aims to illustrate how such data might look, showing lower scores in relevant metrics. The values are illustrative and do not represent precise clinical thresholds.

#Individual	Physical Wellbeing Metrics (1-5 Scale)	Mental Wellbeing Metrics (1-5 Scale)	Emotional Wellbeing Metrics (1-5 Scale)	Spiritual Wellbeing Metrics (1-5 Scale)	Notes
1	RHR:4, HRV:2, BMI:3, Grip:3, Sleep:1, RR:4, Temp:3, PAL:2	ME:2, MF:1, WM:2, RT:3, CF:1, Stress:5, Aware:1, PS:2	ET:1, EI:4, Mood:1, ER:1, Reac:5, Resil:1, SC:2, SCp:1	Purpose:1, Insp:1, Connect:1, Grat:1, LS:1, Forg:2, MM:1, Mind:1	Severe sleep deprivation, high burnout, high anxiety risk
2	RHR:3, HRV:1, BMI:4, Grip:2, Sleep:2, RR:3, Temp:4, PAL:1	ME:1, MF:2, WM:1, RT:4, CF:2, Stress:4, Aware:2, PS:1	ET:2, EI:3, Mood:2, ER:2, Reac:4, Resil:2, SC:1, SCp:2	Purpose:2, Insp:2, Connect:2, Grat:2, LS:2, Forg:3, MM:2, Mind:2	Moderate sleep deprivation, high burnout, moderate depression risk
3	RHR:4, HRV:2, BMI:3, Grip:3, Sleep:1, RR:4, Temp:3, PAL:2	ME:2, MF:1, WM:2, RT:3, CF:1, Stress:5, Aware:1, PS:2	ET:1, EI:4, Mood:1, ER:1, Reac:5, Resil:1, SC:2, SCp:1	Purpose:1, Insp:1, Connect:1, Grat:1, LS:1, Forg:2, MM:1, Mind:1	Severe sleep deprivation, high burnout, high depression and anxiety risk
4	RHR:3, HRV:3, BMI:2, Grip:4, Sleep:2, RR:3, Temp:3, PAL:3	ME:3, MF:3, WM:3, RT:2, CF:3, Stress:3, Aware:3, PS:3	ET:3, EI:2, Mood:3, ER:3, Reac:3, Resil:3, SC:3, SCp:3	Purpose:3, Insp:3, Connect:3, Grat:3, LS:3, Forg:4, MM:3, Mind:3	Mild sleep deprivation, moderate burnout, low mental illness risk
5	RHR:5, HRV:1, BMI:5, Grip:1, Sleep:1, RR:5, Temp:2, PAL:1	ME:1, MF:1, WM:1, RT:5, CF:1, Stress:5, Aware:1, PS:1	ET:1, EI:5, Mood:1, ER:1, Reac:5, Resil:1, SC:1, SCp:1	Purpose:1, Insp:1, Connect:1, Grat:1, LS:1, Forg:1, MM:1, Mind:1	Severe sleep deprivation, high burnout, high risk for both depression and anxiety
Key:

RHR: Resting Heart Rate
HRV: Heart Rate Variability
BMI: Body Mass Index
Grip: Grip Strength
Sleep: Sleep Quality
RR: Respiratory Rate
Temp: Body Temperature
PAL: Physical Activity Level
ME: Mental Energy
MF: Mental Focus
WM: Working Memory Capacity
RT: Reaction Time
CF: Cognitive Flexibility
Stress: Stress Levels
Aware: Awareness/Mindfulness
PS: Problem-Solving Ability
ET: Emotion Type
EI: Emotion Intensity
Mood: Mood
ER: Emotional Regulation
Reac: Emotional Reactivity
Resil: Resilience
SC: Social Connectedness
SCp: Self-Compassion
Purpose: Purpose
Insp: Inspiration
Connect: Connection to Something Greater
Grat: Gratitude
LS: Life Satisfaction
Forg: Forgiveness
MM: Meaning-Making
Mind: Mindfulness

#This is a highly simplified example. Real-world data would be far more complex, with more nuanced relationships between variables and a broader range of scores. This example only illustrates the general trend of lower scores across multiple wellbeing dimensions in individuals at risk. Always consult with qualified healthcare professionals for accurate assessments and diagnoses.



    
