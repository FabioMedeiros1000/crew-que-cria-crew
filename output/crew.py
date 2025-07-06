from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CreateCrewProject():
    """CreateCrewProject crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def agente_de_pesquisa(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_de_pesquisa'],
            verbose=True,
        )

    @agent
    def agente_de_topicos(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_de_topicos'],
            verbose=True
        )

    @agent
    def agente_de_escopo(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_de_escopo'],
            verbose=True
        )

    @agent
    def agente_de_redacao(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_de_redacao'],
            verbose=True
        )

    @agent
    def agente_de_revisao(self) -> Agent:
        return Agent(
            config=self.agents_config['agente_de_revisao'],
            verbose=True
        )


    @task
    def pesquisa_de_conteudo(self) -> Task:
        return Task(
            config=self.tasks_config['pesquisa_de_conteudo'],
        )

    @task
    def analise_de_topicos(self) -> Task:
        return Task(
            config=self.tasks_config['analise_de_topicos'],
        )

    @task
    def definicao_de_escopo(self) -> Task:
        return Task(
            config=self.tasks_config['definicao_de_escopo'],
        )

    @task
    def redacao_do_curso(self) -> Task:
        return Task(
            config=self.tasks_config['redacao_do_curso'],
        )

    @task
    def revisao_do_curso(self) -> Task:
        return Task(
            config=self.tasks_config['revisao_do_curso'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CreateCrewProject crew"""

        return Crew(
            agents=self.agents,  
            tasks=self.tasks,  
            process=Process.sequential,
            verbose=True,
        )