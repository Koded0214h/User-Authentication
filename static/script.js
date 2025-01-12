document.getElementById('profile-picture-input').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const preview = document.getElementById('profile-picture-preview');
    
    if (file) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            preview.src = e.target.result; // Set the uploaded image as the preview
        }
        
        reader.readAsDataURL(file);
    }
});
