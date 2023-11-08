import requests, sys
import json
import pandas as pd


def get_accession(gene_name):
    requestURL = f"https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=100&gene={gene_name}"
    
    r = requests.get(requestURL, headers={ "Accept" : "application/json"})

    if not r.ok:
      r.raise_for_status()
      sys.exit()

    responseBody = r.text
    try:
        json_response = json.loads(responseBody)[0]["accession"]
    except:
        json_response = gene_name

    return json_response

def get_protein_info(accession):
    requestURL = f"https://www.ebi.ac.uk/proteins/api/proteins/{accession}"

    r = requests.get(requestURL, headers={ "Accept" : "application/json"})

    if not r.ok:
      r.raise_for_status()
      sys.exit()

    responseBody = r.text
    try:
        json_response = json.loads(responseBody)
    except:
        json_response = {}

    return json_response

def extract_protein_info(accession, response):
    df =pd.DataFrame({"id":response["id"], "taxid":str(response["organism"]["taxonomy"]), 
                      "organism":response["organism"]["names"][0]["value"], 
                      "comments": response["comments"][0]["text"][0]["value"], 
                      "sequence":response["sequence"]["sequence"], 
                      "sequence_length":response["sequence"]["length"], 
                      "sequence_mass":response["sequence"]["mass"]}, index=[accession])
    return(df)