# Daily English Word Generator

A small Python project that starts with 100 random English words, adds one new word each day, and includes an interactive quiz mode for practice.

<!-- WORD_STATS_START -->
- Total words: **100**
- Latest word: **priority** (noun, intermediate)
- Meaning: something more important than other things
- Example: Health should be a priority.
- Last added: 2026-06-12
<!-- WORD_STATS_END -->

## Features

- Starts with 100 unique English words from a curated local word bank.
- Adds one unused word per day.
- Stores each word with a meaning, example sentence, part of speech, difficulty, date, and source.
- Includes a multiple-choice quiz mode.
- Includes a GitHub Actions workflow template to update the repository every day at 8 PM London time.
- Runs with the Python standard library only.

## Quick Start

```bash
python src/word_generator.py today
```

Show recent words:

```bash
python src/word_generator.py list --limit 10
```

Play quiz mode:

```bash
python src/word_generator.py quiz --questions 5
```

Show stats:

```bash
python src/word_generator.py stats
```

## Initialize Or Reset Data

The repository already includes an initialized `data/words.json` file. To regenerate it:

```bash
python src/word_generator.py init --count 100 --seed launch --overwrite --readme
```

## Add A Daily Word Manually

```bash
python src/word_generator.py add --readme
```

The script will not add two daily words for the same local date.

## Automation

The workflow template in `docs/daily-word.workflow.yml` runs every day around 8 PM London time. GitHub schedules use UTC, so the workflow runs at both possible UTC times and the Python script only updates the word list when the local London hour is actually 20:00.

Manual workflow runs are also supported from the GitHub Actions tab.

To activate the workflow, copy the template to `.github/workflows/daily-word.yml`. If GitHub rejects the push because your token is missing `workflow` scope, see `docs/enable-github-actions.md`.

## Run Tests

```bash
python -m unittest discover -s tests
```

## Project Structure

```text
.
├── data/words.json
├── docs/daily-word.workflow.yml
├── docs/enable-github-actions.md
├── src/word_generator.py
├── tests/test_word_generator.py
└── README.md
```

## Ideas To Extend

- Add a web page with GitHub Pages.
- Add word categories such as business, travel, academic, and everyday English.
- Export a daily flashcard deck.
- Add a spaced-repetition review score.
- Let users contribute new words with pull requests.
