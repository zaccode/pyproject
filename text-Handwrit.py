import pywhatkit as pw

txt = """@RandomDavis i got the file in PycharmProjects\pythonProject\venv\Lib\site-packages when it was installed and the issue was that the module itself wasn't working it didn't give me suggestions when I did "speedtest." and it gave me that error I talked about in the question when I tried to type "speedtest.Speedtest()" without the auto complete (suggestions) and the my script's name is different from the module's name so that is why i moved the module to the script directory because they were different names and i didn't have to rename"""

# text_to_handwriting(text="",pathname="",color="") bydefault blue color 
pw.text_to_handwriting(txt,"hw.png",[0,0,138])#[0,0,138] color code
print(" End ")