# Import necessary libraries
import numpy as np
import pandas as pd
import random

# Define age groups and their corresponding probabilities
# Source: Bangladesh Bureau of Statistics (2020) estimate of age distribution in Bangladesh
age_groups = ["Under 12 years", "12-17 years", "17-23 years", "23-27 years", "27 years and above"]
age_probabilities = [0.17, 0.23, 0.27, 0.20, 0.13]

# Define a function to generate a realistic age
def generate_realistic_age():
    return np.random.choice(age_groups, p=age_probabilities)

# Define a function to generate a realistic gender
# Source: Bangladesh Bureau of Statistics (2020) estimate of gender distribution in Bangladesh
def generate_realistic_gender():
    genders = ["Male", "Female", "Non-binary", "Third gender", "Prefer not to say"]
    probabilities = [0.51, 0.48, 0.01, 0.00, 0.00]  
    return np.random.choice(genders, p=probabilities)

# Define a function to generate a realistic occupation
def generate_realistic_occupation(age):
    if age in ["Under 12 years", "12-17 years"]:
        return "Student"
    elif age in ["17-23 years", "23-27 years"]:
        return np.random.choice(["Student", "Employed", "Unemployed", "Self-employed"], p=[0.7, 0.2, 0.05, 0.05])
    else:
        return np.random.choice(["Employed", "Unemployed", "Self-employed", "Other (please specify)"], p=[0.6, 0.2, 0.1, 0.1])

# Define a function to generate realistic device usage
def generate_realistic_device_usage(age):
    if age in ["Under 12 years", "12-17 years"]:
        return np.random.choice(["2-4 hours", "4-6 hours", "More than 6 hours"], p=[0.3, 0.4, 0.3])
    else:
        return np.random.choice(["Less than 2 hours", "2-4 hours", "4-6 hours", "More than 6 hours"], p=[0.1, 0.3, 0.4, 0.2])

# Define a function to generate realistic stress levels
def generate_realistic_stress_level(age):
    if age in ["Under 12 years", "12-17 years"]:
        return np.random.choice(["Never", "Rarely", "Sometimes"], p=[0.3, 0.4, 0.3])
    else:
        return np.random.choice(["Sometimes", "Often", "Always"], p=[0.4, 0.4, 0.2])

# Define a function to generate realistic sleep quality
def generate_realistic_sleep_quality(stress_level):
    if stress_level in ["Never", "Rarely"]:
        return np.random.choice(["Very good", "Good", "Average"], p=[0.6, 0.3, 0.1])
    elif stress_level in ["Sometimes", "Often"]:
        return np.random.choice(["Good", "Average", "Poor"], p=[0.4, 0.4, 0.2])
    else:
        return np.random.choice(["Average", "Poor", "Very poor"], p=[0.4, 0.3, 0.3])

# Define a function to generate realistic nutrition
def generate_realistic_nutrition(stress_level):
    if stress_level in ["Never", "Rarely"]:
        return np.random.choice(["Very Good", "Good", "Average"], p=[0.6, 0.3, 0.1])
    elif stress_level in ["Sometimes", "Often"]:
        return np.random.choice(["Good", "Average", "Poor"], p=[0.4, 0.4, 0.2])
    else:
        return np.random.choice(["Average", "Poor", "Very Poor"], p=[0.4, 0.3, 0.3])

# templates with sentence structures
templates = [
    "To improve mental health support for Gen Z, {action} in {place}.",
    "{action} can greatly benefit the mental health of Gen Z.",
    "One way to support Gen Z's mental health is by {action} and {additional_action}.",
    "It's essential to {action} for better mental health outcomes in Gen Z.",
    "Encouraging {action} among Gen Z can lead to {benefit}.",
    "{action} and {additional_action} are crucial for enhancing mental health support for Gen Z.",
    "Providing {resources} and {support} can significantly improve mental health for Gen Z.",
    "We should {action} to ensure Gen Z has access to {resources}.",
    "Integrating {action} into {place} can help in supporting Gen Z's mental health.",
    "Fostering {action} and {additional_action} can lead to {benefit}.",
    "It's important to {action} and {additional_action} to promote {benefit} for Gen Z.",
    "By {action}, we can {result} and {benefit}.",
    "Supporting Gen Z's mental health requires {action} and {additional_action}.",
    "{place} should prioritize {action} and {additional_action} for better mental health support.",
    "{resources} and {support} are vital for {place} to effectively support Gen Z's mental health.",
    "{action} can help bridge the gap in mental health support for Gen Z in {place}.",
    "Gen Z's mental health can greatly benefit from {action} and {additional_action} provided in {place}."
]

actions = [
    "increase mental health awareness",
    "provide accessible and affordable mental health services",
    "encourage open discussions about mental health",
    "implement mental health programs and workshops",
    "improve access to online mental health resources",
    "create safe spaces for Gen Z to share experiences",
    "increase funding for mental health research",
    "develop and promote mental health apps",
    "encourage regular mental health check-ups",
    "promote a healthy balance between digital device usage and offline activities",
    "offer anonymous counseling services",
    "integrate mental health education into the school curriculum",
    "provide mental health training for teachers and parents",
    "increase peer support programs",
    "encourage physical activities and hobbies",
    "promote mindfulness and relaxation techniques",
    "create more inclusive and diverse mental health resources",
    "reduce the stigma associated with seeking mental health help",
    "ensure mental health resources are culturally sensitive",
    "encourage employers to provide mental health support"
]

additional_actions = [
    "offer regular mental health workshops",
    "promote mental health awareness campaigns",
    "provide online and offline support groups",
    "develop mental health apps and tools",
    "create mental health hotlines",
    "offer mental health training programs",
    "increase accessibility to mental health services",
    "promote mental health through social media",
    "create supportive community environments",
    "encourage physical and recreational activities"
]

benefits = [
    "better mental health outcomes",
    "reduced stigma",
    "improved access to support",
    "enhanced well-being",
    "greater awareness and education",
    "stronger support networks",
    "more resilient mental health",
    "better coping mechanisms",
    "improved overall health",
    "greater emotional support"
]

resources = [
    "mental health resources",
    "supportive services",
    "counseling and therapy",
    "educational materials",
    "self-help tools",
    "professional help",
    "community support",
    "online resources",
    "mental health apps",
    "hotlines and support groups"
]

support = [
    "emotional support",
    "practical guidance",
    "peer support",
    "professional counseling",
    "online and offline resources",
    "access to mental health professionals",
    "support networks",
    "community programs",
    "educational workshops",
    "mental health hotlines"
]

places = [
    "schools",
    "workplaces",
    "communities",
    "online platforms",
    "universities",
    "public spaces",
    "healthcare settings",
    "social media",
    "educational institutions",
    "youth centers"
]

results = [
    "improve",
    "enhance",
    "promote",
    "foster",
    "support",
    "encourage"
]

# Function to generate diverse suggestions
def generate_diverse_suggestions():
    template = random.choice(templates)
    suggestion = template.format(
        action=random.choice(actions),
        additional_action=random.choice(additional_actions),
        benefit=random.choice(benefits),
        resources=random.choice(resources),
        support=random.choice(support),
        place=random.choice(places),
        result=random.choice(results)
    )
    return suggestion

# Define a function to simulate a realistic survey
def simulate_realistic_survey(survey):
    responses = {}
    age = generate_realistic_age()
    gender = generate_realistic_gender()
    occupation = generate_realistic_occupation(age)
    device_usage = generate_realistic_device_usage(age)
    stress_level = generate_realistic_stress_level(age)
    sleep_quality = generate_realistic_sleep_quality(stress_level)
    nutrition = generate_realistic_nutrition(stress_level)
    mental_health_resources = generate_realistic_mental_health_resources(age)
    depression_symptoms = generate_realistic_depression_symptoms(age)

    responses["Demographic Information"] = {
        "What is your age?": age,
        "What is your gender?": gender,
        "What is your current occupation?": occupation,
    }

    responses["Digital Device Usage"] = {
        "On average, how many hours per day do you spend on digital devices (smartphones, tablets, computers, etc.)?": device_usage,
        "Which activities do you spend most of your time on digital devices? (Select all that apply)": np.random.choice(
            [
                "Social media (Facebook, TikTok, X formally Twitter, Instagram)",
                "Gaming",
                "Studying/Educational purposes",
                "Work/Professional tasks",
                "Watching videos/Movies",
            ],
            size=np.random.randint(1, 4),
            replace=False,
        ).tolist(),
        "Do you use digital devices at night before sleep?": np.random.choice(["Never", "Rarely", "Sometimes", "Often", "Always"]),
        "Do you think the time you spend on your digital devices is good use of your time?": np.random.choice(["Yes", "No", "Sometimes"]),
    }

    responses["Mental Health and Well-Being"] = {
        "How often do you feel stressed?": stress_level,
        "Have you ever felt symptoms of depression (such as prolonged sadness, loss of interest, fatigue, etc.)?": depression_symptoms,
        "Do you feel comfortable discussing your mental health with friends or family?": np.random.choice(["Very comfortable", "Somewhat comfortable", "Neutral", "Somewhat uncomfortable", "Very uncomfortable"]),
        "Do you think your digital device usage affects your mental health?": np.random.choice(["Not at all", "A little", "Moderately", "A lot", "Significantly"]),
    }

    responses["Physical Activity and Sleep"] = {
        "How often do you engage in physical activities (exercise, sports, etc.)?": np.random.choice(["Never", "Rarely", "Sometimes", "Often", "Always"]),
        "How would you rate your sleep quality?": sleep_quality,
        "How would you rate your current nutrition and diet?": nutrition,
    }

    responses["Access to Mental Health Resources"] = {
        "Are you aware of the mental health resources available to you?": np.random.choice(["Yes", "No", "Not sure"]),
        "Have you ever sought professional help for mental health issues?": np.random.choice(["Yes", "No"]),
    }

    responses["Preferences for Mental Health Support"] = {
        "What is your preferred mode of receiving mental health support? (Select all that apply)": np.random.choice(
            [
                "In-person counseling",
                "Online therapy sessions",
                "Support groups",
                "AI-powered chatbots",
                "Self-help resources (books, articles, videos)",
                "Other (please specify)",
            ],
            size=np.random.randint(1, 3),
            replace=False,
        ).tolist(),
        "Would you be open to using an AI-powered chatbot for mental health support and managing digital device usage?": np.random.choice(["Yes", "No", "Maybe"]),
        "What features would you find most helpful in an AI-powered chatbot? (Select all that apply)": np.random.choice(
            [
                "Immediate emotional support",
                "Tips for managing digital device usage",
                "Resources for mental health (articles, videos, etc.)",
                "Daily check-ins/mood tracking",
                "Connection to professional help",
                "Other (please specify)",
            ],
            size=np.random.randint(1, 4),
            replace=False,
        ).tolist(),
        "Do you have any suggestions for improving mental health support for Gen Z? (Open-ended)": generate_diverse_suggestions(),
    }

    return responses

# Define a function to generate realistic mental health resources
def generate_realistic_mental_health_resources(age):
    if age in ["Under 12 years", "12-17 years"]:
        return np.random.choice(["No", "Not sure", "Yes"], p=[0.5, 0.3, 0.2])
    else:
        return np.random.choice(["Yes", "No", "Not sure"], p=[0.5, 0.3, 0.2])

# Define a function to generate realistic depression symptoms
def generate_realistic_depression_symptoms(age):
    if age in ["Under 12 years", "12-17 years"]:
        return np.random.choice(["No", "Sometimes", "Yes"], p=[0.6, 0.3, 0.1])
    else:
        return np.random.choice(["No", "Sometimes", "Yes"], p=[0.5, 0.3, 0.2])

# Simulate 4000 survey responses
responses = [simulate_realistic_survey({}) for _ in range(4000)]

# Flatten the responses into a single df
def flatten_responses(responses):
    flat_responses = []
    for response in responses:
        flat_response = {}
        for section, questions in response.items():
            for question, answer in questions.items():
                flat_response[f"{section} - {question}"] = answer
        flat_responses.append(flat_response)
    return pd.DataFrame(flat_responses)

# Save responses to CSV
df = flatten_responses(responses)
df.to_csv("survey_responses.csv", index=False)