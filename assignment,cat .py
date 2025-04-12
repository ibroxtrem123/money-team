import requests

class CatFactFetcher:
    def __init__(self):
        self.api_url = 'https://catfact.ninja/fact'
        self.shown_facts = []  # To keep track of shown facts

    def get_cat_fact(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            fact = data.get("fact")

            if not fact:
                return "Error: No fact found in the response."

            return fact

        except requests.RequestException as e:
            return f"Error fetching cat fact: {e}"
        except ValueError as e:
            return f"Error parsing response: {e}"

class CatFactApp:
    def __init__(self):
        self.fetcher = CatFactFetcher()

    def run(self):
        print("Welcome to the cat fact Generator.....")
        while True:
            command = input("\n Do you want to know a fact about cats? (yes/no): ").strip().lower()
            if command == "no":
                print("Goodbye!")
                break
            elif command == "yes":
                fact = self.fetcher.get_cat_fact()
                print(f"Cat fact: {fact}")
            else:
                print("Please  type 'yes' to get facts or 'no' to exit")

if __name__ == "__main__":
    app = CatFactApp()
    app.run()
