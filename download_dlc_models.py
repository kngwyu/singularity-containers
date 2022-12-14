from pathlib import Path

from deeplabcut.utils import auxfun_models, auxiliaryfunctions


def download_models() -> None:
    dlc_path = auxiliaryfunctions.get_deeplabcut_path()
    networks = [
        "resnet_50",
        "resnet_101",
        "resnet_152",
        "mobilenet_v2_1.0",
        "mobilenet_v2_0.75",
        "mobilenet_v2_0.5",
        "mobilenet_v2_0.35",
        "efficientnet-b0",
        "efficientnet-b3",
        "efficientnet-b6",
    ]
    for network in networks:
        auxfun_models.check_for_weights(network, Path(dlc_path), 1)


if __name__ == "__main__":
    download_models()
