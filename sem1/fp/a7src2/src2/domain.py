class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def get_real_part(self):
        return self.real

    def get_imaginary_part(self):
        return self.imag

    def to_dict(self):
        return {'real': self.real, 'imaginary': self.imag}

    def __str__(self):
        return f"{self.real} {self.imag}"