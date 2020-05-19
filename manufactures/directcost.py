import numpy as np

from openmdao.api import ExplicitComponent


class directcost(ExplicitComponent):

#Ca : aircraft cost less engine
#Ce : cost per engine
#Ne : number of engines

    #def initialize(self):
        #self.options.declare('Ne', types=float)
        #self.options.declare('Ca', types=float)
        #self.options.declare('Ce', types=float

    def setup(self):
        self.add_input('Ca')
        self.add_input('Ce')
        self.add_input('Ne')
        self.add_output('directcost')

        self.declare_partials('directcost', 'Ca')
        self.declare_partials('directcost', 'Ce')
        self.declare_partials('directcost', 'Ne')

    def compute(self, inputs, outputs):
        Ca = inputs['Ca']
        Ce = inputs['Ce']
        Ne = inputs['Ne']

        outputs['directcost'] = 
    def compute_partials(self, inputs, partials):
        N = self.options['N']
        tc = self.options['tc']
        AR = self.options['AR']
        sweep = self.options['sweep']

        W0 = inputs['W0']
        Swing = inputs['Swing']

        cosSweep = np.cos(sweep * np.pi / 180)

        partials['Wwing', 'W0'] = 0.0051 * 0.557 * W0 ** -0.443 * N ** 0.557 * Swing ** 0.649 * AR ** 0.5 * tc ** -0.4 * cosSweep ** -1 * 0.1 ** 0.1 * Swing ** 0.1
        partials['Wwing', 'Swing'] = 0.0051 * W0 ** 0.557 * N ** 0.557 * 0.649 * Swing ** -0.351 * AR ** 0.5 * tc ** -0.4 * cosSweep ** -1 * 0.1 ** 0.1 * 0.1 * Swing ** -0.9
© 2020 GitHub, Inc.
