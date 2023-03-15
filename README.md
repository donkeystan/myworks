### These are my works

#### 1. Programming related works

- **C**

  - Garment Measurement Record Tool

    - To Compile this program

      ```powershell
      cd \Stan_Project\1. C\Garment Measurement
      gcc .\sys_measure_v0.0.1.c
      ```
      
    - Introduction

      > This is my first project, I tried use C to make a simple input and then text record output program.
      >
      > It's designed for a friend who runs a small uniform company.
      >
      > There is a concept self-made data-base using tree, and linked-list under construction.
      >

      

  - Grid Puzzle

    - o Compile this program

      ```powershell
      cd \Stan_Project\1. C\Garment Measurement
      gcc .\sys_measure_v0.0.1.c
      ```

    - Introduction
    
      > This is a small game built just for fun.
      >
      > By updating the TILE and the BOARD_ROW_SIZE BOARD_COL_SIZE, the Grid Puzzle can be enlarged
    
      
    
      

- **Python**

  - **Parser** 

    - **Inventory Generator**

      - To run this script, go to the designated directory 

        ```powershell
        cd \Stan_Project\2. Python\1. Parser\1. Parser_inventory_generator
        python .\INV_GEN_V1.0.py
        ```

        a new folder and a human readable report file will be generated.

      - Introduction

        > Our company's ERP system does not generate a proper inventory report for staff's quick reference,
        >
        > so I write this script to quickly organize a human readable excel chart for my colleagues.
        >
        > This program can be packed to an executable file for windows.

      

    - **Inventory History Generator**

      - To run this script, go to the designated directory 

        ```powershell
        \Stan_Project\2. Python\1. Parser\2. Parser_inventory_history_generator
        ```

        then open the PART_HX_WH_(MULTIPLE)_v1.py file with any IDE

        change the wh_list[ ]  and part_list[ ] if certain Part No and Warehouse No is required

        then run the python script file

        ```powershell
        python .\PART_HX_WH_(MULTIPLE)_v1.py
        ```

      - Introduction

        > Our company's ERP system does not keep record of how the inventory changes,
        >
        > so I made this script to allow people to find the inventory changes within a certain period of time

      

    - **PO Splitter**

      - To run this script, go to the designated directory 

        ```powershell
        \Stan_Project\2. Python\1. Parser\3. Parser_PO_splitter
        ```

        make sure to change the customer [studio A]  PO's name to **in.XLSX**

        then run the python script file

        ```powershell
        python xls_split_v1.py
        ```

      - Introduction

        > One of our customer Studio A always issue PO to us with just an Excel file. They have more than 40 stores in Taiwan.
        >
        > Our ERP system can only handle one purchase order a time, so all 40 stores information has to separated into 40 excel files.
        >
        > I wrote this script to help our colleague saves time of splitting an Excel file to 40 or more excel files.

    

  - **Framework - Django**

    - **Uniform Measurement System**

      - To run this system, go to the designated directory

        ```powershell
        \Stan_Project\2. Python\2. Framework_Django\hf_uniform
        ```

        To prevent error, it is recommended to run under virtual environment with Django V3.2.3 installed

        then run the following

        ```powershell
        python manage.py runserver //a designated IP can be assigned to it
        ```

        then in your web browser, type in http://127.0.0.1:8000 if no designated IP is given.

        to login, a temp username: danielliu and password: hofo1981 can be used to test the system.

      - Introduction

        >This is a system built for my friend who runs a small uniform business. It is designed for him to put the customer uniform measurement record into the system through a web browser on a laptop or mobile phone.
        >
        >Any change made or system logging in will be written in the file log.txt
        >
        >Currently my friend is checking what kind of module he needs, and I will help him extend the system in the future.

      

    - **ToDo List**

      - To run this system, go to the designated directory

        ```powershell
        \Stan_Project\2. Python\2. Framework_Django\todo_list
        ```

        To prevent error, it is recommended to run under virtual environment with Django V3.2.3 installed

        then run the following

        ```powershell
        python manage.py runserver //a designated IP can be assigned to it
        ```

        then in your web browser, type in http://127.0.0.1:8000/todo/ if no designated IP is given.

      - Introduction

        >This is a project made my classmate in NTUB, where the teacher want us to build tools using Django.

      

    - **Notes**

      - To run this system, go to the designated directory

        ```powershell
        \Stan_Project\2. Python\2. Framework_Django\notes
        ```

        To prevent error, it is recommended to run under virtual environment with Django V3.2.3 installed

        then run the following

        ```powershell
        python manage.py runserver //a designated IP can be assigned to it
        ```

        then in your web browser, type in 127.0.0.1:8000 if no designated IP is given.

        to login, two temp users can be logged in to access individual's contents

        user1: lynnpan password1: lynn123456

        user2: johnliu password2: john654321

      - Introduction

        >Same as the ToDo List, this app is built for a classmate in NTUB.
        >
        >The notes app allows different people logging in to access different contents.

    

  - **Data Analysis**

    - **NASA Near Earth Object Analysis**

      To see the Data Analysis, go to the directory
      
      ```powershell
      \Stan_Project\2. Python\3. Data Analysis
      ```
      
      and open the NASA_near_earth_object.ipynb with VS Code with the extension
      
      or just click the following link to see a cloud version
      
      https://colab.research.google.com/drive/1XyY1iWnIHLGcU8yuEcRfzjqKq7sigpXW#scrollTo=67mAxAD78I6t
      
    - Introduction
    
      > I tried to learn the Data Analysis, so I search kaggle.com for free Data Sets to do my practice on Data Analysis
    
    

- **JavaScript**

  - **Boundary Cap Holes**
    
    - **Hand Control Version**
    
      - To run this web page, just go to the diretory
    
        ```powershell
        \Stan_Project\3. JavaScript\BOUNDARY_CAP HOLES\Hand_control\radom_exhibit_v3.3
        ```
    
        directly open up the file < rand.html > and then click only once anywhere on the page
    
        The PC used to run this page must have a web camera to activate the hand control
    
      - Introduction
    
        > This web page is created for an Art Exhibition called "BOUNDARY_CAP HOLES" owned by my brother-in-law,
        >
        > who opened a small workshop of art.
        >
        > I use the media pipe to capture the hand gesture and then extract and process the data for DOM object controls
        >
        > On the page, there will be random video pop up and vanish. You can drag, zoom, rotate or kill a random video by hand.
    
        
    
    - **No Hand Control Version**
    
      - To run this web page, just go to the diretory
    
        ```powershell
        \Stan_Project\3. JavaScript\BOUNDARY_CAP HOLES\No_hand_control\radom_exhibit
        ```
    
        directly open up the file < rand.html > and then click only once anywhere on the page
    
        
    
      - Introduction
    
        > This is the first version web page for Art Exhibition called "BOUNDARY_CAP HOLES" owned by my brother-in-law,
        >
        > who opened a small workshop of art.
        >
        > On the page, there will be random video pop up and vanish.
    
    
    
  - **Uniform Measurement Page**
  
    - To run this web page, just go to the diretory
  
      ```powershell
      Stan_Project\3. JavaScript\Garments_Input
      ```
  
      directly open up the file < measurement.html > and the page can be used to save temporary data
  
      
  
    - Introduction
  
      > This is a single web page version for my friend's uniform workshop.
      >
      > It's made to put in his laptop to prevent system failure, and he can use this page directly for record saving.



#### 2. Excel VBA Macro

- **Inventory Generator**

  - To run the Excel macro, go to the directory

    ```powershell
    \Stan_Project\4. Excel_VBA Macro
    ```

    open < infinite_loop_v1.3.1.xlsm >  and the raw data < inventory.XLSX >

    and in the developer tab, chose macro and then run < infinite_loop_v1.3.1.xlsm!inventory_check > macro

  - Introduction

    > This is the excel version of inventory generator
    >
    > It's made to turn the system raw data to human readable report.

  

- **Sales Record Generator**

  - To run the Excel macro, go to the directory

    ```powershell
    \Stan_Project\4. Excel_VBA Macro
    ```

    open < infinite_loop_v1.3.1.xlsm >  and the raw data < sales record_0220.XLSX >

    and in the developer tab, chose macro and then run < infinite_loop_v1.3.1.xlsm!sales_check > macro

  - Introduction

    > This macro is to help supervisor to quickly get the right pivot data to see each salesperson's sales record
    >
    > It's made to turn the system raw data to human readable report.




#### 3. 3D Works

- ProE
  - TV WALL MOUNT 01
  - TV WALL MOUNT 02
- Keyshot
  - TV Wall Mount 32-55
  - TV Wall Mount 32-70
  - 11in1 Keyboard Hub

 