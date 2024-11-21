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

    let resultDiv = document.getElementById('result');

    try {
        console.log('Sending request with data:', data);

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        console.log('Response status:', response.status);

        const responseData = await response.json();
        console.log('Response data:', responseData);

        if (response.ok) {
            resultDiv.innerHTML = `
                <div class="bg-blue-50 border border-blue-200 text-blue-700 px-4 py-3 rounded relative" role="alert">
                    <strong class="font-bold">Resultado: </strong>
                    ${responseData.max_zone_name ? 
                        `La zona con mayor probabilidad de tráfico es: ${responseData.max_zone_name} a las ${new Date().getHours()}:${new Date().getMinutes()}` : 
                        'No se recibieron datos válidos de la zona'}
                </div>
            `;
        } else {
            resultDiv.innerHTML = `
                <div class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded relative" role="alert">
                    Error en la predicción: ${responseData.detail || 'Respuesta no válida'}
                </div>
            `;
        }
    } catch (error) {
        console.error('Error completo:', error);
        resultDiv.innerHTML = `
            <div class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded relative" role="alert">
                Error de conexión: ${error.message}
            </div>
        `;
    }
});