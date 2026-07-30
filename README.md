# Malaysian Road Sign Recognition Chatbot (DRIBIE)

A Telegram chatbot powered by ResNet-50 CNN that classifies Malaysian traffic signs and provides real-time explanations to drivers.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-ee4c2c?logo=pytorch&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram&logoColor=white)
![ResNet](https://img.shields.io/badge/Model-ResNet--50-success)
![Accuracy](https://img.shields.io/badge/Accuracy-100%25-brightgreen)

---

## Project Overview

**DRIBIE** is a Telegram chatbot that detects and classifies Malaysian traffic signs using a Convolutional Neural Network (CNN) built with PyTorch. Users send an image of a traffic sign, and the bot returns the sign type, confidence score, explanation, and actionable instructions. The system achieves over 90% recognition accuracy with no additional software or hardware required.

---

## Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.8+ |
| Deep Learning | PyTorch, torchvision |
| Model Architecture | ResNet-50 (CNN) with custom classifier head |
| Models Evaluated | ResNet-50, DenseNet121, VGG-16 |
| Chatbot Platform | Telegram Bot API (pyTelegramBotAPI) |
| Image Processing | Pillow (PIL) |
| Number of Classes | 9 Malaysian traffic sign categories |

### Supported Traffic Signs

| Label | Sign |
|---|---|
| 0 | Diverge |
| 1 | Give Way |
| 2 | Height 5 Meters |
| 3 | Hump |
| 4 | No Stopping |
| 5 | Obstruction |
| 6 | Speed Limit 80 |
| 7 | Traffic Light |
| 8 | U-turn |

---

## Installation

### Prerequisites

- Python 3.8 or higher
- A Telegram Bot Token (from [@BotFather](https://t.me/BotFather))

### Steps

```bash
git clone https://github.com/Azieyati/Malaysian-Traffic-sign-Classification-Chatbot.git
cd Malaysian-Traffic-sign-Classification-Chatbot
pip install torch torchvision pyTelegramBotAPI Pillow
```

Open `main.py` and replace the token:

```python
bot = telebot.TeleBot('YOUR_BOT_TOKEN_HERE')
```

Run the bot:

```bash
python main.py
```

---

## Usage

Send `/start` to begin, then `/Signboard` to start sign recognition. Upload a cropped photo of a traffic sign to receive the prediction.

| Command | Description |
|---|---|
| `/start` | Start the bot and see options |
| `/Signboard` | Begin traffic sign recognition |
| `/help` | Show usage instructions |

---

## Test Results

### Test Case 1: Traffic Sign Recognition

Successfully recognized traffic light signs and provided real-time guidance. Demonstrated high accuracy and responsiveness in realistic traffic scenarios.

<img width="355" height="424" alt="testcase1" src="https://github.com/user-attachments/assets/88866bf3-44eb-41e9-bd8b-4a9595942755" />



### Test Case 2: Uncertain Prediction Handling

Provided traffic sign predictions with confidence scores and guided users to improve input when accuracy was low, ensuring a reliable experience.

<img width="355" height="424" alt="testcase2" src="https://github.com/user-attachments/assets/3ead58dc-066d-4822-aad0-d40a4f0b8e38" />


### Test Case 3: Handling Noisy or Partial Images

Successfully predicted traffic signs from noisy or partially captured images, returning confidence scores (e.g., Speed Limit 80 - Accuracy: 71.03%) with friendly guidance.

<img width="355" height="424" alt="testcase3" src="https://github.com/user-attachments/assets/fa472136-6335-44c9-9469-e8b50a68a000" />


---

## Model Performance

### Confusion Matrix

![Confusion Matrix](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/4454e4b9-d0db-4da6-bf48-9f8a8c7b5f52)
![Confusion Matrix 2](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/a2f4466f-1daa-4a3b-833d-c04ba4d3836e)

```
Accuracy = 95/95 x 100 = 100%
```

### Model Comparison

![Model Comparison](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/bbb1fcae-195a-432f-8346-7e3f412d8f65)

### Real-World Image Results

![Real-World Results](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/c6d3c6e8-9e52-49db-8bb1-fc473474d391)

---

## Conclusion

ResNet-50 outperformed DenseNet and VGG-16 in real-world testing, and the custom dataset produced superior results compared to public datasets. The DRIBIE chatbot achieves 100% accuracy across near and far objects, demonstrating the model's accuracy and versatility.

---

## License

This project is licensed under the terms specified in the [LICENCE](LICENCE) file.

- **Attribution Required** — Credit must be given to the original author (Azieyati) with a link back to the repository.
- **No Modifications** — The source code must remain unaltered.
- **Non-Commercial** — This software may not be used for commercial purposes.

---

&copy; 2026 Azieyati. All rights reserved.
