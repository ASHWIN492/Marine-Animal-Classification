function classifyImage() {
    const imageInput = document.getElementById("imageInput");
    const resultText = document.getElementById("resultText");
    const imagePreview = document.getElementById("imagePreview");
    const loadingSpinner = document.getElementById("loadingSpinner");

    resultText.innerText = "";
    loadingSpinner.style.display = "block";

    // Check if an image is selected
    if (imageInput.files.length > 0) {
        const file = imageInput.files[0];

        // Display image preview
        const reader = new FileReader();
        reader.onload = function (e) {
            imagePreview.innerHTML = `<img src="${e.target.result}" alt="Uploaded Image">`;
        };
        reader.readAsDataURL(file);

        // Create FormData object to send the image file to Flask backend
        const formData = new FormData();
        formData.append("image", file);

        // Make a POST request to Flask backend
        fetch("/classify", {
            method: "POST",
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            // Update the resultText with the classification result
            resultText.innerText = `Result: ${data.result}`;
            loadingSpinner.style.display = "none";
        })
        .catch(error => {
            console.error("Error:", error);
            resultText.innerText = "Error occurred during classification.";
            loadingSpinner.style.display = "none";
        });
    } else {
        resultText.innerText = "Please select an image.";
        loadingSpinner.style.display = "none";
    }
}
