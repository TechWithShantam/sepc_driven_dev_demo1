document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('uploadForm').onsubmit = async function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        const res = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        const data = await res.json();
        const container = document.getElementById('tableContainer');
        if (data.error) {
            container.innerHTML = `<p style='color:red;'>${data.error}</p>`;
            return;
        }
        let html = '';
        if (Array.isArray(data.columns) && Array.isArray(data.rows)) {
            html = '<table><thead><tr>';
            data.columns.forEach(col => html += `<th>${col}</th>`);
            html += '</tr></thead><tbody>';
            data.rows.forEach(row => {
                if (Array.isArray(row)) {
                    html += '<tr>' + row.map(cell => `<td>${cell}</td>`).join('') + '</tr>';
                } else {
                    html += `<tr><td colspan="${data.columns.length}">Invalid row data</td></tr>`;
                }
            });
            html += '</tbody></table>';
            if (data.warning) html += `<p style='color:orange;'>${data.warning}</p>`;
        } else {
            html = "<p style='color:red;'>No valid data received from server.</p>";
        }
        container.innerHTML = html;
    };

    document.getElementById('downloadBtn').onclick = function() {
        window.location = '/download';
    };
});
