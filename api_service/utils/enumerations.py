from enum import Enum


class DestroyTimeEnum(Enum):
    DEFAULT = "DEFAULT"
    AFTER_READ = "AFTER_READ"
    TEN_MINUTES = "TEN_MINUTES"
    ONE_HOUR = "ONE_HOUR"
    ONE_DAY = "ONE_DAY"
    ONEW_WEEK = "ONE_WEEK"
