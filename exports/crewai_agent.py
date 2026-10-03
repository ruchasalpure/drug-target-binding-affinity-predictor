from crewai import Agent

drug_target_binding_affinity_predictor = Agent(
    role="Drug Target Binding Affinity Predictor",
    goal="Deliver high-precision autonomous Drug Target Binding Affinity Predictor operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
