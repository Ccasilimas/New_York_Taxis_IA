document.getElementById('predictionForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const PULocationID = document.getElementById('PULocationID').value;
    const pickup_weekday = new Date().getDay(); // Día de la semana (0 para Domingo hasta 6 para Sábado)
    const pickup_hour = new Date().getHours();    // Hora actual en formato 24 horas

    // URL del endpoint de FastAPI
    const url = 'http://0.tcp.ngrok.io:16013/predict/';

    // Datos a enviar en la solicitud
    const data = {
        PULocationID: parseInt(PULocationID),
        pickup_weekday: pickup_weekday,
        pickup_hour: pickup_hour
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const responseData = await response.json();
        let resultDiv = document.getElementById('result');

        if (response.ok) {
            resultDiv.innerHTML = `
                <div class="bg-blue-50 border border-blue-200 text-blue-700 px-4 py-3 rounded relative" role="alert">
                    <strong class="font-bold">Resultado: </strong>
                    La zona con mayor probabilidad de tráfico es: ${responseData.max_zone_name} a las ${new Date().getHours()}:${new Date().getMinutes()}
                </div>