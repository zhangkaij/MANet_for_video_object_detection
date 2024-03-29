# --------------------------------------------------------
# Fully Motion-Aware Network for Video Object Detection
# Extend FGFA by adding instance-level aggregation and motion pattern reasoning
# Modified by Shiyao Wang
# --------------------------------------------------------

import os
import sys
os.environ['PYTHONUNBUFFERED'] = '1'
os.environ['MXNET_CUDNN_AUTOTUNE_DEFAULT'] = '0'
os.environ['MXNET_ENABLE_GPU_P2P'] = '0'
this_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(this_dir, '..', '..', 'manet_rfcn'))

import train_end2end
import test

if __name__ == "__main__":
    #train_end2end.main()
    test.main()




