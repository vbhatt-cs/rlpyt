
import numpy as np

from rlpyt.replays.non_sequence.n_step import NStepReturnBuffer
from rlpyt.replays.frame import FrameBufferMixin
from rlpyt.replays.non_sequence.uniform import UniformReplay
from rlpyt.replays.non_sequence.prioritized import PrioritizedReplay


class NStepFrameBuffer(FrameBufferMixin, NStepReturnBuffer):

    def extract_observation(self, T_idxs, B_idxs):
        """Frames are returned OLDEST to NEWEST."""
        return np.stack([self.samples_frames[t:t + self.n_frames, b]
            for t, b in zip(T_idxs, B_idxs)], axis=0)  # [B,C,H,W]


class UniformReplayFrameBuffer(UniformReplay, NStepFrameBuffer):

    pass


class PrioritizedReplayFrameBuffer(PrioritizedReplay, NStepFrameBuffer):

    pass