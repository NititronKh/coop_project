from django.db import models

class Publish(models.Model):
    DEFAULT_TITLE = "ประกาศ"

    title = models.CharField(
        max_length=255,
        default=DEFAULT_TITLE,
        verbose_name="เรื่อง"
    )
    content = models.TextField(verbose_name="เนื้อหา")
    image = models.ImageField(upload_to='media/publish_images/', null=True, blank=True, verbose_name="รูปภาพ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Publish"
        verbose_name_plural = "Publishes"

