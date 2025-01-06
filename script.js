const BUCKET_URL = 'https://devopsweatherdashboard.s3.amazonaws.com/';

async function fetchS3Data() {
  try {
    // Fetch the JSON file directly from S3
    const response = await fetch(`${BUCKET_URL}weather-data.json`);
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

    const data = await response.json();
    displayData(data);
  } catch (error) {
    console.error('Error fetching S3 data:', error);
    document.getElementById(
      'data-container'
    ).innerHTML = `<p style="color:red;">Failed to load data.</p>`;
  }
}
