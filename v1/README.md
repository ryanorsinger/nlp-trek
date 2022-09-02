# NLP Trek

## Analyzing Star Trek Transcripts with Natural Language Processing

## Data Source
- Text from http://www.chakoteya.net/StarTrek/

## What is my level of observation?
- One line or action is the observation
- Each row will have the following features:
	- episode name
	- season
	- location
	- character
	- character's line
	- some lines are captain's logs or actions

## Regular Expressions in Each Episode
- Location is denoted by square brackets like `[Bridge]`, `[Transporter room]`, or `[Ferengi Science Lab]` followed by dialog until the next location denoted.
- Actions are denoted by parentheses like `(Bok turns up the device)` or `(Crusher puts two small devices on his forehead, turns the lights out and leaves)` 
	- most actions have a new line character
	- some actions are in-line with a character's line
- Characters are denoted by all caps followed by a colon like `PICARD:`, `MCCOY:`, or `Q:`
	- One or more capital letters ending with a colon
	- When a character is in a costume, `Q (JUDGE):`
	- Some names may have numbers
- When a character is heard over communications, `PICARD [OC]:`
- Logs
	- Captain's logs look like `Captain's log, stardate 41153.7. Preparing to detach...`
	- Crew logs look like `Personal log, Commander William Riker. Stardate 41153.7.` on their own line. 
- Stardate is the word stardate followed by a number only one decimal `41153.7`

## Possibilities
- Analytics and Exploration
	- about who talks the most, least, etc...
	- Analytics about locations
	- What locations show up most frequently in episodes
	- Analytics about only the actions
	- n-grams
	- Word clouds
		- by episode
		- by season
		- by character
		- by character in 1st season vs. last season
- Topic modeling
	- compare and contrast
	- per series type (TOS, TNG, DS9, Voyager, etc...)
	- per season
	- per episode
	- by character
- Sentiment analysis
	- compare and contrast sentiment
	- by episode
	- by character
	- by season
- Character prediction classifier
	- Make a model that takes in text and returns a prediction of which character
- Dialog Generator
	- Episode generator
	- Character based chatbot like a Picard chatbot

## MVP
- Acquire all episodes from a specific series
- MVP Prepare 
	- get Captain's logs
	- get all character lines
- Explore 
- Modeling:
	- train a character prediction classifier
