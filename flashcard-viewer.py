import dearpygui.dearpygui as dpg
import json, StateManager, Flashcard, FlashcardHandler

def main():

    reader = StateManager.StateManager("./data/") # My file reader class, I wouldn't recommend using this anywhere.
    cards = []

    # Load the data stored in all my flashcard files...
    reader.openFile("domainOneFlashcards.json")
    for i in range(55):
        next = Flashcard.Flashcard(json=(json.loads(reader.readData())))
        cards.append(next)
    reader.closeFile()

    reader.openFile("domainTwoFlashcards.json")
    for i in range(16):
        next = Flashcard.Flashcard(json=(json.loads(reader.readData())))
        cards.append(next)
    reader.closeFile()

    reader.openFile("domainThreeFlashcards.json")
    for i in range(28):
        next = Flashcard.Flashcard(json=(json.loads(reader.readData())))
        cards.append(next)
    reader.closeFile()

    reader.openFile("domainFourFlashcards.json")
    for i in range(38):
        next = Flashcard.Flashcard(json=(json.loads(reader.readData())))
        cards.append(next)
    reader.closeFile()

    reader.openFile("domainFiveFlashcards.json")
    for i in range(34):
        next = Flashcard.Flashcard(json=(json.loads(reader.readData())))
        cards.append(next)
    reader.closeFile()

    # Create DPG variables...
    dpg.create_context()
    content = None
    cardList = FlashcardHandler.FlashcardHandler(cards)

    def prevcommand(): # Go to the previous card in the list
        cardList.previous()
        dpg.set_value("content", value=cardList.getText())

    def flipcommand(): # Flip the card over so you can read what's on the other side
        cardList.swap()
        dpg.set_value("content", value=cardList.getText())

    def nextcommand(): # Go to the next card in the list
        cardList.next()
        dpg.set_value("content", value=cardList.getText())

    # Draw the main window, and section it off for: card content at the top, and buttons for prev, flip, and next commands.
    with dpg.window(label="Example Window", tag="Primary Window"):
        with dpg.child_window(autosize_x=True, height=500, tag="Card Window"):
            content = dpg.add_text(default_value=cardList.getText(),tag="content", wrap=0)
        with dpg.table(tag="idk lol", header_row=False):
            button_width = 255
            button_height = 60
            dpg.add_table_column()
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_button(label="Previous", width=button_width, height=button_height, callback=prevcommand)
                dpg.add_button(label="Flip", width=button_width, height=button_height, callback=flipcommand)
                dpg.add_button(label="Next", width=button_width, height=button_height, callback=nextcommand)

    # This removes the gray-ish background that is default on DGP windows. I wanted it to stay black, but I ended up having the UI fill the window so this part doesn't actually change anything.
    with dpg.theme(tag="no_bg_theme"):
        with dpg.theme_component(dpg.mvWindowAppItem):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (0, 0, 0, 0))
            dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 0, 0, 0))
    dpg.bind_item_theme("Primary Window", "no_bg_theme")

    # Create the window and set the font size to be fairly readable.
    dpg.create_viewport(title='Flashcards', width=800, height=584)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.set_global_font_scale(2)

    # The render loop required for rendering frames. I could have used 'dpg.start_dearpygui()' instead, but I felt like setting it up manually so I did this.
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

# Runs the program if and only if this file is called to run through terminal.
if __name__ == "__main__":
    main()
