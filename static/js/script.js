function sendRequest() {
    const text = document.getElementById('textInput').value;
    const shift = document.getElementById('shiftInput').value;
    fetch('/cipher', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text, shift: Number(shift) }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Encrypted Text: ${data.result}`;
    })
    .catch(error => console.error('Error:', error));
}
