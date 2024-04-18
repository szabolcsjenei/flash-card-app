# Flash Card App

A simple flash card application built with Python using the Tkinter library. This app helps users learn new words in a foreign language by presenting them with flash cards and allowing them to mark whether they know the word or not.
Each flash card is displayed for 3 seconds before revealing the meaning.

![flashcard](https://github.com/szabolcsjenei/flash-card-app/assets/131205642/779e1d09-6f9b-4df0-9d5c-7c7594e4710e)

## Features

- Displays flash cards with words in French and their corresponding English translations.
- Allows users to mark whether they know the word or not.
- Automatically saves words that the user needs to practice to a file for later review.

## Requirements

- Python 3.x
- Pandas library

## How to Use

1. Clone this repository:
   
   `git clone https://github.com/szabolcsjenei/flash-card-app.git`

2. Navigate to the project directory:
   
   `cd flash-card-app`

3. Install dependencies:
   
   `pip install pandas`

4. Run the app:
   
   `python main.py`

5. Use the right button if you know the word or the wrong button if you don't. The app will automatically load the next word.

## Data Storage

The app uses a CSV file to store the words for learning. By default, it looks for a file named `french_words.csv` in the `data` directory. After you mark a word as known, the program will create or update `words_to_learn.csv`, which will contain words from the original `french_words.csv` but it removes the known word from the file.

## Customization

- Feel free to add more words to the `french_words.csv` file or modify the existing one.
