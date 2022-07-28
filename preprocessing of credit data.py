{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6310b98",
   "metadata": {},
   "outputs": [],
   "source": [
    "from imblearn.over_sampling import ADASYN\n",
    "from collections import Counter\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import warnings\n",
    "import pickle\n",
    "\n",
    "\n",
    "pd.set_option('display.max_columns',None)\n",
    "warnings.filterwarnings(action='ignore')\n",
    "\n",
    "\n",
    "df = pd.read_csv(r\"C:\\Users\\Lenovo\\PycharmProjects\\GermanBankCreditCard\\SouthGermanCredit\\Preprocess.csv\")\n",
    "df.drop(['Unnamed: 0'],axis=1,inplace=True)\n",
    "\n",
    "\n",
    "df.isnull().sum()\n",
    "\n",
    "\n",
    "q1 = df.quantile(0.25)\n",
    "q3 = df.quantile(0.75)\n",
    "IQR = q3-q1\n",
    "\n",
    "\n",
    "((df < (q1-1.5*IQR)) | (df > (q3+1.5*IQR))).sum()\n",
    "\n",
    "\n",
    "columns=['duration','purpose','amount','other_debtors','age','other_installment_plans','housing','number_credits','job',\n",
    "        'people_liable','foreign_worker']\n",
    "for i in columns:\n",
    "    q75,q25=np.percentile(df[i],[75,25])\n",
    "    iqr=q75 - q25\n",
    "    minimum = q25 - 1.5*iqr\n",
    "    maximum = q75 + 1.5*iqr\n",
    "    df.loc[df[i] < minimum, i] = minimum\n",
    "    df.loc[df[i] > maximum, i] = maximum\n",
    "\n",
    "\n",
    "((df < (q1-1.5*IQR)) | (df > (q3+1.5*IQR))).sum()\n",
    "\n",
    "\n",
    "df.skew()\n",
    "\n",
    "col=['amount','savings','number_credits']\n",
    "for i in col:\n",
    "    df[i]=np.log(df[i]+1)\n",
    "\n",
    "\n",
    "df.skew()\n",
    "\n",
    "\n",
    "for i in df.columns:\n",
    "    sns.displot(data=df,x=i,kde=True)\n",
    "\n",
    "\n",
    "del df['other_debtors']\n",
    "del df['other_installment_plans']\n",
    "del df['housing']\n",
    "del df['job']\n",
    "del df['people_liable']\n",
    "del df['foreign_worker']\n",
    "\n",
    "\n",
    "scaling = [feature for feature in df.columns if feature not in ['credit_risk']]\n",
    "\n",
    "\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "scaler = StandardScaler()\n",
    "scaler.fit(df[scaling])\n",
    "\n",
    "\n",
    "scaler.transform(df[scaling])\n",
    "\n",
    "\n",
    "df2=pd.DataFrame(scaler.transform(df[scaling]),columns=df[scaling].columns)\n",
    "\n",
    "\n",
    "final=pd.concat([df[['credit_risk']].reset_index(drop=True),df2],axis=1)\n",
    "final.head()\n",
    "\n",
    "\n",
    "final.to_csv(r'C:\\Users\\Lenovo\\PycharmProjects\\GermanBankCreditCard\\SouthGermanCredit\\Final_Model.csv')\n",
    "\n",
    "\n",
    "file = 'Scaler_Credit_Data.pkl'\n",
    "\n",
    "pickle.dump(scaler,open(file,'wb'))"
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