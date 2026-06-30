from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.full_name


class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    transmission_mode = models.CharField(max_length=100)
    incubation_period = models.CharField(max_length=100)
    prevention = models.TextField()

    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.name


class Symptom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    severity_level = models.CharField(max_length=20)
    symptom_code = models.CharField(max_length=20)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.name

class HealthReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    symptoms = models.ManyToManyField(Symptom)
    report_date = models.DateField()
    risk_level = models.CharField(max_length=20)

    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return f"{self.patient.full_name} - {self.report_date}"