{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1c16f0ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime\n",
    "\n",
    "\n",
    "class logger:\n",
    "\n",
    "    def __init__(self, file='logFiles.log'):\n",
    "        self.f_name = file\n",
    "\n",
    "    def info(self, log_type, log_message):\n",
    "        now = datetime.now()\n",
    "        current_time = now.strftime(\"%d-%m-%y %H:%M:%S\")\n",
    "        f = open(self.f_name, \"a+\")\n",
    "        f.write(current_time + \",\" + log_type + \",\" + log_message + \"\\n\")\n",
    "        f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37ecb650",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
