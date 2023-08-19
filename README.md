# Tibbers
A Discord bot made to detect insults/toxicity using Pytorch

## What Does It Do and How?
The bot reads every message sent on the server and it responds to a message if the sender sent a toxic, severely toxic, threatening, obscene, hateful or insulting message. It responds randomly using 4 different APIs:
1. [Bored API](https://www.boredapi.com/api/activity/)
   This API is used to give something to do to the sender as if the hateful message was out of boredom.
2. [Evil Insult](https://evilinsult.com/generate_insult.php?lang=en&type=json)
   This API insults back in a clever/funny way.
3. [The Motivate 365 API](https://api.themotivate365.com/stoic-quote)
   This API sends back a stoic quote in order to humble the sender.
4. [Advice Slip JSON API](https://api.adviceslip.com/advice)
   This API sends back advice that hopefully helps the sender to calm their own nerves down.

- The deep learning model was trained using the data from [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge).


## Model
```
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
```
