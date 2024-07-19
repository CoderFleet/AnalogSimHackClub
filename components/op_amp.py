class OpAmp:
    def __init__(self):
        self.input_signal = None
        self.output_signal = None

    def compute_output(self):
        if self.input_signal is not None:
            self.output_signal = self.input_signal * 10
