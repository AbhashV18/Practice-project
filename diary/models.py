from django.db import models
from django.conf import settings


class Subject(models.Model):
    name = models.CharField("Назва предмета", max_length=100)
    short_name = models.CharField("Коротка назва", max_length=30, blank=True)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"

    def __str__(self):
        return self.short_name or self.name


class Lesson(models.Model):
    WEEKDAYS = [
        (0, "Понеділок"),
        (1, "Вівторок"),
        (2, "Середа"),
        (3, "Четвер"),
        (4, "Пʼятниця"),
        (5, "Субота"),
        (6, "Неділя"),
    ]

    LESSON_TYPES = [
        ("lecture", "Лекція"),
        ("practice", "Практика"),
        ("lab", "Лабораторна"),
        ("other", "Інше"),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    weekday = models.IntegerField("День тижня", choices=WEEKDAYS)
    start_time = models.TimeField("Початок")
    end_time = models.TimeField("Кінець")
    room = models.CharField("Аудиторія", max_length=50, blank=True)
    teacher = models.CharField("Викладач", max_length=100, blank=True)
    lesson_type = models.CharField(
        "Тип заняття", max_length=20, choices=LESSON_TYPES, default="lecture"
    )

    class Meta:
        verbose_name = "Заняття"
        verbose_name_plural = "Заняття"
        ordering = ["weekday", "start_time"]

    def __str__(self):
        return f"{self.get_weekday_display()} {self.subject} ({self.start_time}-{self.end_time})"


class Grade(models.Model):
    GRADE_TYPES = [
        ("lab", "Лабораторна робота"),
        ("practice", "Практична робота"),
        ("test", "Контрольна"),
        ("module", "Модуль"),
        ("exam", "Екзамен"),
        ("other", "Інше"),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Студент"
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name="Предмет"
    )

    grade_type = models.CharField(
        "Тип роботи",
        max_length=20,
        choices=GRADE_TYPES
    )

    grade_value = models.PositiveIntegerField("Оцінка", default=0)
    date = models.DateField("Дата", auto_now_add=True)
    comment = models.CharField("Коментар", max_length=255, blank=True)

    class Meta:
        verbose_name = "Оцінка"
        verbose_name_plural = "Оцінки"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.student.username}: {self.subject} — {self.grade_value}"

