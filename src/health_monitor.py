def monitor_health(data):
    print("Analyzing plant/soil health...")
    avg_ph = data['ph'].mean()
    print(f"Average soil pH: {avg_ph}")
