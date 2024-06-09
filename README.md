# **Mood Me UP Installation Guide**

## Overview

**Mood Me UP** is an application designed to suggest happy music to users feeling sad. Utilizing the Spotify API, the app fetches tracks characterized by certain audio features associated with happiness. These key audio features include valence, energy, and tempo.

## **Key Audio Features for Happy Music:**

- **Valence:** A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g., happy, cheerful, euphoric).
- **Energy:** A measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.
- **Tempo:** The overall estimated tempo of a track in beats per minute (BPM). Happy music often has a higher tempo.

## **Installation:**

### **For Mac Users:**

1. **Clone the repository:**

   - Use `git clone` to clone the repository from GitHub.
   - Navigate to the project directory using the terminal.

2. **Install the required packages:**

   - Use `pip install` to install the necessary Python packages:
     - `pandas`
     - `notify-py`
     - `requests`

3. **Set up Environment Variables:**
   - Create a `.env` file in the project directory to store your Spotify API credentials.
   - Add your Spotify API credentials to the `.env` file:
     - `SPOTIFY_CLIENT_ID=your_spotify_client_id`
     - `SPOTIFY_CLIENT_SECRET=your_spotify_client_secret`

### **For Windows Users:**

Follow similar steps as mentioned above, but download the repository as a ZIP file from GitHub and extract it to a directory of your choice.

## **Imports:**

The following Python packages are used in the project:

- `notifypy`
- `requests`
- `pandas`
- `base64`
- `dotenv`
- `os`

## **How to Use:**

1. **Load Environment Variables:**

   - Load your environment variables (Spotify API credentials) using dotenv.

2. **Authenticate with Spotify API:**

   - Authenticate and get access to the Spotify API.

3. **Fetch Happy Music Recommendations:**

   - Use the Spotify API to fetch tracks with high valence, energy, and tempo.

4. **Notify User:**
   - Notify the user about the happy music recommendations.

## **Analyzing Database:**

The application can also analyze a database of tracks to suggest happy music. Ensure your database is in a compatible format (e.g., CSV) and load it using pandas.

## **License:**

This project is licensed under the MIT License. See the LICENSE file for details.

**Happy listening with Mood Me UP!**
