import dataclasses


@dataclasses.dataclass
class FuzzerConfig:
    time_budget: float = 600
    warm_up_times: int = 5
    url: str = "http://localhost:8080/api/v3"
    output_dir: str = "output"
