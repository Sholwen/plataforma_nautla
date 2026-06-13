from django.db import models

# Create your models here.
class Eventos(models.Model):
    """
    Modelo que representa los lugares del directorio turístico del municipio.
    """
    # --- TEXTOS CORTOS (CharField) ---
    nombre = models.CharField(
        max_length=200, 
        verbose_name="Nombre del Evento"
    )
    
    # --- TEXTOS LARGOS (TextField) ---
    descripcion = models.TextField(
        verbose_name="Descripción del Evento"
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
        verbose_name="Fecha y Hora del Evento"
    )
    
    # --- IMÁGENES (ImageField) ---
    # Los archivos se subirán a la carpeta 'media/lugares/'
    imagen_principal = models.ImageField(
        upload_to='eventos/principales/', 
        blank=True, 
        null=True, 
        verbose_name="Imagen Principal"
    )

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        # Define cómo se identificará el registro en el panel de administración
        return self.nombre
