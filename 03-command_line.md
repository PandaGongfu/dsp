# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a *cheat sheet* for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> >   
    1. *pushd/popd dir* = switch directory  
    2. *touch file* = create empty file  
    3. *mv old new* = rename file or folder  
    4. *man cmd* = find help for command  
    5. *wc file* = wordcount  
    6. *less file* = show content of file  
    7. *export/echo var* = set new env variable  
    8. *env | grep name* = find env variables containing name 
    9. *grep word file* = find word in file  
    10. *grep -E exp file* = find word using reg expression  
      

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
  `ls` list files in the current directory  
  `ls -a` do not ignore entries starting with .  
  `ls -l` use a long listing format  
  `ls -lh` print sizes in human readable format  
  `ls -lah` list files including hidden files in human readable format  
  `ls -t` list files sorted by the time they were last modified  
  `ls -Glp` use long listing, append '/' to directories and don't print group names

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
    Option | Description
    ------ | -----------
    -c | Displays files by timestamp
    -m | Display the names as a comma-separated list
    -r | Displays files in reverse order
    -x | Displays files as rows across the screen
    -1 | Displays each entry on a line 

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 
    UNIX does not accept a long list of arguments from standard input, xargs divides it into small list when used in combination of find and grep.      
    ```  
    find . -name '*.py' | xargs grep 'graph'
    ```  
    This will find the word 'graph' in all py file from the current directory and below.

