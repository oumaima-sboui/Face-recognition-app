from flask import Flask, request, render_template
import face_recognition as fr
import cv2
import numpy as np
import os
import json

app = Flask(__name__)

path = "./train/"

known_names = []
known_name_encodings = []
data ={}
images = os.listdir(path)
for _ in images:
    image = fr.load_image_file(path + _)
    image_path = path + _
    encoding = fr.face_encodings(image)[0]

    known_name_encodings.append(encoding)
    known_names.append(os.path.splitext(os.path.basename(image_path))[0].capitalize())

print(known_names)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get uploaded file
        uploaded_file = request.files['file']

        # Save the uploaded file to disk
        file_path = './test/' + uploaded_file.filename
        uploaded_file.save(file_path)

        # Load the image from disk
        image = cv2.imread(file_path)

        # Detect face locations and encodings
        face_locations = fr.face_locations(image)
        face_encodings = fr.face_encodings(image, face_locations)

        # Recognize faces
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = fr.compare_faces(known_name_encodings, face_encoding)
            name = ""

            face_distances = fr.face_distance(known_name_encodings, face_encoding)
            best_match = np.argmin(face_distances)

            if matches[best_match]:
                name = known_names[best_match]

            cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(image, (left, bottom - 15), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            reco = {str(file_path): name}
            data.update(reco)
        with open('data.json', 'w') as mon_fichier:
            json.dump(data, mon_fichier)
        # Save output image
        output_path = './static/output.jpg'
        cv2.imwrite(output_path, image)

        # Render result page with output image
        return render_template('result.html', image_url="./output.jpg")

    # Render upload page with file input form
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
