import logging
import os
import torch
import telebot
from PIL import Image
from torchvision import transforms
import torch.nn.functional as F
from torchvision.models import resnet50
# other model: densenet121, vgg16

# Create the Telegram bot
bot = telebot.TeleBot('6135118251:AAETo4ZYabDbNDeUESmCEdvQO7FwzjAcATE')
num_classes = 9

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

# Initialize the model with pre-trained weights
model = resnet50(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, num_classes) # the number of classes

model.load_state_dict(
    torch.load('/Users/phisoft/PycharmProjects/Malaysia-Traffic-sign-Classification-Chatbot-using-Resnet-50-CNN/pretrained_model.pth', map_location=torch.device('cpu')))
model.eval()

# Define the device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Define the label mapping
label_mapping = {
    0: 'Diverge',
    1: 'Give way',
    2: 'Height 5 Meters',
    3: 'Hump',
    4: 'No stopping',
    5: 'Obstruction',
    6: 'Speed Limit 80',
    7: 'Traffic Light',
    8: 'U-turn',
}

# Define the image preprocessing steps
transform = transforms.Compose([
    transforms.Resize(224),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(degrees=(-15,15)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


@bot.message_handler(commands=['start'])
def starting(message):
    bot.reply_to(message, "Hello, what can i help you ?")
    bot.send_message(
        message.chat.id, "Please choose one :\n"
                         "/Signboard - Road Sign information\n"
                         "/help - Show the instructions")


# Reply to
@bot.message_handler(commands=['Signboard'])
def greet(message):
    bot.reply_to(message, "Please noted that picture must be cropped following the traffic sign corner size")
    bot.reply_to(message, "Please send a photo of traffic signs...")


# /help instructions for user
@bot.message_handler(commands=['help'])
def hello(message):
    bot.send_message(
        message.chat.id,
        "🛑 How to Use This Bot to Identify a Traffic Sign 🛑\n\n"
        "Please follow these simple steps:\n\n"
        "1️⃣ *Capture a clear photo* of the traffic sign you'd like me to identify.\n\n"
        "2️⃣ *Crop the image* so that the traffic sign is clearly visible and centered in the frame. Avoid background distractions if possible.\n\n"
        "3️⃣ *Send the photo here* in this chat. I will analyze it and provide you with the sign's type and relevant information.\n\n"
        "📌 Tip: For best results, make sure the photo is taken in good lighting and not blurry.\n\n"
        "Once you're ready, just upload the image, and I’ll take care of the rest! 😊"
    )


@bot.message_handler(func=lambda message: True, content_types=['text'])
def errormessage(message):
    text = message.text.lower()

    if text in ['hello', 'hey']:
        bot.send_message(message.chat.id, "Hello! Hope you're having a great day. Please send a photo of a traffic sign you'd like me to analyze.")
    elif text in ['hi', 'hai']:
        bot.send_message(message.chat.id, "Hi there! I'm here to help you identify traffic signs. Please send a photo.")
    elif text in ['bye', 'goodbye', 'good bye']:
        bot.send_message(message.chat.id, "Goodbye! Thank you for using the bot. Stay safe and see you again soon.")
    elif text in ['help', 'helps']:
        bot.send_message(message.chat.id, "I'm here to identify traffic signs for you. Just send a clear and cropped image of the road sign, and I'll take care of the rest.")
    elif text.startswith("/"):
        bot.send_message(message.chat.id, "Sorry, I didn't recognize that command. Please type /help to see available options.")
    else:
        bot.send_message(message.chat.id, "I'm not sure what you mean. Please send a photo of a traffic sign or type /help for instructions.")

# Handle all other messages.
@bot.message_handler(func=lambda message: True, content_types=['audio', 'voice', 'video', 'document',
                                                               'location', 'contact', 'sticker', ])
def default_command(message):
    bot.reply_to(message, 'This chatbot only accept image, please send a picture')


# Handle the "/classify" command
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, 'picture is scan...')

    # Download the image sent by the user
    image_info = bot.get_file(message.photo[-1].file_id)
    image_file = bot.download_file(image_info.file_path)

    # Check the file type
    if image_info.file_path.endswith('.heic'):
        bot.reply_to(message, "Sorry, HEIC files are not supported.")
        return

    # Save the image locally
    image_path = 'user_image.jpg'
    with open(image_path, 'wb') as file:
        file.write(image_file)

    # Preprocess the image
    input_image = Image.open(image_path)
    input_tensor = transform(input_image).unsqueeze(0)

    # Inference
    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = F.softmax(outputs, dim=1)
        confidence, predicted_idx = torch.max(probabilities, 1)
        predicted_label_idx = predicted_idx.item()
        accuracy = confidence.item() * 100

    predicted_label = label_mapping.get(predicted_label_idx, 'Unknown')

    # Send result photo with prediction and accuracy
    with open(image_path, 'rb') as photo:
        bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=f"🔍 *Prediction Result*\n"
                    f"🚦 Traffic Sign: *{predicted_label}*\n"
                    f"🎯 Accuracy: *{accuracy:.2f}%*",
            parse_mode="Markdown"
        )

    if accuracy < 50:
        bot.send_message(message.chat.id,
                         "⚠️ I'm not very confident about this prediction. "
                         "Please try sending a clearer or more cropped image for better accuracy.")
    elif accuracy > 50:
        # Condition check
        if predicted_label_idx == 0:
            bot.reply_to(message,
                         "Hey there! 👋 This sign usually appears above the road or near junctions where lanes split. It's giving drivers a heads-up about which lane to take. 🚗")
            bot.send_message(message.chat.id, "👉 What you should do:\n"
                                              "• Pick the correct lane early based on your direction.\n"
                                              "• Avoid sudden lane changes — stay safe!")

        elif predicted_label_idx == 1:
            bot.reply_to(message,
                         "This is a *Yield* sign! ⛔ It’s a red triangle pointing downward — it means you need to slow down and be ready to give way.")
            bot.send_message(message.chat.id, "👉 What you should do:\n"
                                              "• Slow down.\n"
                                              "• Let other vehicles pass if needed before you go.")

        elif predicted_label_idx == 2:
            bot.reply_to(message,
                         "Whoa! 🚧 This sign means there's a height restriction ahead — 5 meters max. Usually found near tunnels, bridges, or overhead barriers.")
            bot.send_message(message.chat.id, "👉 What you should do:\n"
                                              "• Make sure your vehicle isn’t taller than 5m.\n"
                                              "• If it is — take another route to avoid any bumps (literally!).")

        elif predicted_label_idx == 3:
            bot.reply_to(message, "Heads up! 🛑 That’s a speed bump warning sign — it means a road hump is coming up.")
            bot.send_message(message.chat.id, "👉 What you should do:\n"
                                              "• Slow down.\n"
                                              "• Drive over it gently to protect your vehicle and passengers.")

        elif predicted_label_idx == 4:
            bot.reply_to(message,
                         "Oops — no stopping here! 🚫 This sign means you're not allowed to stop your car in that zone, not even for a second.")
            bot.send_message(message.chat.id, "👉 What you should do:\n"
                                              "• Keep driving — stopping could block traffic or cause danger.")

        elif predicted_label_idx == 5:
            bot.reply_to(message,
                         "Caution! ⚠️ That’s an obstruction warning sign. Something might be in your lane ahead, like a rock or fallen tree.")
            bot.send_message(message.chat.id, "👉 What you should do:\n"
                                              "• Stay alert and slow down.\n"
                                              "• Be ready to steer around safely.")

        elif predicted_label_idx == 6:
            bot.reply_to(message, "Zoom zoom... but not too fast! 🏁 This sign means the speed limit is 80 km/h.🚗")
            bot.send_message(message.chat.id, "👉 What you should do:\n"
                                              "• Keep your speed at or below 80 km/h — safety first!")

        elif predicted_label_idx == 7:
            bot.reply_to(message,
                         "🚦 Traffic light ahead! This sign is telling you to watch out for signal lights controlling the intersection.")
            bot.send_message(message.chat.id, "👉 What you should do:\n"
                                              "• Start slowing down.\n"
                                              "• Obey the lights — red means stop, green means go!")

        elif predicted_label_idx == 8:
            bot.reply_to(message, "Making a U-turn? 🔄 This sign says you're allowed to make one here.")
            bot.send_message(message.chat.id, "👉 What you should do:\n"
                                              "• Use the correct lane.\n"
                                              "• Signal, wait for a safe gap, then make your turn carefully.")
    # Delete the local image file
    os.remove(image_path)


# Start the bot
bot.polling()