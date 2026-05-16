"""Pure-Python dataclasses for PISA wire message payloads.

These shared types intentionally do not import generated protobuf modules.
Role-specific APIs such as ``pisa_api.simulator`` and ``pisa_api.av`` re-export
the relevant names so wrapper authors can stay out of ``*_pb2``.
"""

from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path
from typing import Any, Dict, List, Optional


class ControlMode(IntEnum):
    NONE = 0
    TRAJECTORY = 1
    THROTTLE_STEER = 2
    WAYPOINTS = 3
    POSITION = 4
    ACKERMANN = 5
    THROTTLE_STEER_BREAK = 6


class RoadObjectType(IntEnum):
    UNKNOWN = 0
    CAR = 1
    TRUCK = 2
    BUS = 3
    SEMITRAILER = 4
    TRAILER = 5
    MOTORCYCLE = 6
    BICYCLE = 7
    PEDESTRIAN = 8
    VAN = 9
    TRAIN = 10
    TRAM = 11
    WHEEL_CHAIR = 12
    WHEELCHAIR = 12
    ANIMAL = 13


class ShapeType(IntEnum):
    BOUNDING_BOX = 0
    CYLINDER = 1
    POLYGON = 2


@dataclass(frozen=True)
class WorldPositionData:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    h: float = 0.0
    p: float = 0.0
    r: float = 0.0
    h_relative: float = 0.0


@dataclass(frozen=True)
class LanePositionData:
    road_id: int = 0
    lane_id: int = 0
    s: float = 0.0
    offset: float = 0.0
    junction_id: Optional[int] = None


@dataclass(frozen=True)
class PositionData:
    lane: LanePositionData = field(default_factory=LanePositionData)
    world: WorldPositionData = field(default_factory=WorldPositionData)


@dataclass(frozen=True)
class SpawnConfigData:
    position: PositionData = field(default_factory=PositionData)
    speed: float = 0.0


@dataclass(frozen=True)
class GoalConfigData:
    position: PositionData = field(default_factory=PositionData)


@dataclass(frozen=True)
class EgoConfigData:
    target_speed: float = 0.0
    spawn_config: SpawnConfigData = field(default_factory=SpawnConfigData)
    goal_config: GoalConfigData = field(default_factory=GoalConfigData)


@dataclass(frozen=True)
class ScenarioData:
    format: str = ""
    name: str = ""
    path: Optional[Path] = None


@dataclass(frozen=True)
class ScenarioPackData:
    name: str = ""
    map_name: str = ""
    scenarios: Dict[str, Path] = field(default_factory=dict)
    param_range_file: Optional[Path] = None
    ego: EgoConfigData = field(default_factory=EgoConfigData)
    timeout_ns: int = 0


@dataclass(frozen=True)
class ControlCommand:
    mode: ControlMode = ControlMode.NONE
    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ObjectKinematicData:
    time_ns: int = 0
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    yaw: float = 0.0
    speed: float = 0.0
    acceleration: float = 0.0
    yaw_rate: float = 0.0
    yaw_acceleration: float = 0.0


@dataclass(frozen=True)
class ShapeDimensionData:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


@dataclass(frozen=True)
class ShapeVertexData:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


@dataclass(frozen=True)
class ShapeData:
    type: ShapeType = ShapeType.BOUNDING_BOX
    dimensions: ShapeDimensionData = field(default_factory=ShapeDimensionData)
    vertices: List[ShapeVertexData] = field(default_factory=list)


@dataclass(frozen=True)
class ObjectStateData:
    type: RoadObjectType = RoadObjectType.UNKNOWN
    kinematic: ObjectKinematicData = field(default_factory=ObjectKinematicData)
    shape: Optional[ShapeData] = None


@dataclass(frozen=True)
class CollisionInfoData:
    occurred: bool = False
    actor_a: Optional[int] = None
    actor_b: Optional[int] = None
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RuntimeFrameData:
    sim_time_ns: int = 0
    objects: List[ObjectStateData] = field(default_factory=list)
    collision: List[CollisionInfoData] = field(default_factory=list)
    extras: Dict[str, Any] = field(default_factory=dict)


__all__ = [
    "CollisionInfoData",
    "ControlCommand",
    "ControlMode",
    "EgoConfigData",
    "GoalConfigData",
    "LanePositionData",
    "ObjectKinematicData",
    "ObjectStateData",
    "PositionData",
    "RoadObjectType",
    "RuntimeFrameData",
    "ScenarioData",
    "ScenarioPackData",
    "ShapeData",
    "ShapeDimensionData",
    "ShapeType",
    "ShapeVertexData",
    "SpawnConfigData",
    "WorldPositionData",
]
