# Mood Me UP

Mood Me UP is an application designed to suggest happy music to users based on their mood. Utilizing the Spotify API, the app fetches tracks characterized by certain audio features associated with happiness. These key audio features include valence, energy, and tempo.

## Key Audio Features for Happy Music

- **Valence**: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g., happy, cheerful, euphoric).
- **Energy**: A measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.
- **Tempo**: The overall estimated tempo of a track in beats per minute (BPM). Happy music often has a higher tempo.

## Installation

To set up the Mood Me UP app, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/MoodMeUP.git
    cd MoodMeUP
    ```

2. **Install the required packages:**

    ```bash
    pip install pandas
    pip install notify-py
    pip install requests
    ```

3. **Environment Variables:**
   Create a `.env` file in the project directory to store your Spotify API credentials.

    ```bash
    touch .env
    ```

    Add your Spotify API credentials to the `.env` file:

    ```env
    SPOTIFY_CLIENT_ID=your_spotify_client_id
    SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
    ```

## Imports

The following Python packages are used in the project:

- `notifypy`
- `requests`
- `pandas`
- `base64`
- `dotenv`
- `os`

## How to Use

1. **Load Environment Variables:** Load your environment variables (Spotify API credentials) using `dotenv`.

2. **Authenticate with Spotify API:** Authenticate and get access to Spotify API.

3. **Fetch Happy Music Recommendations:** Use the Spotify API to fetch tracks with high valence, energy, and tempo.

4. **Notify User:** Notify the user about the happy music recommendations.

## Analyzing Database

The application can also analyze a database of tracks to suggest happy music. Ensure your database is in a compatible format (e.g., CSV) and load it using pandas.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy listening with Mood Me UP!
