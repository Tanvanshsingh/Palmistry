function uploadFile() {
    const fileInput = document.getElementById('uploadInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('results').innerHTML = `
            <p><strong>Palmistry Reading:</strong></p>
            <p>${data.reading}</p>
            <p><strong>Additional Information:</strong></p>
            <p>${data.info}</p>
        `;
    })
    .catch(error => console.error('Error:', error));
}
