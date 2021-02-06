
# Project Automated Wardrobe main.py file

from tkinter import *
from PIL import Image, ImageTk
import cv2
import requests
import os
import json
#***********************************************************************
#SpeechRegonition imported modules

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

#*** All Modules imported till here **************************************


checker = True
avoid_repetions_of_cloth = 0


#******************************************** Speech_recog functions Code Here **************************************************

def speak(text , mp3_file_number):
    tts = gTTS(text=text , lang="en")
    filename = "voice" + mp3_file_number + ".mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak("Hey! How are you doing? I am bot and i will be guiding you througout the application",str(0))
speak("Let me brief you about the project idea, We will take your cloths input from your wardrobe and help you to figure out which one to wear today",str(1))
#speak("good",str(1))
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception : " + str(e))

    return said

#get_audio()

#************************* SpeechRecog_ functions ends here *******************************************************************


#****SpeechRecog_ Interaction with the user***************************************************************************************

output = []

speak("Are you an existing user?",str(2))
user_answer1 = get_audio()

speak("Can you please enter your name in the terminal",str(3))
user_name_temp = input("Enter Your name here : ")
user_name = "/" + user_name_temp

prompt_to_user = "Hi " + user_name + "! I am assigned to help you, Do you need my help?"

#THIS IF CONTAINS CODE TO HANDLE THE EXISTING USER
if "yes" in user_answer1:
            speak("hi"+ user_name +"how are you?,I hope you are doing good",str(4))
            speak("I am looking for your digital wardrobe till then please wait!", str(5))
            speak("Thank you for waiting,I found your wardrobe i am good to go",str(6))
            speak("Can you please tell your city name?",str(7))
            user_city = get_audio();

            # API call for the temperature
            # *************************************************************************************
            # Enter your API key here
            temperature_integral_value = -1
            api_key = "e376bdd305b3501ab3ed789f7a1a2787"

            # base_url variable to store url
            base_url = "http://api.openweathermap.org/data/2.5/weather?"

            # Give city name
            city_name = user_city

            # complete_url variable to store
            # complete url address
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            # get method of requests module
            # return response object
            response = requests.get(complete_url)

            # json method of response object
            # convert json format data into
            # python format data
            x = response.json()

            # Now x contains list of nested dictionaries
            # Check the value of "cod" key is equal to
            # "404", means city is found otherwise,
            # city is not found
            if x["cod"] != "404":

                # store the value of "main"
                # key in variable y
                y = x["main"]

                # store the value corresponding
                # to the "temp" key of y
                current_temperature = y["temp"]
                temperature_in_cel = int(current_temperature) - 273

                # store the value corresponding
                # to the "humidity" key of y
                current_humidiy = y["humidity"]

                # print following values
                print("Temperature (Celcius) = " + str(temperature_in_cel))
                print("Humidity = " + str(current_humidiy))

            else:
                print("City Not Found ")


            # ***************************************************************************************************
            # APi call ends Here

            temperature_integral_value = temperature_in_cel

            prompt_to_user2 = "oh" + user_city + "is a beautiful city, I have few friends there"
            speak(prompt_to_user2, str(8))
            speak("Please wait, I am searching your wardrobe",str(9))
            # Deciding the season based on the temperature

            season = "none"

            if 0 <= temperature_integral_value <= 18:
                season = "Exterme Winter"
            elif 19 <= temperature_integral_value <= 24:
                season = "Winter"
            elif 25 <= temperature_integral_value <= 34:
                season = "summer"
            elif 35 <= temperature_integral_value <= 39:
                season = "Extreme Summer"
            else:
                season = "none"

            # season decided

            speak("Oh i got one match for today,It will pop up in new window", str(10))

            speak("Thank you for using my service I hope you have great day ahead",str(11))
            # creating address manually and poping up wear

            if season == "Exterme Winter":
                    if (avoid_repetions_of_cloth > 5):
                        avoid_repetions_of_cloth = 0
                    pic_address = r"C:\Users\saura\PycharmProjects\pythonProjectAutoMated\Images" + user_name + "\sw" + str(0) + ".jpg"
                    avoid_repetions_of_cloth += 1

                    img = cv2.imread(pic_address, -1)
                    cv2.imshow('Your_Wear_For_Today', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    print(pic_address)


            elif season == "Winter":
                    if (avoid_repetions_of_cloth > 5):
                        avoid_repetions_of_cloth = 0
                    pic_address = r"C:\Users\saura\PycharmProjects\pythonProjectAutoMated\Images" + user_name + "\swt" + str(0) + ".jpg"
                    avoid_repetions_of_cloth += 1

                    img = cv2.imread(pic_address, -1)
                    cv2.imshow('image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    print(pic_address)

            elif season == "summer":
                    if (avoid_repetions_of_cloth > 5):
                        avoid_repetions_of_cloth = 0
                    pic_address = r"C:\Users\saura\PycharmProjects\pythonProjectAutoMated\Images" + user_name + r"\fullsv" + str(0) + ".jpg"
                    avoid_repetions_of_cloth += 1

                    img = cv2.imread(pic_address, -1)
                    cv2.imshow('Your_Wear_For_Today', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    print(pic_address)

            elif season == "Extreme Summer":
                    if (avoid_repetions_of_cloth > 5):
                        avoid_repetions_of_cloth = 0
                    pic_address = r"C:\Users\saura\PycharmProjects\pythonProjectAutoMated\Images" + user_name + "\halfsv" + str(0) + ".jpg"
                    avoid_repetions_of_cloth += 1

                    img = cv2.imread(pic_address, -1)
                    cv2.imshow('Your_Wear_For_Today', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                    print(pic_address)

            else:
                    print("Sorry, even I am confused now ")

                    print("\nThank You !")

                # address creation done  and new window opens with todays wear pic





# THIS WILL ELSE WILL HANDEL NEW USERS
else:
    speak("Ok,i will help you to setup your digital wardrobe", str(4))
    speak("Please create a new folder with your name at the provided location, the location is displayed at the terminal",str(5))
    print(r"Location --> C:\Users\saura\PycharmProjects\pythonProjectAutoMated\Images")
    input("Please press enter once you created folder : ")
    speak("Once your folder is created you can proceed further in one of the ways, either I will guide you or you can use our graphical user interface service",str(6))



    speak(prompt_to_user, str(12))

    user_choice_to_use = get_audio()

    if "yes" in user_choice_to_use :
            output.append("Y")
            speak("Ohh you need my help, Ok i will guide you",str(13))
            speak("welcome to the automated wardobe",str(14))
            speak("How would you like to give your cloth input option one manually option two by image capturing", str(15))
            user_answer3 = get_audio()
            if "manually" in user_answer3:
                speak("Ok, please save your cloths photos in your folder", str(16))
                output.append(1)
            else:
                output.append(2)
                speak("Alright webcam will open later and it will click photos one by one",str(17))

            speak("Can you please provide me with following data which is displayed at the terminal", str(18))
            output.append(input("Enter number of sweaters you have"))
            output.append(input("Enter number of sweatshirts  you have"))
            output.append(input("Enter number of full sleeve t-shirt/shirts you have"))
            output.append(input("Enter number of half sleeve t-shirt/shirts you have"))

            speak("Oh same pinch even i have " + output[2] + "sweaters",str(19))
            speak("thank you for providing your data, I am allotting space for your digital wardrobe",str(20))
            output.append(2)
            speak("Can you tell me in which city you are in?",str(21))
            user_city = (get_audio())
            output.append(user_city)
            prompt_to_user3 = "oh" + user_city + "is a beautiful city, I have few friends there"
            speak(prompt_to_user3,str(22))

            speak("Please wait i am reading wheather forecast of " + user_city , str(23))







    else :

                speak("Ohh you don't need my help, Ok new window will pop up and that will guide you,Thanks for listening me ,i am signing off",str(13))


                # **************************************************************************************************************************************
                #                                                        GUI CODE HERE

                def save():
                    text = e1.get() + "\n" + e2.get() + "\n" + e3.get() + "\n" + e4.get() + "\n" + e5.get() + "\n" + e6.get() + "\n" + e7.get() + "\n" + e8.get()
                    with open("test.txt", "w") as f:
                        f.writelines(text)


                def show():
                    with open("test.txt", "r") as f:
                        f.readlines()
                    e1.get(f.seek(0))
                    e2.get(f.seek(1))
                    e3.get(f.seek(2))
                    e4.get(f.seek(3))
                    e5.get(f.seek(4))
                    e6.get(f.seek(5))
                    e7.get(f.seek(6))
                    e8.get(f.seek(7))


                master = Tk(className="Automated wardrobe")
                master.geometry("600x600")
                # master.config(bg='black')
                load = Image.open(r'C:\Users\saura\PycharmProjects\pythonProjectAutoMated\Images\shivaay1.jpeg')
                render = ImageTk.PhotoImage(load)
                img = Label(master, image=render)
                img.place(x=0, y=0)

                Label(master, text="i.Would you like to give your clothes collection?\n(Y/N)", padx=10, pady=10).grid(row=3,
                                                                                                                      column=0)
                Label(master, text="ii.Would you like to give your cloyhes collection?\nManually(1)\nImage processing(2)", padx=10,
                      pady=10).grid(row=4)
                Label(master, text="iii.Enter the number of sweater you have.", padx=10, pady=10).grid(row=5)
                Label(master, text="iv.Enter the number of sweatshirt you have.", padx=10, pady=10).grid(row=6)
                Label(master, text="v.Enter the number of full sleev shirt/t-shirt you have.", padx=10, pady=10).grid(row=7)
                Label(master, text="vi.Enter the number of half sleev shirt/t-shirt you have.", padx=10, pady=10).grid(row=8)
                Label(master, text="vii.Which way you want to take temperature of city.\nManually(1)\nAutomatically(2)", padx=10,
                      pady=10).grid(row=9)
                Label(master,
                      text="If you chose manually please enter temperature of your city \nOR\n If you chose Automatically please enter city name",
                      padx=10, pady=10).grid(row=10)

                e1 = Entry(master)
                e2 = Entry(master)
                e3 = Entry(master)
                e4 = Entry(master)
                e5 = Entry(master)
                e6 = Entry(master)
                e7 = Entry(master)
                e8 = Entry(master)

                e1.grid(row=3, column=1)
                e2.grid(row=4, column=1)
                e3.grid(row=5, column=1)
                e4.grid(row=6, column=1)
                e5.grid(row=7, column=1)
                e6.grid(row=8, column=1)
                e7.grid(row=9, column=1)
                e8.grid(row=10, column=1)

                Button(master, text='Save', command=save, bg="red", font="comicsansms 20 bold").grid(row=12, column=1, sticky=W,
                                                                                                     pady=6)
                Button(master, text='Exit', command=master.destroy, bg="gray", font="comicsansms 20 bold").grid(row=12, column=2,
                                                                                                                sticky=W, pady=6)

                mainloop()

                file = open("test.txt", "r")
                # output=[]
                for line in file:
                    output.append(line.strip())

                print(output)
                file.close()

                # *******************************************************************************************************************************************
                # GUI CODE ENDS HERE




    print("                                                                  WELCOME TO AUTOMATED WARDROBE")
    yes_or_no = output[0]




    if yes_or_no == "Y":
          opt_selection = int(output[1])

          # list for variety of cloths user has
          varierty_of_cloth = ["Sweaters", "Sweatshirts", "Full_Sleeve_T-Shirts/Shirts", "Half_Sleeve_T-Shirts/Shirts"]
          varities = len(varierty_of_cloth)

          # abb for the cloths to save name for addressing
          abb_for_cloth = ["sw" , "swt" , "fullsv" , "halfsv"]

          number_of_sweaters = int (output[2])
          number_of_sweatshirts = int (output[3])
          number_of_fullsleeve_shirts_tshirts = int (output[4])
          number_of_halfsleeve_shirts_tshirts = int (output[5])

          #quantity of each variety clothes
          quantity_of_cloth = [number_of_sweaters, number_of_sweatshirts, number_of_halfsleeve_shirts_tshirts , number_of_fullsleeve_shirts_tshirts]

          if opt_selection == 1:
              # taking cloth input
              print("Please copy and paste the collected pics in the project folder, manually")
              print("Thank You for Your Input \n")

              # cloth input taken

          elif opt_selection == 2:
              print("We will be using your webcam for this process , Thank You !\n")
              #Taking pics from webcam and saving in folder
              # **********************************************************************************************

              for k in range(varities):
                  print("Please click all  "+ varierty_of_cloth[k] + " one by one : ")
                  i = quantity_of_cloth[k]
                  j = -1
                  current_running = True
                  while current_running:
                      j += 1
                      videoCaptureObject = cv2.VideoCapture(0)
                      result = True
                      while (result):
                          ret, frame = videoCaptureObject.read()
                          cv2.imwrite("NewPicture.jpg", frame)
                          result = False
                      videoCaptureObject.release()
                      cv2.destroyAllWindows()

                      img = cv2.imread("NewPicture.jpg", -1)
                      cv2.imshow('Just_clicked', img)
                      cv2.waitKey(0)
                      cv2.destroyAllWindows()

                      img = cv2.imread('NewPicture.jpg', 1)
                      path = r'C:\Users\saura\PycharmProjects\pythonProjectAutoMated\Images' + user_name
                      cv2.imwrite(os.path.join(path, abb_for_cloth[k] + str(j) + '.jpg'), img)
                      cv2.waitKey(0)

                      if j >= i-1:
                          current_running = False

                  #*************************************************************************************************************************
                  # image clicked till here


          # creating address for cloths

          address_to_sweaters = []
          address_to_sweatshits = []
          address_to_full_sleeve = []
          address_to_half_sleeve = []

          for i in range(number_of_sweaters):
              address_to_sweaters.append(i)

          for i in range(number_of_sweatshirts):
              address_to_sweatshits.append(i)

          for i in range(number_of_fullsleeve_shirts_tshirts):
              address_to_full_sleeve.append(i)

          for i in range(number_of_halfsleeve_shirts_tshirts):
              address_to_half_sleeve.append(i)

          # addressing done

          # asking for temperature

          choice = int(output[6])
          temperature_integral_value = -1
          while(True):
              if choice == 1:
                  temp = output[7]
                  temperature_integral_value = int(temp)
                  break
              elif choice == 2:
                  print("Dont worry we will read wheather report for you")

                  #API call for the temperature
                  #*************************************************************************************
                  # Enter your API key here
                  api_key = "e376bdd305b3501ab3ed789f7a1a2787"

                  # base_url variable to store url
                  base_url = "http://api.openweathermap.org/data/2.5/weather?"

                  # Give city name
                  city_name = output[7]

                  # complete_url variable to store
                  # complete url address
                  complete_url = base_url + "appid=" + api_key + "&q=" + city_name

                  # get method of requests module
                  # return response object
                  response = requests.get(complete_url)

                  # json method of response object
                  # convert json format data into
                  # python format data
                  x = response.json()

                  # Now x contains list of nested dictionaries
                  # Check the value of "cod" key is equal to
                  # "404", means city is found otherwise,
                  # city is not found
                  if x["cod"] != "404":

                      # store the value of "main"
                      # key in variable y
                      y = x["main"]

                      # store the value corresponding
                      # to the "temp" key of y
                      current_temperature = y["temp"]
                      temperature_in_cel = int(current_temperature) - 273

                      # store the value corresponding
                      # to the "humidity" key of y
                      current_humidiy = y["humidity"]

                      # print following values
                      print("Temperature (Celcius) = " + str(temperature_in_cel))
                      print("Humidity = " + str(current_humidiy))

                  else:
                      print("City Not Found ")

                  #***************************************************************************************************
                  #APi call ends Here

                  temperature_integral_value = temperature_in_cel

                  break

              else:
                  choice = int(input("Invalid Input , Please provide input again : "))

          # temperature taken

          # temp_speak_to_user = "Oh, It is " + str(temperature_in_cel) + "Celcius temperature at" + user_city
          # speak(temp_speak_to_user,str(24))

          # Deciding the season based on the temperature

          season = "none"

          if 0 <= temperature_integral_value <=18:
              season = "Exterme Winter"
          elif 19 <= temperature_integral_value <= 24:
              season = "Winter"
          elif 25<= temperature_integral_value <= 34:
              season = "summer"
          elif 35<= temperature_integral_value  <= 39:
              season = "Extreme Summer"
          else:
              season = "none"

          # season decided

          season_speak_to_user = "Oh its " + season + " according to me,I am looking for something good in your digital wardrobtill then please wait"
          # speak(season_speak_to_user,str(25))

          #speak("Oh,I found one match it will pop up in new window,Please have a look",str(26))

          print("Check Your Wear for Today in new window :--")

          #temp_speak_to_user = "Oh, It is " + str(temperature_in_cel) + "Celcius temperature at" + user_city
          #speak(temp_speak_to_user, str(24))

          season_speak_to_user = "Oh its " + season + " according to me,I am looking for something good in your digital wardrobtill then please wait"
          speak(season_speak_to_user, str(25))

          speak("Oh,I found one match it will pop up in new window,Please have a look", str(26))

          # creating address manually and poping up wear

          if season == "Exterme Winter":
              if(avoid_repetions_of_cloth>number_of_sweaters):
                  avoid_repetions_of_cloth = 0
              pic_address = r"C:\Users\saura\PycharmProjects\pythonProjectAutoMated\Images"+ user_name +"\sw" + str(address_to_sweaters[avoid_repetions_of_cloth]) + ".jpg"
              avoid_repetions_of_cloth+= 1

              img = cv2.imread(pic_address, -1)
              cv2.imshow('Your_Wear_For_Today', img)
              cv2.waitKey(0)
              cv2.destroyAllWindows()

              print(pic_address)


          elif season == "Winter":
              if(avoid_repetions_of_cloth>number_of_sweatshirts):
                  avoid_repetions_of_cloth = 0
              pic_address = r"C:\Users\saura\PycharmProjects\pythonProjectAutoMated\Images" + user_name +  "\swt" + str(address_to_sweatshits[avoid_repetions_of_cloth]) + ".jpg"
              avoid_repetions_of_cloth+= 1

              img = cv2.imread(pic_address,-1)
              cv2.imshow('image',img)
              cv2.waitKey(0)
              cv2.destroyAllWindows()

              print(pic_address)

          elif season == "summer":
              if(avoid_repetions_of_cloth>number_of_fullsleeve_shirts_tshirts):
                  avoid_repetions_of_cloth = 0
              pic_address = r"C:\Users\saura\PycharmProjects\pythonProjectAutoMated\Images" + user_name +r"\fullsv" + str(address_to_full_sleeve[avoid_repetions_of_cloth]) + ".jpg"
              avoid_repetions_of_cloth+= 1

              img = cv2.imread(pic_address, -1)
              cv2.imshow('Your_Wear_For_Today', img)
              cv2.waitKey(0)
              cv2.destroyAllWindows()

              print(pic_address)

          elif season == "Extreme Summer":
              if(avoid_repetions_of_cloth>number_of_halfsleeve_shirts_tshirts):
                  avoid_repetions_of_cloth = 0
              pic_address = r"C:\Users\saura\PycharmProjects\pythonProjectAutoMated\Images" + user_name + "\halfsv" + str(address_to_half_sleeve[avoid_repetions_of_cloth])+".jpg"
              avoid_repetions_of_cloth+= 1

              img = cv2.imread(pic_address, -1)
              cv2.imshow('Your_Wear_For_Today', img)
              cv2.waitKey(0)
              cv2.destroyAllWindows()

              print(pic_address)

          else:
              print("Sorry , even I am confused now ")

          print("\nThank You !")

          # address creation done  and new window opens with todays wear pi


          speak("thank You for using our service",str(27))


