import datetime
import sys
from typing import Literal, SupportsFloat, TypedDict

from ._typing import CapsuleType

littlecms_version: str | None

_Tuple3f = tuple[float, float, float]
_Tuple2x3f = tuple[_Tuple3f, _Tuple3f]
_Tuple3x3f = tuple[_Tuple3f, _Tuple3f, _Tuple3f]

class _IccMeasurementCondition(TypedDict):
    observer: int
    backing: _Tuple3f
    geo: str
    flare: float
    illuminant_type: str

class _IccViewingCondition(TypedDict):
    illuminant: _Tuple3f
    surround: _Tuple3f
    illuminant_type: str

class CmsProfile:
    @property
    def rendering_intent(self) -> int: ...
    @property
    def creation_date(self) -> datetime.datetime | None: ...
    @property
    def copyright(self) -> str | None: ...
    @property
    def target(self) -> str | None: ...
    @property
    def manufacturer(self) -> str | None: ...
    @property
    def model(self) -> str | None: ...
    @property
    def profile_description(self) -> str | None: ...
    @property
    def screening_description(self) -> str | None: ...
    @property
    def viewing_condition(self) -> str | None: ...
    @property
    def version(self) -> float: ...
    @property
    def icc_version(self) -> int: ...
    @property
    def attributes(self) -> int: ...
    @property
    def header_flags(self) -> int: ...
    @property
    def header_manufacturer(self) -> str: ...
    @property
    def header_model(self) -> str: ...
    @property
    def device_class(self) -> str: ...
    @property
    def connection_space(self) -> str: ...
    @property
    def xcolor_space(self) -> str: ...
    @property
    def profile_id(self) -> bytes: ...
    @property
    def is_matrix_shaper(self) -> bool: ...
    @property
    def technology(self) -> str | None: ...
    @property
    def colorimetric_intent(self) -> str | None: ...
    @property
    def perceptual_rendering_intent_gamut(self) -> str | None: ...
    @property
    def saturation_rendering_intent_gamut(self) -> str | None: ...
    @property
    def red_colorant(self) -> _Tuple2x3f | None: ...
    @property
    def green_colorant(self) -> _Tuple2x3f | None: ...
    @property
    def blue_colorant(self) -> _Tuple2x3f | None: ...
    @property
    def red_primary(self) -> _Tuple2x3f | None: ...
    @property
    def green_primary(self) -> _Tuple2x3f | None: ...
    @property
    def blue_primary(self) -> _Tuple2x3f | None: ...
    @property
    def media_white_point_temperature(self) -> float | None: ...
    @property
    def media_white_point(self) -> _Tuple2x3f | None: ...
    @property
    def media_black_point(self) -> _Tuple2x3f | None: ...
    @property
    def luminance(self) -> _Tuple2x3f | None: ...
    @property
    def chromatic_adaptation(self) -> tuple[_Tuple3x3f, _Tuple3x3f] | None: ...
    @property
    def chromaticity(self) -> _Tuple3x3f | None: ...
    @property
    def colorant_table(self) -> list[str] | None: ...
    @property
    def colorant_table_out(self) -> list[str] | None: ...
    @property
    def intent_supported(self) -> dict[int, tuple[bool, bool, bool]] | None: ...
    @property
    def clut(self) -> dict[int, tuple[bool, bool, bool]] | None: ...
    @property
    def icc_measurement_condition(self) -> _IccMeasurementCondition | None: ...
    @property
    def icc_viewing_condition(self) -> _IccViewingCondition | None: ...
    def is_intent_supported(self, intent: int, direction: int, /) -> int: ...

class CmsTransform:
    def apply(self, id_in: CapsuleType, id_out: CapsuleType) -> int: ...

def profile_open(profile: str, /) -> CmsProfile: ...
def profile_frombytes(profile: bytes, /) -> CmsProfile: ...
def profile_tobytes(profile: CmsProfile, /) -> bytes: ...
def buildTransform(
    input_profile: CmsProfile,
    output_profile: CmsProfile,
    in_mode: str,
    out_mode: str,
    rendering_intent: int = 0,
    cms_flags: int = 0,
    /,
) -> CmsTransform: ...
def buildProofTransform(
    input_profile: CmsProfile,
    output_profile: CmsProfile,
    proof_profile: CmsProfile,
    in_mode: str,
    out_mode: str,
    rendering_intent: int = 0,
    proof_intent: int = 0,
    cms_flags: int = 0,
    /,
) -> CmsTransform: ...
def createProfile(
    color_space: Literal["LAB", "XYZ", "sRGB"], color_temp: SupportsFloat = 0.0, /
) -> CmsProfile: ...

if sys.platform == "win32":
    def get_display_profile_win32(handle: int = 0, is_dc: int = 0, /) -> str | None: ...
