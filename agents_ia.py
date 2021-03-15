
from agents4e import TrivialVacuumEnvironment, ReflexVacuumAgent


def teste_ReflexVacuumAgent():
    print("\nAgente ReflexVacuumAgent:")
    # create an object of the ReflexVacuumAgent
    agent = ReflexVacuumAgent()
    # create an object of the TrivialVacuumEnvironment
    environment = TrivialVacuumEnvironment()
    # add agent to the environment
    environment.add_thing(agent)

    passos = 10  # numero total de passos de simulaçao a executar
    for passo in range(passos):
        print_simulation_status(passo, environment, agent)
        environment.step()
    print_simulation_status(passo, environment, agent)  #estado final


def print_simulation_status(passo, environment, agent):
    print(f"\nEstado t={passo}:")
    print(f'Percepção do agente: {environment.percept(agent)}')
    print(f'Estado do ambiente: {environment.status}')