# Books Collection Analysis 📚

A data analysis project exploring a personal book collection of 179 books.
Built with **Python built-ins only** — no pandas, no numpy.

## Project Overview

This project analyzes a personal reading list to uncover patterns in:
- Rating distribution across the collection
- Most represented authors
- Publication trends by decade
- Top rated books

## Dataset

- **File:** `data/books.csv`
- **Records:** 179 books
- **Fields:** title, author, year, pages, rating

## Key Findings

- Average rating: **7.80 / 10**
- Most prolific author: **Stephen King** (12 books)
- Most popular decade: **2000s** (36 books)
- Highest rated: **Mały Książę, Hobbit, Gra o tron, Diuna, Mistrz i Małgorzata** (10/10)

## Project Structure

- `data/books.csv` — raw dataset
- `analysis.py` — main analysis script
- `report.txt` — generated report
- `README.md` — project documentation

## How to Run

```bash
git clone https://github.com/sp9end/books-analysis.git
cd books-analysis
python -m venv venv
venv\Scripts\activate
python analysis.py
```

## Tools Used

- Python 3.12
- csv, statistics, collections, datetime, os (built-in modules only)

## Author

Barbara | Aspiring Data Analyst