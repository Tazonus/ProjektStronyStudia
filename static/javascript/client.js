document.addEventListener("DOMContentLoaded", function() {
    function fetchImage(event) {
        event.preventDefault();

        const form = document.getElementById('imageForm');
        const formData = new FormData(form);

        fetch('/send-message', {
            method: 'POST',
            body: formData
        })
        .then(response => response.blob())
        .then(blob => {

            const imgURL = URL.createObjectURL(blob);
            const img = document.createElement('img');
            img.src = imgURL;

            const wrapper = document.querySelector('.image_wrapper');
            wrapper.innerHTML = '';
            wrapper.appendChild(img);
        })
        .catch(error => console.error('Error:', error));
    }
    document.getElementById('imageForm').addEventListener('submit', fetchImage);
});
