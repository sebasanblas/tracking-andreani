# tracking-andreani

Script para obtener status de paquete de Andreani y enviar mensaje a bot personal de Telegram.

Escrito por Sebastian San Blas.

### Modificar variables dentro del script para el correcto funcionamiento.

tracking_andreani.py utiliza chromedriver que debe coincidir con la versión de Google Chrome  (ver [Chromedriver](https://chromedriver.chromium.org/)).

## ¿Cómo ejecutar?

Dar permisos de ejecución `chmod +x tracking_andreani.py`

Ejecutar `./tracking_andreani.py`

## ¿Cómo automatizar via cron?

Ejecutar `crontab -e`

Agregar `*/30 * * * * ((Ubicación personal))/tracking-andreani/tracking_andreani.py` para una ejecución cada 30 minutos.


## IMPORTANTE: este script fue elaborado con fines totalmente didácticos, no comerciales. No hay una intencionalidad de perjudicar a Andreani. La empresa no participó en ninguna instancia del proceso. Es un proyecto individual. 
