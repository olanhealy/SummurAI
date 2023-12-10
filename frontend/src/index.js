// This code assumes your form has an ID of 'uploadForm' and you have a div with an ID of 'summary' for displaying the results

document.addEventListener('DOMContentLoaded', () => {
    // Attach the event listener to the form after the DOM is fully loaded
    const form = document.getElementById('uploadForm');
    form.addEventListener('submit', function(event) {
      // Prevent the default form submission
      event.preventDefault();
  
      // Create a FormData object, passing in the form
      const formData = new FormData(this);
  
      // Use fetch to send the form data to the server's '/upload' endpoint
      fetch('/upload', {
        method: 'POST',
        body: formData,
      })
      .then(response => {
        // Check if the response is ok (status code 200-299)
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        // Parse the text stream response body
        return response.text();
      })
      .then(data => {
        // Display the response data in the summary element
        document.getElementById('summary').textContent = data;
      })
      .catch(error => {
        // Handle any errors that occurred during fetch
        console.error('There has been a problem with your fetch operation:', error);
      });
    });
  });
  