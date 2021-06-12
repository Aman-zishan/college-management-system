<p align="center">
 <img height="159px" src="docs/logo.png" />
 </p>


<div align="center">


[![Website perso.crans.org](https://img.shields.io/website-up-down-green-red/http/perso.crans.org.svg)](http://perso.crans.org/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Aman-zishan/textextractor2.0.svg)](https://github.com/Aman-zishan/textextractor2.0/blob/master/LICENSE)

</div>

<h3> Tech stack used: :octocat: </h3>

<li>Visual Code Studio</li>
<li>python</li>
<li>Django</li>
<li>Database : sqlite3</li>



<h3>Installation :gem: </h3>

1. **:round_pushpin: clone the repository.**

   ```shell
   $git clone https://github.com/Aman-zishan/college-management-system.git

   ```
2. **:checkered_flag: navigate to downloaded folder.**

   ```shell
   $cd college-management-system

   ```
3. **:construction: set up virtual environment.**

   ```shell
   #windows
   
   $py -3 -m venv venv
   
   #linux/mac OS
   
   $python3 -m venv venv

   ```
4. **:diamonds: activate virtual environment.**

   ```shell
   #windows

   $venv\Scripts\activate
   
   #linux/mac OS
   
   $source venv/bin/activate

   ```
5. **:hot_pepper: install django & other required dependencies**
    ```shell
    
    #windows
    

   $pip install -r requirements.txt
   
   #linux/mac OS
   
  
   $pip3 install -r requirements.txt

   ```
6. **:dart: setup database and run server**
    ```shell
   #make sure to delete all files excluding __init__.py before migration to avoid operation errors.

    
   $python manage.py makemigrations
   $python manage.py migrate
   $python manage.py runserver

   ```
 # ER diagram
 
 ![ER diagram](https://user-images.githubusercontent.com/55238388/121786670-14150700-cbdf-11eb-8853-1c2a739082dd.png)




