import pizza_utils
import random
from ruamel.yaml import YAML

def genp():
    p = random.choice(pizza_utils.pizzas_disponiveis)
    return p.lower()

def main():
    yaml = YAML()
    yaml.preserve_quotes = True
    with open("data/back.nlu.yml") as fin:
        data = fin.read()
    data = yaml.load(data)
    # pedidos = data["nlu"][2]["examples"].split("\n")
    # proc = [reply.replace("{endereco}",
    #         f"[{pizza_utils.slot_value_endereco()}](endereco)") for reply in pedidos]
    # data["nlu"][2]["examples"] = "\n".join(proc)
    # pedidos = data["nlu"][1]["examples"].split("\n")
    # proc = [reply.replace("{itens}", f"[{genp()}](itens)") for reply in pedidos]
    # data["nlu"][1]["examples"] = "\n".join(proc)
    pedidos = data["nlu"][3]["examples"].split("\n")
    proc = [reply.replace("{endereco}",
            f"[{pizza_utils.slot_value_endereco()}](endereco)") for reply in pedidos]
    data["nlu"][3]["examples"] = "\n".join(proc)
    with open("data/nlu.yml", "w") as fout:
        yaml.dump(data, fout)

if __name__ == "__main__":
    main()

