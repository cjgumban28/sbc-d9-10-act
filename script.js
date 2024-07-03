document.getElementById('birthdayForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const birthday = document.getElementById('birthday').value;
    
    fetch('/calculate_age', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, birthday })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('displayName').textContent = `Name: ${data.name}`;
        document.getElementById('displayAge').textContent = `Age: ${data.age}`;
    })
    .catch(error => console.error('Error:', error));
});
