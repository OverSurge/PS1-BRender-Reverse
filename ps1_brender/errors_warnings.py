UNSUPPORTED_GAME = "This reversing feature isn't supported on this game."


class ReverseError(Exception):
    def __init__(self, explanation: str, absolute_file_offset: int = None):
        Exception.__init__(self)
        self.message = f"A reversing error has been encountered at offset {hex(absolute_file_offset)}:\n" \
            if absolute_file_offset is not None else f"A reversing error has been encountered:\n"
        self.message += f"{explanation}\n" \
                        f"If you think this error isn't supposed to happen, you can ask me for help " \
                        f"(contact details in the README)."

    def __str__(self):
        return self.message


class SectionNameError(ReverseError):
    def __init__(self, absolute_file_offset: int, expected: str, found: str):
        super(SectionNameError, self).__init__(
            f"Section codename is either missing or incorrect, expected '{expected}', got '{found}'.",
            absolute_file_offset)


class SectionSizeMismatch(ReverseError):
    def __init__(self, absolute_file_offset: int, name: str, expected: int, found: int):
        super(SectionSizeMismatch, self).__init__(
            f"The {name} section size is different than expected: got {found} instead of {expected}.",
            absolute_file_offset)


class NegativeIndexError(ReverseError):
    CAUSE_VERTEX = "vertex"
    CAUSE_VERTEX_NORMAL = "vertex normal"
    CAUSE_FACE = "face"

    def __init__(self, absolute_file_offset: int, cause: str, value: int, entire):
        super(NegativeIndexError, self).__init__(
            f"A negative {cause} index has been found: {value}. Whole {cause}: {entire}", absolute_file_offset)


class IncompatibleAnimationError(ReverseError):
    def __init__(self, model_count: int, anim_count: int):
        super(IncompatibleAnimationError, self).__init__(
            f"This model has {model_count} vertex groups, but "
            f"this animation is designed for models with {anim_count} vertex groups, thus they are incompatible.")


class ZeroRunLengthError(ReverseError):
    def __init__(self, absolute_file_offset: int):
        super(ZeroRunLengthError, self).__init__("A zero run length has been found while decompressing.",
                                                 absolute_file_offset)


class TexturesWarning(ReverseError):
    def __init__(self, absolute_file_offset: int, n_textures: int, n_rows: int):
        super(TexturesWarning, self).__init__(
            f"Too much textures ({n_textures}), or incorrect row count ({n_rows}).\n"
            f"It is most probably caused by an inaccuracy in my reverse engineering of the textures format.",
            absolute_file_offset)


class Models3DWarning(ReverseError):
    def __init__(self, absolute_file_offset: int, n_vertices: int, n_faces: int):
        super(Models3DWarning, self).__init__(
            f"Too many vertices or faces ({n_vertices} vertices, {n_faces} faces). It is most probably caused by an "
            f"inaccuracy in my reverse engineering of the models format.\nIf you think that the amounts are coherent, "
            f"you can silence this warning with the --ignore-warnings commandline option.", absolute_file_offset)


class AnimationsWarning(ReverseError):
    def __init__(self, absolute_file_offset: int, n_total_frames: int):
        super(AnimationsWarning, self).__init__(
            f"Too much frames in animation (or no frame): {n_total_frames} frames.\n"
            f"It is most probably caused by an inaccuracy in my reverse engineering of the textures format.",
            absolute_file_offset)
