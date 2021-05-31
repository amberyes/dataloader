import torch

import torchvision.models as models

# pretrained=True就可以使用预训练的模型

net = models.squeezenet1_1(pretrained=False)

pthfile = r'snapshots/Epoch0.pth'

net.load_state_dict(torch.load(pthfile))

print(net)