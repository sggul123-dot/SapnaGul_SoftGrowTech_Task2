class StockPortfolioTracker:
    def __init__(self):
        # Hardcoded stock prices
        self.stock_prices = {
            "AAPL": 180,
            "TSLA": 250,
            "GOOG": 2700,
            "MSFT": 300
        }
        self.total_investment = 0

    def run(self):
        print("Stock Portfolio Tracker")
        print("Available Stocks:", ", ".join(self.stock_prices.keys()))
        
        while True:
            stock_name = input("Enter stock name (or type 'done' to finish): ").upper()
            
            if stock_name == "DONE":
                break

            if stock_name in self.stock_prices:
                quantity = int(input("Enter quantity: "))
                investment = self.stock_prices[stock_name] * quantity
                self.total_investment += investment
                print("Added:", stock_name, "| Investment:", investment)
            else:
                print("Stock not available.")

        print("\nTotal Investment Value:", self.total_investment)

        # Optional: Save result to a text file
        with open("portfolio_summary.txt", "w") as file:
            file.write("Total Investment Value: " + str(self.total_investment))


if __name__ == "__main__":
    tracker = StockPortfolioTracker()
    tracker.run()