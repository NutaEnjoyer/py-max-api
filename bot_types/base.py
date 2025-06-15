from pydantic import BaseModel


class Model(BaseModel):
    def __str__(self):
        return self.model_dump_json()
