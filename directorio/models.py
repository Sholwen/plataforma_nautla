from django.db import models

class LugarTuristico(models.Model):
    """
    Modelo que representa los lugares del directorio turístico del municipio.
    """
    # --- TEXTOS CORTOS (CharField) ---
    nombre = models.CharField(
        max_length=200, 
        verbose_name="Nombre del Lugar"
    )
    telefono = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        verbose_name="Teléfono de Contacto"
    )
    rutas = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Rutas de Acceso / Dirección"
    )
    
    # --- TEXTOS LARGOS (TextField) ---
    descripcion = models.TextField(
        verbose_name="Descripción del Lugar"
    )
    observaciones = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Observaciones o Notas Adicionales"
    )
    
    # --- FECHA Y HORA (DateTimeField) ---
    festividades = models.DateTimeField(
        blank=True, 
        null=True, 
        verbose_name="Fecha y Hora de Festividades"
    )
    
    # --- IMÁGENES (ImageField) ---
    # Los archivos se subirán a la carpeta 'media/lugares/'
    imagen_principal = models.ImageField(
        upload_to='lugares/principales/', 
        blank=True, 
        null=True, 
        verbose_name="Imagen Principal"
    )
    galeria_fotos = models.ImageField(
        upload_to='lugares/galeria/', 
        blank=True, 
        null=True, 
        verbose_name="Fotos de la Galería"
    )
    
    # --- BOOLEANOS (BooleanField) ---
    # Define si el lugar es familiar (False) o exclusivo de adultos (True)
    es_solo_adultos = models.BooleanField(
        default=False, 
        verbose_name="¿Es exclusivo para adultos?"
    )

    class Meta:
        verbose_name = "Lugar Turístico"
        verbose_name_plural = "Lugares Turísticos"

    def __str__(self):
        # Define cómo se identificará el registro en el panel de administración
        return self.nombre
