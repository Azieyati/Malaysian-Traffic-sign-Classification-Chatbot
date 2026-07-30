# Malaysian Road Sign Recognition Chatbot (DRIBIE)

A Telegram chatbot powered by ResNet-50 CNN that classifies Malaysian traffic signs and provides real-time explanations to drivers.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-ee4c2c?logo=pytorch&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram&logoColor=white)
![ResNet](https://img.shields.io/badge/Model-ResNet--50-success)
![Accuracy](https://img.shields.io/badge/Accuracy-100%25-brightgreen)

---

## Project Overview

Traffic signs provide essential information about road conditions while driving or walking. Misunderstanding them can lead to accidents, particularly for tourists or international students unfamiliar with Malaysian road signs.

**DRIBIE** is a Telegram chatbot that detects and classifies Malaysian traffic signs using a Convolutional Neural Network (CNN) built with PyTorch. Users send an image of a traffic sign, and the bot returns:

- The type of traffic sign detected
- A confidence score
- A detailed explanation of the sign's meaning
- Actionable instructions for the driver

The system achieves over 90% recognition accuracy and is accessible via Telegram with no additional software or hardware required.

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
| Preprocessing | Resize (224x224), Random Flip, Random Rotation, Normalization |
| Number of Classes | 9 Malaysian traffic sign categories |

### Model Architecture

- **Base Model:** ResNet-50 (pre-trained on ImageNet)
- **Custom Head:** Fully connected layer mapping 2048 features to 9 classes
- **Inference:** Softmax for probability distribution, argmax for label prediction

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

## Features

- **Image Classification** — Send a photo of a traffic sign and receive instant recognition
- **Detailed Explanations** — Understand what each sign means and how to respond
- **Confidence Scoring** — View the model's confidence level for each prediction
- **Low Confidence Warnings** — Get notified if image quality is insufficient
- **Natural Conversation** — Responds to greetings and common commands
- **Help System** — Built-in help command with usage instructions

---

## Installation

### Prerequisites

- Python 3.8 or higher
- A Telegram Bot Token (from [@BotFather](https://t.me/BotFather))

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/Azieyati/Malaysian-Traffic-sign-Classification-Chatbot.git
   cd Malaysian-Traffic-sign-Classification-Chatbot
   ```

2. **Install dependencies**

   ```bash
   pip install torch torchvision pyTelegramBotAPI Pillow
   ```

3. **Configure your bot token**

   Open `main.py` and replace the token with your own:

   ```python
   bot = telebot.TeleBot('YOUR_BOT_TOKEN_HERE')
   ```

4. **Run the bot**

   ```bash
   python main.py
   ```

---

## Usage

1. Start a chat with the bot on Telegram
2. Send `/start` to see available commands
3. Send `/Signboard` to begin sign recognition mode
4. Upload a cropped photo of a traffic sign
5. Receive the prediction with sign type, accuracy, and explanation

### Bot Commands

| Command | Description |
|---|---|
| `/start` | Start the bot and see options |
| `/Signboard` | Begin traffic sign recognition |
| `/help` | Show usage instructions |

---

## Model Performance

### Confusion Matrix

![Confusion Matrix](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/4454e4b9-d0db-4da6-bf48-9f8a8c7b5f52)

![Confusion Matrix 2](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/a2f4466f-1daa-4a3b-833d-c04ba4d3836e)

```
Accuracy = correct_predictions / total_samples
Accuracy = 95/95 x 100 = 100%
```

### Model Comparison

![Model Comparison](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/bbb1fcae-195a-432f-8346-7e3f412d8f65)

### Real-World Image Results

![Real-World Results](https://github.com/Azieyati/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/assets/156404474/c6d3c6e8-9e52-49db-8bb1-fc473474d391)

---

## Project Structure

```
Malaysian-Traffic-sign-Classification-Chatbot/
├── main.py                 # Telegram bot entry point
├── pretrained_model.pth    # Pre-trained ResNet-50 weights
├── df.png                  # Data flow diagram
└── README.md               # Project documentation
```

---

## Objectives

1. To identify the requirements for developing a road sign recognition chatbot.
2. To develop a road sign recognition chatbot for Malaysian road signs.
3. To test the performance of the chatbot using quantitative and qualitative methods.

---

## Target Users

### Newbie Drivers
Individuals who have recently obtained their driver's license or have limited driving experience. They may lack confidence and knowledge in various aspects of driving, including road rules, traffic signs, and safe driving practices.

### Tourists Who Drive in Malaysia
Tourists who are studying or visiting Malaysia and choose to explore the country by driving. They may be unfamiliar with Malaysian roads, traffic regulations, and local driving customs.

---

## Project Significance

This project helps newbie drivers better understand the meaning of each traffic sign in an interactive way. It potentially:

- Enhances road safety
- Improves driver awareness
- Contributes to a more efficient traffic system
- Educates drivers who are less experienced or unfamiliar with certain traffic signs
- Provides actionable explanations to empower safer driving decisions

By leveraging computer vision and machine learning, this project addresses crucial aspects of traffic management, aiming to create safer, more informed, and more efficient road systems.

---

## Conclusion

- The comparative analysis of three CNN models — ResNet-50, DenseNet, and VGG-16 — tested on real-world images with varying brightness, distance, and quality, reveals that ResNet-50 is the most suitable model for this project.
- Comparison between public and custom datasets shows the custom dataset produces superior results.
- The DRIBIE chatbot, powered by the ResNet-50 deep learning model, achieves 100% accuracy across near and far objects, demonstrating the accuracy and versatility of the model.

---

&copy; 2026 Azieyati. All rights reserved.
