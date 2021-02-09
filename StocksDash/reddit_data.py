import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table 
from dash.exceptions import PreventUpdate
import flask
from flask import Flask
import pandas as pd
import dateutil.relativedelta
from datetime import date
import datetime
import yfinance as yf
import numpy as np
import praw
import sqlite3
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from config import r_cid, r_csec, r_uag
def get_reddit(cid= r_cid, csec= r_csec, uag= r_uag, subreddit='wallstreetbets'):
   
    #connect to reddit
    reddit = praw.Reddit(client_id= cid, client_secret= csec, user_agent= uag)
#get the new reddit posts
    posts = reddit.subreddit(subreddit).new(limit=None)
#load the posts into a pandas dataframe
    p = []
    for post in posts:
        p.append([post.title, post.score, post.selftext])
    posts_df = pd.DataFrame(p,columns=['title', 'score', 'post'])
    
    return posts_df
