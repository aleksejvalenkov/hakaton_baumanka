import torch
import torchvision
import numpy as np
import cv2
from neural_net.src.utils import draw_keypoints, check_people
from PIL import Image
from torchvision.transforms import transforms as transforms

class Net:
    def __init__(self) -> None:
        

        # transform to convert the image to tensor
        self.transform = transforms.Compose([
            transforms.ToTensor()
        ])

        # initialize the model
        self.model = torchvision.models.detection.keypointrcnn_resnet50_fpn(pretrained=True,
                                                                    num_keypoints=17)
        # set the computation device
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # load the modle on to the computation device and set to eval mode
        self.model.to(self.device).eval()

        self.image_path = "/home/alex/Documents/hackaton_baumanka/image.jpeg"
        # self.image_path = "hakaton_baumanka/neural_net/input/image4.jpg"

    def detect(self):
        image = Image.open(self.image_path).convert('RGB')
        # NumPy copy of the image for OpenCV functions
        orig_numpy = np.array(image, dtype=np.float32)
        # convert the NumPy image to OpenCV BGR format
        orig_numpy = cv2.cvtColor(orig_numpy, cv2.COLOR_RGB2BGR) / 255.
        # transform the image
        image = self.transform(image)
        # add a batch dimension
        image = image.unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(image)
        output_image = draw_keypoints(outputs, orig_numpy)

        people = check_people(outputs)

        return output_image ,  people
    
        # # visualize the image
        # cv2.imshow('Keypoint image', output_image)
        # cv2.waitKey(0)

        # # set the save path
        # save_path = f"../outputs/{args['input'].split('/')[-1].split('.')[0]}.jpg"
        # cv2.imwrite(save_path, output_image*255.)

