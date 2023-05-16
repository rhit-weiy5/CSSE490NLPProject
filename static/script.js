document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('sentimentForm');
  const resultContainer = document.getElementById('resultContainer');
  const resultElement = document.getElementById('sentimentResult');

  form.addEventListener('submit', function(event) {
    event.preventDefault(); 

    const textData = document.getElementById('textData').value;

    // Send the textData to the Flask route for sentiment analysis
    fetch('/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ textData })
    })
    .then(response => response.json())
    .then(data => {
      // Update the resultElement with the sentiment value received from the server
      const sentiment = data.sentiment;
      resultElement.textContent = 'Sentiment: ' + sentiment;

      // Display the resultContainer
      resultContainer.style.display = 'block';
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });
});
