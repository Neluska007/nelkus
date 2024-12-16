### GUI imports
from guizero import *
from main import *

### GUI functions
def my_first_gui_function():
    text_welcome.value = "Ahoj, můj nejdražší uživateli."
    try:
            weight=float(txtbox_weight.value)
    except:
            text_cml.value = "Musíš vložit číslo"
            return
    bmr=weight*24.2
    activityfactor=float(txtbox_af.value)
    cml=bmr*activityfactor
    cmlrounded= round(cml, 1)
    text_cml.value =cmlrounded

### GUI App
app = App(title="My App", width=775, height=650)

## Window 1
window1 = Box(app, visible=True)

# Welcome text
text_welcome = Text(window1, text=(f"Hi, user!"))

# Input activity factor
text_af = Text(
    window1,
    text=(
        "        Please enter your activity factor for today:"
    )
)
txtbox_af = TextBox(window1)

# Input weight
text_weight = Text(
    window1,
    text=(f"Zadej svoji váhu (kg):")
)
txtbox_weight = TextBox(window1)

# Output calorie maintenance level
text_cml = Text(window1, text ="")

button = PushButton(window1, command=my_first_gui_function)
# Display an image
image_widget = Picture(
    window1,
    image="resources/images/calculating_cml.png",
    width=680,
    height=480,
    align="bottom"
)



app.display()

