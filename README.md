# Tibbers
A Discord bot made to detect insults/toxicity using Pytorch

## Model
================================================================
               Kernel Shape Output Shape      Params   Mult-Adds
Layer                                                           
0_embed_layer  [64, 243146]     [64, 64]  15.561344M  15.561344M
1_lstm                    -     [64, 40]      13.76k      13.44k
2_tanh                    -     [64, 40]           -           -
3_linear_1         [40, 32]     [64, 32]      1.312k       1.28k
4_relu                    -     [64, 32]           -           -
5_linear_2         [32, 16]     [64, 16]       528.0       512.0
6_relu                    -     [64, 16]           -           -
7_linear_3          [16, 6]      [64, 6]       102.0        96.0
8_sigmoid                 -      [64, 6]           -           -
----------------------------------------------------------------
                          Totals
Total params          15.577046M
Trainable params      15.577046M
Non-trainable params         0.0
Mult-Adds             15.576672M
================================================================
               Kernel Shape Output Shape      Params   Mult-Adds
Layer                                                           
0_embed_layer  [64, 243146]     [64, 64]  15561344.0  15561344.0
1_lstm                    -     [64, 40]     13760.0     13440.0
2_tanh                    -     [64, 40]         NaN         NaN
3_linear_1         [40, 32]     [64, 32]      1312.0      1280.0
4_relu                    -     [64, 32]         NaN         NaN
5_linear_2         [32, 16]     [64, 16]       528.0       512.0
6_relu                    -     [64, 16]         NaN         NaN
7_linear_3          [16, 6]      [64, 6]       102.0        96.0
8_sigmoid                 -      [64, 6]         NaN         NaN
================================================================
| epoch   0 |  112.689 seconds elapsed | accuracy    0.902 | loss    0.001
| epoch   1 |  109.055 seconds elapsed | accuracy    0.908 | loss    0.001
| epoch   2 |  113.333 seconds elapsed | accuracy    0.913 | loss    0.001
| epoch   3 |  108.886 seconds elapsed | accuracy    0.916 | loss    0.001
| epoch   4 |  110.584 seconds elapsed | accuracy    0.917 | loss    0.001

