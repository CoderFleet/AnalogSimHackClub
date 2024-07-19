class OpAmp:
    def __init__(self):
        self.input_voltage = 0
        self.output_voltage = 0

    def simulate(self):
        self.output_voltage = self.input_voltage * 10
