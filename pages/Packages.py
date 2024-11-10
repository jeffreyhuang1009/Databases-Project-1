from flask import Flask, flash, redirect, render_template, request, session, abort,Blueprint, url_for
import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError, DataError
uri=''
engine=create_engine(uri)
