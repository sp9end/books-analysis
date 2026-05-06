import csv
import os
from collections import Counter
import statistics

# ============================================================
# BOOKS COLLECTION ANALYSIS
# Author: Barbara
# Description: Analysis of a personal book collection
#              using only Python built-in modules
# ============================================================

DATA_FILE = "data/books.csv"

# ============================================================
# 1. LOAD DATA
# ============================================================

def load_books(filepath):
    """Load books from a CSV file and return a list of dicts."""
    books = []
    try:
        with open(filepath, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append({
                    "title": row["title"],
                    "author": row["author"],
                    "year": int(row["year"]),
                    "pages": int(row["pages"]),
                    "rating": int(row["rating"])
                })
    except FileNotFoundError:
        print(f"Error: file '{filepath}' not found!")
        return []
    return books

books = load_books(DATA_FILE)
print(f"Loaded {len(books)} books.")

# ============================================================
# 2. BASIC STATISTICS
# ============================================================

def basic_stats(books):
    """Calculate basic statistics for the book collection."""
    ratings = [b["rating"] for b in books]
    pages = [b["pages"] for b in books]

    print("\n--- Basic Statistics ---")
    print(f"Total books:        {len(books)}")
    print(f"Average rating:     {statistics.mean(ratings):.2f}")
    print(f"Median rating:      {statistics.median(ratings):.2f}")
    print(f"Rating std dev:     {statistics.stdev(ratings):.2f}")
    print(f"Highest rating:     {max(ratings)}")
    print(f"Lowest rating:      {min(ratings)}")
    print(f"Average pages:      {statistics.mean(pages):.0f}")
    print(f"Longest book:       {max(pages)} pages")
    print(f"Shortest book:      {min(pages)} pages")

basic_stats(books)

# ============================================================
# 3. AUTHORS ANALYSIS
# ============================================================

def authors_analysis(books):
    """Analyse authors in the collection."""
    authors = [b["author"] for b in books]
    author_counts = Counter(authors)

    print("\n--- Authors Analysis ---")
    print(f"Unique authors: {len(author_counts)}")
    print("\nTop 10 most represented authors:")
    for author, count in author_counts.most_common(10):
        print(f"  {author}: {count} books")


# ============================================================
# 4. DECADES ANALYSIS
# ============================================================

def decades_analysis(books):
    """Analyse books by decade of publication."""
    decades = [(b["year"] // 10) * 10 for b in books]
    decade_counts = Counter(decades)

    print("\n--- Books by Decade ---")
    for decade in sorted(decade_counts.keys()):
        count = decade_counts[decade]
        bar = "█" * count
        print(f"  {decade}s: {bar} ({count})")


authors_analysis(books)
decades_analysis(books)

# ============================================================
# 5. RATINGS ANALYSIS
# ============================================================

def ratings_analysis(books):
    """Analyse books by rating."""
    print("\n--- Books by Rating ---")
    for rating in range(10, 0, -1):
        rated = [b for b in books if b["rating"] == rating]
        bar = "█" * len(rated)
        print(f"  {rating}/10: {bar} ({len(rated)})")

    print("\nTop 10 highest rated books:")
    sorted_books = sorted(books, key=lambda b: b["rating"], reverse=True)
    for book in sorted_books[:10]:
        print(f"  {book['rating']}/10 - {book['title']} by {book['author']}")


ratings_analysis(books)

# ============================================================
# 6. GENERATE REPORT
# ============================================================

def generate_report(books, filepath="report.txt"):
    """Generate a text report and save to file."""
    from datetime import date
    ratings = [b["rating"] for b in books]
    pages = [b["pages"] for b in books]
    authors = Counter([b["author"] for b in books])
    sorted_books = sorted(books, key=lambda b: b["rating"], reverse=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("BOOKS COLLECTION ANALYSIS REPORT\n")
        f.write(f"Generated: {date.today()}\n")
        f.write("=" * 50 + "\n\n")

        f.write("BASIC STATISTICS\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total books:    {len(books)}\n")
        f.write(f"Avg rating:     {statistics.mean(ratings):.2f}\n")
        f.write(f"Median rating:  {statistics.median(ratings):.2f}\n")
        f.write(f"Avg pages:      {statistics.mean(pages):.0f}\n")
        f.write(f"Longest book:   {max(pages)} pages\n")
        f.write(f"Shortest book:  {min(pages)} pages\n\n")

        f.write("TOP 10 AUTHORS\n")
        f.write("-" * 30 + "\n")
        for author, count in authors.most_common(10):
            f.write(f"{author}: {count} books\n")

        f.write("\nTOP 10 HIGHEST RATED BOOKS\n")
        f.write("-" * 30 + "\n")
        for book in sorted_books[:10]:
            f.write(f"{book['rating']}/10 - {book['title']} by {book['author']}\n")

    print(f"\nReport saved to '{filepath}'!")


generate_report(books)