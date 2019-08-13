from enum import Enum,EnumMeta

class ChoiceEnumMeta(EnumMeta):
    def __iter__(self):
        return ((tag.name,tag.value) for tag in super().__iter__())


class ChoiceEnum(Enum,metaclass = ChoiceEnumMeta):
    pass

class LikeChoice(ChoiceEnum):
    like = "1"
    unlike = "0"

class CollectChoice(ChoiceEnum):
    collect = "1"
    un_collect = "0"

class FollowChoice(ChoiceEnum):
    follow = "1"
    un_follow = "0"

class GenderChoice(ChoiceEnum):
    boy = "1"
    girl = "0"

class IsMaster(ChoiceEnum):
    isMaster = "1"
    notMaster = "0"

class ActivityOrTrainChoice(ChoiceEnum):
    activity = "1"
    train = "0"