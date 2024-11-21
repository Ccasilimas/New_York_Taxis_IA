<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtener los datos del formulario
    $PULocationID = $_POST['PULocationID'];
    $pickup_weekday = date('w'); // Día de la semana (0 para Domingo hasta 6 para Sábado)
    $pickup_hour = date('G');    // Hora actual en formato 24 horas
    
    // URL del contenedor Docker (ajusta según tu configuración)
    $url = 'http://0.tcp.ngrok.io:16013/predict/';

    // Datos a enviar en la solicitud
    $data = array(
        "PULocationID" => intval($PULocationID),
        "pickup_weekday" => intval($pickup_weekday),
        "pickup_hour" => intval($pickup_hour)
    );

    // Inicializar cURL
    $ch = curl_init($url);

    // Configurar las opciones de cURL
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

    // Ejecutar la solicitud y obtener la respuesta
    $response = curl_exec($ch);

    if (curl_errno($ch)) {
        $error = 'Error de conexión: ' . curl_error($ch);
    } else {
        $responseData = json_decode($response, true);
        
        // Verificar si la respuesta es válida
        if ($responseData === null) {
            $error = 'Error al decodificar la respuesta JSON';
        }
    }

    // Cerrar cURL
    curl_close($ch);
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado de Predicción</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="w-full max-w-md">
        <?php if (isset($error)): ?>
            <div class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded relative" role="alert">
                <?php echo $error; ?>
            </div>
        <?php elseif (isset($responseData['max_zone_name'])): ?>
            <div class="bg-blue-50 border border-blue-200 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <strong class="font-bold">Resultado: </strong>
                La zona con mayor probabilidad de tráfico es: <?php echo $responseData['max_zone_name']; ?> a las <?php echo date('G:i'); ?>
            </div>
        <?php else: ?>
            <div class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded relative" role="alert">
                Error en la predicción: No se recibió una respuesta válida
            </div>
        <?php endif; ?>
        
        <div class="mt-4 text-center">
            <a href="index.html" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
                Volver al Inicio
            </a>
        </div>
    </div>
</body>
</html>
<?php } ?>