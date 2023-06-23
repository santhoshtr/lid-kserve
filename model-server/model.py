from kserve import Model, ModelServer
from typing import Dict
import fasttext


class LanguageIdentificationModel(Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.ready = False

    def load(self):
        self.model = fasttext.load_model('/mnt/models/lid201-model.bin')
        self.ready = True

    def predict(self, payload: Dict, headers: Dict[str, str] = None) -> Dict:
        text = payload["text"]
        label, score = self.model.predict(text)
        return {
            "language": label[0].replace("__label__", ""),
            "score": score[0]
        }


if __name__ == "__main__":
    model = LanguageIdentificationModel('lid-model')
    model.load()
    ModelServer(workers=1, http_port=9999).start([model])
