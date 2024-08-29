# Project Summary: Instagram to Notion Recipe Transfer App

## Project Overview

We are developing an application that extracts recipes from Instagram Reels, processes them using NLP techniques (including ChatGPT), and transfers the structured recipe information to Notion. The app aims to automate the process of capturing and organizing recipes from social media content.

## Current Project State

1. We have established a basic project structure with the following key components:

   - Instagram data extraction (placeholder implementation)
   - NLP processing using ChatGPT for recipe extraction and classification
   - Notion API integration for creating recipe pages
   - Utility functions for error handling
   - Data models for representing recipes
   - Main service for orchestrating the workflow
2. We have implemented a detailed NLP component using ChatGPT to extract and classify recipe information from transcribed audio and video descriptions.
3. We have set up environment variable management using a .env file and updated the configuration handling in config.py.

## Key Components Implemented

1. `nlp/recipe_extractor.py`: Uses ChatGPT to process transcribed audio and video descriptions, extracting structured recipe information and generating classification tags.
2. `config.py`: Manages loading of environment variables from a .env file, including API keys for Instagram, Notion, and OpenAI.
3. Basic project structure including placeholders for Instagram extraction, Notion integration, and the main workflow.

## Next Steps

1. Implement the Instagram data extraction component, including video transcription.
2. Expand and refine the Notion API integration for creating detailed recipe pages.
3. Develop a user interface (web-based or command-line) for inputting Instagram Reel URLs.
4. Implement comprehensive error handling and logging throughout the application.
5. Set up unit tests and integration tests for all components.
6. Refine the workflow orchestration in `services/workflow.py` to integrate all components seamlessly.

## Technical Considerations

- The project uses Python 3.8+ and relies on libraries such as `openai`, `notion-client`, and `python-dotenv`.
- API keys for Instagram, Notion, and OpenAI are required and should be stored securely in the .env file.
- The NLP component using ChatGPT may require fine-tuning of prompts and API parameters for optimal results.
- Consideration should be given to rate limiting and error handling for external API calls.

## Current Questions or Challenges

1. What is the best approach for extracting and transcribing audio from Instagram Reels?
2. How can we optimize the ChatGPT prompts for more accurate recipe extraction?
3. What additional features or refinements would enhance the usefulness of the Notion recipe pages?

Please continue the development of this project, focusing on implementing the next steps and addressing the current questions and challenges. Feel free to suggest improvements or alternative approaches to any aspect of the project.
