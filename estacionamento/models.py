from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome    

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    cor = models.CharField(max_length=15)
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    observacoes = models.TextField()

    def __str__(self):
        return self.marca.nome + ' ' + self.placa

    class Meta:
        verbose_name = 'Veículo'        

class MovRotativo(models.Model):
    checkin = models.DateTimeField(auto_now=False)
    checkout = models.DateTimeField(auto_now=False, blank=True, null=True)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    pago = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Movimento Rotativo'

    def horas_total(self):
        import math
        if self.checkout:
            horas = (self.checkout - self.checkin).total_seconds() / 3600 # transformando segundos em horas
            return math.ceil(horas) # arredonda hora para cima
        else:
            return 0

    def valor(self):
        return self.valor_hora * self.horas_total()

    def __str__(self):
        return self.veiculo

    def save(self, *args, **kwargs):
        self.valor_hora = 30
        super(MovRotativo, self).__init__(*args, **kwargs)
    

    

class Parametro(models.Model):
    valor_mes = models.DecimalField(max_digits=5, decimal_places=2)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return 'Parâmetros'

    class Meta:
        verbose_name = 'Parâmetro'    

class Mensalista(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    inicio = models.DateField()
    valor_mensal = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.veiculo.placa

class MovMensalista(models.Model):
    mensalista = models.ForeignKey(Mensalista, on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.mensalista)

    class Meta:
        verbose_name = 'Movimento Mensalista'            