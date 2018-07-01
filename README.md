# Diabetic Retinopathy Clinical Support Assistant
Source code of Web App for demo of Diabetic Retinopathy: Segmentation and Grading

## Idea
Diabetic Retinopathy is the most prevalent cause of avoidable vision impairment, mainly affecting working age population in the world. Recent research has given a better understanding of requirement in clinical eye care practice to identify better and cheaper ways of identification, management, diagnosis and treatment of retinal disease.
Computer-aided disease diagnosis in retinal image analysis could ease mass screening of population with diabetes mellitus and help clinicians in utilizing their time more efficiently.
We have trained models to segment four distinct lesions from retinal images to aid the clinician in disease diagnosis. We have also trained a classifier to grade the retinal images according to the severity of Diabetic Retinopathy.

## Product
We trained 4 distinct binary models employing UNet architecture for the segmentation of 4 kinds of lesions, and a ResNet model for
disease grading. We developed a Django webserver with a basic user interface to upload and test retinal images on our models. The Django site was hosted on our workstation.

## Model
Refer to: [Diabetic Retinopathy: Segmentation, Grading and Localization](https://github.com/apopli/diabetic-retinopathy)

## Dependencies
* Tensorflow
* Django
* Pillow
* OpenCV
* SciPy
* NumPy

## How to run this project
* Install the dependencies.
* Run the server with `python manage.py runserver`

#### View demo video: https://apopli.github.io/dr_demo.mp4
