{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f533872b-200b-46da-a910-b9ea04196a52",
   "metadata": {},
   "source": [
    "Commands of Git and GIThub:\n",
    "\n",
    "Gitbash general commands: \n",
    "1) vim -> lets you edit a file present in the local repo or a new one\n",
    "       eg: vim helloworld.py will create a file if it doesn't exist\n",
    "   a) after entering the file we can edit by clicking in 'i' for insert and edit the file.\n",
    "   b) after inserting click on 'esc' and ':q' or ':wq' to get out of the file\n",
    "2) cat-> will show the content of the file [read only]\n",
    "       eg: cat helloworld.py or cat <file name>\n",
    "3) ls will list all the files in particular folder location.\n",
    "4) git config --global user.name <username> will update the user name as per the github so we can establish connection\n",
    "5) git config --global  user.email <emailid> will update the emailid\n",
    "6) git config --global -e \n",
    "\n",
    "Cloning form the github:\n",
    "1) create a local repo using mkdir command or directly create folders in desired location.\n",
    "2) use 'cd' to navigate to the folder location\n",
    "3) git clone <git link obtained from the github>[this will clone all the files from the github to the local machine]\n",
    "\n",
    "How to push changes made in the loca machine to github:\n",
    "1) 'git add .': this will add all the files in the local machine to staging are which is ready to be committed\n",
    "2) 'git add <file name> will add only one fle\n",
    "3) git commit -m 'comments' will commit the changes to local repo\n",
    "4) git push -f origin <branch> main or master based on the name will push the changes to github\n",
    "\n",
    "   \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a613684d-5c17-4b47-b26b-794d8cbeccb9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
