document.getElementById('query-time-range-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const startTime = document.getElementById('start_time').value;
    const endTime = document.getElementById('end_time').value;
    
    fetch('/query-time-range', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ start_time: startTime, end_time: endTime })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('time-range-results').innerHTML = `
            <p>Query Duration: ${data.query_duration} seconds</p>
            <pre>${JSON.stringify(data.results, null, 2)}</pre>
        `;
    });
});

document.getElementById('query-specific-time-net-value-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const time = document.getElementById('time').value;
    const netValue = document.getElementById('net_value').value;
    const count = document.getElementById('count').value;
    
    fetch('/query-specific-time-net-value', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ time: time, net_value: netValue, count: count })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('specific-time-net-value-results').innerHTML = `
            <p>Query Duration: ${data.query_duration} seconds</p>
            <pre>${JSON.stringify(data.results, null, 2)}</pre>
        `;
    });
});

document.getElementById('modify-attribute-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const time = document.getElementById('time').value;
    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;
    const depth = document.getElementById('depth').value;
    const mag = document.getElementById('mag').value;
    const net = document.getElementById('net').value;
    const id = document.getElementById('id').value;
    
    fetch('/modify-attribute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ time: time, latitude: latitude, longitude: longitude, depth: depth, mag: mag, net: net, id: id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('modify-attribute-results').innerHTML = `
            <p>${JSON.stringify(data, null, 2)}</p>
        `;
    });
});
