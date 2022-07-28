{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1fc8fe9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Database Name : South German Bank Data\n",
    "# Keyspace Name : credit\n",
    "# Table Name : credit_data\n",
    "\n",
    "from cassandra.auth import PlainTextAuthProvider\n",
    "from cassandra.cluster import Cluster\n",
    "from application_logging.logger import logger\n",
    "import pandas as pd\n",
    "import csv\n",
    "\n",
    "logger = logger('log_Files/Database.log')\n",
    "\n",
    "\n",
    "class dataBaseOperation:\n",
    "\n",
    "    def __init__(self):\n",
    "\n",
    "        logger.info('INFO', 'Trying To Connect With The Database')\n",
    "        self.keyspace = 'credit'\n",
    "\n",
    "        self.table_name = 'credit_data'\n",
    "\n",
    "        self.client_id = 'fDFMepzLgZIZqCkXgbEEeffc'\n",
    "\n",
    "        self.client_secret = 'dqpA4MgjHlqiKrSBMh,OdE_cNhsy_6Zv.3hSFgA5C2AIkPtQxMQcep1NOovoYapYKgzBL1nj6xxD5c7JH6FYcbsEIX8EwFo8Un4W5BGtHqZi.j81q4HnCNLRp3oLtzS7'\n",
    "\n",
    "        self.cloud_config = {\n",
    "            'secure_connect_bundle': r\"C:\\Users\\Lenovo\\PycharmProjects\\GermanBankCreditCard\\secure-connect-south-german-bank-data.zip\"}\n",
    "\n",
    "        auth_provider = PlainTextAuthProvider(self.client_id, self.client_secret)\n",
    "        cluster = Cluster(cloud=self.cloud_config, auth_provider=auth_provider)\n",
    "        self.session = cluster.connect()\n",
    "        logger.info('INFO', 'The Connection Is Created')\n",
    "\n",
    "    def usekeyspace(self):\n",
    "\n",
    "        try:\n",
    "\n",
    "            logger.info('INFO', 'Using The Keyspace That We Created At Time of Database Creating')\n",
    "            self.session.execute(\"USE {keyspace};\".format(keyspace=self.keyspace))\n",
    "\n",
    "            # print('Using The energy Keyspace')\n",
    "            logger.info('INFO', 'The {keyspace} Is Selected'.format(keyspace=self.keyspace))\n",
    "\n",
    "        except Exception as e:\n",
    "            raise Exception(f\"(useKeySpace) - Their Is Something Wrong About useKeySpace Method \\n\" + str(e))\n",
    "\n",
    "    def createtable(self):\n",
    "\n",
    "        try:\n",
    "\n",
    "            logger.info('INFO', 'Table Is Creating Inside The Selected Keyspace')\n",
    "            self.session.execute(\"USE {keyspace};\".format(keyspace=self.keyspace))\n",
    "\n",
    "            self.session.execute(\n",
    "                \"CREATE TABLE {table_name}(ID int PRIMARY KEY,status int, duration int,credit_history int,purpose int,\"\n",
    "                \"amount int,savings int,employment_duration int,installment_rate int,personal_status_sex int,\"\n",
    "                \"other_debtors int,present_residence int,property int, age int, other_installment_plans int,\"\n",
    "                \"housing int, number_credits int, job int, people_liable int, telephone int,foreign_worker int,\"\n",
    "                \"credit_risk int);\".format(table_name=self.table_name))\n",
    "\n",
    "            # print('Table Is Created Inside The Keyspace')\n",
    "\n",
    "            logger.info('INFO', 'The Table Is Created Inside The {keyspace} With Name {table_name}'.format(\n",
    "                        keyspace=self.keyspace, table_name=self.table_name))\n",
    "\n",
    "        except Exception as e:\n",
    "            raise Exception(f\"(createTable) - Their Is Something Wrong About Creating Table Method \\n\" + str(e))\n",
    "\n",
    "    def insertintotable(self):\n",
    "\n",
    "        try:\n",
    "\n",
    "            logger.info('INFO', 'Inserting The Data Into DATABASE')\n",
    "            file = \"SouthGermanCredit\\SouthGermanCredit.csv\"\n",
    "            with open(file, mode='r') as f:\n",
    "                next(f)\n",
    "\n",
    "                reader = csv.reader(f, delimiter='\\n')\n",
    "                for i in reader:\n",
    "\n",
    "                    data = ','.join([value for value in i])\n",
    "                    self.session.execute(\"USE {keyspace};\".format(keyspace=self.keyspace))\n",
    "\n",
    "                    self.session.execute(\n",
    "                        \"INSERT INTO {table_name} (ID,status,duration,credit_history,purpose,amount,savings,\"\n",
    "                        \"employment_duration,installment_rate,personal_status_sex,other_debtors,present_residence,\"\n",
    "                        \"property,age,other_installment_plans,housing,number_credits,job,people_liable,telephone,\"\n",
    "                        \"foreign_worker,credit_risk) VALUES ({data});\".format(table_name=self.table_name, data=data))\n",
    "\n",
    "                # print('Data Is Inseted')\n",
    "                logger.info('INFO', 'All The Data Entered Into The {keyspace} Having Table Name {table_name}'.\n",
    "                            format(keyspace=self.keyspace, table_name=self.table_name))\n",
    "\n",
    "        except Exception as e:\n",
    "            raise Exception(f\"(insertintotable) - Their Is Something Wrong About Insert Into Data Method \\n\" + str(e))\n",
    "\n",
    "    def getdatafromdatabase(self):\n",
    "\n",
    "        try:\n",
    "\n",
    "            logger.info('INFO', 'Trying To Get The Data From The DataBase')\n",
    "            df = pd.DataFrame()\n",
    "\n",
    "            query = \"SELECT * FROM {keyspace}.{table_name};\".format(keyspace=self.keyspace, table_name=self.table_name)\n",
    "            for row in self.session.execute(query):\n",
    "\n",
    "                df = df.append(pd.DataFrame([row]))\n",
    "\n",
    "            logger.info('INFO', 'We Gathered The Data From DataBase {}'.format(df))\n",
    "        except Exception as e:\n",
    "            raise Exception(f\"(getData) - Their Is Something Wrong About getData Method \\n\" + str(e))"
   ]
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
