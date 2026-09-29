import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

# Check whether website is accessible
if response.status_code == 200:

    print("Website connected successfully!")
    print("Starting web scraping...\n")

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # List to store book information
    books = []

    # Find all book containers
    book_items = soup.find_all("article", class_="product_pod")

    # Extract information
    for book in book_items:

        # Book title
        title = book.h3.a["title"]

        # Price
        price = book.find("p", class_="price_color").text.strip()

        # Rating
        rating = book.find("p", class_="star-rating")["class"][1]

        # Availability
        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        # Product URL
        product_link = book.h3.a["href"]

        # Store information
        books.append({
            "Book Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product URL": product_link
        })

    # Convert data into DataFrame
    df = pd.DataFrame(books)

    # Display dataset
    print("Books Scraped Successfully!\n")
    print(df)

    # Save dataset to CSV
    df.to_csv("books_dataset.csv", index=False)

    print("\n--------------------------------")
    print("Scraping completed successfully!")
    print("Dataset saved as: books_dataset.csv")
    print("--------------------------------")

else:
    print("Failed to connect to the website.")
    print("Status Code:", response.status_code)