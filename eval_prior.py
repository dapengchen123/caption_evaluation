from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap
import matplotlib.pyplot as plt
import skimage.io as io
import pylab

pylab.rcParams['figure.figsize'] = (10.0, 8.0)
import json
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.3f')

dataDir = '/home/dpchen/workspace/language/code/datasets/coco/raw'
dataDirA = '/home/dpchen/workspace/language/code/COCO_evaldemo/coco_caption_eval'
dataType='val2014'
algName = 'fakecap'
annFile='%s/annotations/captions_%s.json'%(dataDir,dataType)
subtypes=['results', 'evalImgs', 'eval']
[resFile, evalImgsFile, evalFile]= \
['%s/results/captions_%s_%s_%s.json'%(dataDirA,dataType,algName,subtype) for subtype in subtypes]


coco = COCO(annFile)

cocoRes = coco.loadRes(resFile)

cocoEval = COCOEvalCap(coco, cocoRes)

cocoEval.params['image_id'] = cocoRes.getImgIds()

cocoEval.evaluate()


