#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# VJackson, 2021-Aug-30, added code in place of TODO/pseudo code, added DataIO   
# -----------------------class, added constructors,setters,getters. 
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __str__: (string): Returns formatted CD details

    """

    # -- Constructor -- #
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str) -> None:
        #    -- Attributes  -- #
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist

    # -- Properties -- #
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = value

    # CD title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = value

    # CD artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = value

    # -- Methods -- #
    def __str__(self):
        return '{}\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    def load_inventory(file_name, lst_Inventory: list) -> None:
        """
        Function to manage data ingestion from file to a list of dictionaries

        Loads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one row in table.

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list): list of CD objects.

        Returns:
            None.

        """
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
            file.close()
        except FileNotFoundError:
            FileIO.save_inventory(strFileName, lstOfCDObjects)

    def save_inventory(file_name, lst_Inventory: list) -> None:
        """
        Function to write data in lstTbl to a data file

        Writes the data from a 2D table into a file identified by file_name
        (list of dicts) table one line in the file represents one row in table.

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list): list of CD objects.

        Returns:
            None.

        """
        try:
            with open(file_name, 'w') as objFile:
                for cd in lst_Inventory:
                    objFile.write('{},{},{}\n'.format(cd.cd_id, cd.cd_title, cd.cd_artist))
            objFile.close()
        except Exception:
            print('There was an error writing to file!')

class DataIO:
    """Processes data within the program:

    properties:

    methods:
        add_cd(file_name, lst_Inventory): -> None
        
    """

    @staticmethod
    def add_CD(objCDData, lst_inventory):
        """function to add CD info to the inventory table.

        References the values in return tuple from a function (IO.get_CD_data)
        then appends to a 2D table (lst_inventory).

        Args:
            ObjCDData (tuple): Containts values for ID, CD Title, CD Artist to be added to inventory.
            lst_inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        cdId, title, artist = objCDData
        row = CD(cdId, title, artist)
        lst_inventory.append(row)
        print('CD Added: ' + row.__str__())


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.

        """
        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD')
        print('[i] Display Current Inventory\n[s] Save Inventory to file\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '        
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(lst_inventory):
        """Displays current inventory table


        Args:
            lst_inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_inventory:
            print(row)
        print('======================================')

    @staticmethod 
    def get_CD_data():
        """function to request CD information from User to add CD to inventory

        Args:
            None.

        Returns:
            Tuple: objects with user input values for new ID, CD Title, and Artist

        """
        while True:
            try:
                strID = int(input('Enter ID: ').strip())
                break
            except ValueError:
                print('Please enter a number!')
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return (strID, strTitle, strArtist)


# -- Main Body of Script -- #
# 1. When program starts, read in the currently saved Inventory
FileIO.load_inventory(strFileName, lstOfCDObjects)

while True:
    # Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        CdData = IO.get_CD_data()
        # 3.3.2 Add item to the table
        DataIO.add_CD(CdData, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.5 process save inventory to file
    elif strChoice == 's':
        # 3.5.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')
