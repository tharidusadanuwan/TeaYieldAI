from jobs.weather_scheduler import fetch_all_weather


if __name__ == "__main__":

    print("Starting scheduled weather update...")

    fetch_all_weather()

    print("Scheduled weather update finished.")