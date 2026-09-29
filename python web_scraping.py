import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)

if response.status_code == 200:
    print("Website connected successfully!")

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    # Find all books
    for book in soup.select("article.product_pod"):

        title = book.h3.a["title"]

        price = book.select_one(".price_color").text.strip()

        availability = book.select_one(".availability").text.strip()

        rating = book.select_one("p.star-rating")["class"][1]

        books.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })

    # Create DataFrame
    df = pd.DataFrame(books)

    # Display dataset
    print("\nScraped Data:\n")
    print(df.to_string(index=False))

    # Save dataset
    df.to_csv("books_dataset.csv", index=False)

    print("\nDataset saved successfully as books_dataset.csv")

else:
    print("Unable to connect to website.")
    print("Status code:", response.status_code)
