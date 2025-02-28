async function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const response = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });

    if (response.ok) {
        const data = await response.json();
        const token = data.access_token;
        fetchContactInfo(token);
    } else {
        alert('Login failed');
    }
}

async function fetchContactInfo(token) {
    const response = await fetch('http://127.0.0.1:5000/enrichment', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('full-name').innerText = `Full Name: ${data.full_name}`;
        document.getElementById('department').innerText = `Department: ${data.department}`;
        document.getElementById('phone-number').innerText = `Phone Number: ${data.phone_number}`;
        document.getElementById('job-title').innerText = `Job Title: ${data.job_title}`;
        document.getElementById('login-form').style.display = 'none';
        document.getElementById('contact-info').style.display = 'block';
    } else {
        alert('Failed to fetch contact info');
    }
}
