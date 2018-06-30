from io import BytesIO
# import torch
from PIL import Image
from django.shortcuts import render
from pathlib import Path
import os
import numpy as np
import time
# from torchvision import transforms

# from densenet.model import predict

from dr_unet.test_ma import predict_ma
from dr_unet.test_he import predict_he
from dr_unet.test_se import predict_se
from dr_unet.test_ex import predict_ex

def index(request):
    template_name = 'index.html'
    if request.method == 'POST':
        if request.POST.get("upload"):
            images_files = request.FILES.getlist('images')
            if not images_files:
                return render(request, template_name, {'status': "no_image"})
            images = []
            for img in images_files:
                img_name = img.name
                image = Image.open(BytesIO(img.read()))
                images.append(image)
            for file in os.listdir("static/images/"):
                os.remove("static/images/"+file)
            images[0].save("static/images/saved.jpg","JPEG")

            score_csv = np.loadtxt("static/score/scores.csv", delimiter=",", dtype='str')
            # print(score_csv[0][0])
            for idx in range(143):
                if score_csv[idx][0] == img_name:
                    pred = score_csv[idx][1]
                    break
            grade_file = open("static/images/grade", "w")
            grade_file.write(pred)
            grade_file.close()
            time.sleep(5) 

            # pred_out = predict_ma(images[0])
            # pred_out.save("static/images/predicted_ma.jpg", "JPEG")
            # pred_out = predict_he(images[0])
            # pred_out.save("static/images/predicted_he.jpg", "JPEG")
            # pred_out = predict_se(images[0])
            # pred_out.save("static/images/predicted_se.jpg", "JPEG")
            # pred_out = predict_ex(images[0])
            # pred_out.save("static/images/predicted_ex.jpg", "JPEG")

            context = {'status': "uploaded", 'ma_converted': "false", 'he_converted': "false", 'se_converted': "false", 'ex_converted': "false", 'preds': pred}
            return render(request, template_name, context)
        elif request.POST.get("convert_ma"):
            grade_file = open("static/images/grade", "r")
            pred = grade_file.readline()
            grade_file.close()
            my_file = Path("static/images/saved.jpg")
            if my_file.is_file():
                input_im = Image.open("static/images/saved.jpg")
            else:
                return render(request, template_name, {'status': "no_image"})
            out_im = predict_ma(input_im)
            out_im.save("static/images/predicted_ma.jpg", "JPEG")
            context = {'status': "converting", 'ma_converted': "true", 'preds': pred}
            return render(request, template_name, context)
        elif request.POST.get("convert_he"):
            grade_file = open("static/images/grade", "r")
            pred = grade_file.readline()
            grade_file.close()
            my_file = Path("static/images/saved.jpg")
            if my_file.is_file():
                input_im = Image.open("static/images/saved.jpg")
            else:
                return render(request, template_name, {'status': "no_image"})
            out_im = predict_he(input_im)
            out_im.save("static/images/predicted_he.jpg", "JPEG")
            context = {'status': "converting", 'he_converted': "true", 'preds': pred}
            return render(request, template_name, context)
        elif request.POST.get("convert_se"):
            grade_file = open("static/images/grade", "r")
            pred = grade_file.readline()
            grade_file.close()
            my_file = Path("static/images/saved.jpg")
            if my_file.is_file():
                input_im = Image.open("static/images/saved.jpg")
            else:
                return render(request, template_name, {'status': "no_image"})
            out_im = predict_se(input_im)
            out_im.save("static/images/predicted_se.jpg", "JPEG")
            context = {'status': "converting", 'se_converted': "true", 'preds': pred}
            return render(request, template_name, context)
        elif request.POST.get("convert_ex"):
            grade_file = open("static/images/grade", "r")
            pred = grade_file.readline()
            grade_file.close()
            my_file = Path("static/images/saved.jpg")
            if my_file.is_file():
                input_im = Image.open("static/images/saved.jpg")
            else:
                return render(request, template_name, {'status': "no_image"})
            out_im = predict_ex(input_im)
            out_im.save("static/images/predicted_ex.jpg", "JPEG")
            context = {'status': "converting", 'ex_converted': "true", 'preds': pred}
            return render(request, template_name, context)
        # elif request.POST.get("predict_dg"):
        #     my_file = Path("static/images/xray.jpg")
        #     if my_file.is_file():
        #         input_im = Image.open("static/images/xray.jpg")
        #     else:
        #         return render(request, template_name, {'status': "no_image"})
        #     image = input_im.convert('RGB')
        #     output, preds = predict(image)
        #     context = {'output': round(output.numpy()[0] * 100, 2),
        #                'preds': "Normal" if preds.numpy()[0] == 0 else "Abnormal",
        #                'status': "success"}
        #     return render(request, template_name, context)

    return render(request, template_name)