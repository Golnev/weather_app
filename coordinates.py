# # NamedTuple
#
# from typing import NamedTuple
#
#
# class Coordinates(NamedTuple):
#     latitude: float
#     longitude: float
#
#
# def get_gps_coordinates() -> Coordinates:
#     """Returns current coordinates using GPS"""
#     return Coordinates(10, 20)
# # Обычный словарь dict
#
# def get_gps_coordinates() -> dict[str, float]:
#     return {'longitude': 10, 'latitude': 20}
# # Словарь с Literal ключами
#
# from typing import Literal
#
#
# def get_gps_coordinates() -> dict[Literal['longitude'] | Literal['latitude'], float]:
#     return {'longitude': 10, 'latitude': 20}
#
# # def get_gps_coordinates() -> dict[Literal["longitude", "latitude"], float]:
# #     return {"longitude": 10, "latitude": 20}
# # TypedDict
# from typing import TypedDict
#
#
# class Coordinates(TypedDict):
#     longitude: float
#     latitude: float
#
#
# c = Coordinates(longitude=10, latitude=20)
import ipaddress
# Dataclass
import re
from dataclasses import dataclass
from typing import TypeAlias

import requests

import config
from exceptions import CantGetIPAddress, CantGetCoordinates


@dataclass(slots=True, frozen=True)
# frozen=True - структура неизменна,
# slots=True = __slots__ более быстрый доступ к атрибутам и более эффективное хранение в памяти
class Coordinates:
    longitude: float
    latitude: float


IPAddress: TypeAlias = str


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using GPS"""

    ip_address = _get_ip_address()
    data_from_ip = _get_data_from_ip(ip_address)
    coordinates = _get_coordinates(data_from_ip)

    return _round_coordinates(coordinates)


def _get_ip_address() -> IPAddress:
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip = response.json()['ip']
        return ip
    except Exception:
        raise CantGetIPAddress()


def _get_data_from_ip(ip: IPAddress) -> dict:
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        return data
    except Exception:
        raise CantGetCoordinates()


def _get_coordinates(data: dict) -> Coordinates:
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    if not longitude or not latitude:
        raise CantGetCoordinates()

    return Coordinates(longitude=longitude, latitude=latitude)


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDINATES:
        return coordinates
    return Coordinates(*map(lambda c: round(c, 1), [coordinates.longitude, coordinates.latitude]))


if __name__ == '__main__':
    print(get_gps_coordinates())
