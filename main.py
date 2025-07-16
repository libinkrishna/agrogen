from src import data_loader, crop_recommender, health_monitor

def main():
    print("AgroGen starting...")

    data = data_loader.load_data("data/raw/sample.csv")
    crop_recommender.recommend_crop(data)
    health_monitor.monitor_health(data)

if __name__ == "__main__":
    main()
